from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book, Borrow
from .serializers import AuthorSerializer, BookSerializer, BorrowSerializer, BorrowListSerializer
from .permissions import IsAdminOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly,]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly,]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']
    search_fields = ['title']

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.available_copies <= 0:
            raise Exception('Book is not available')  # Ideally, use a more specific exception like DRF's `ValidationError`
        # Decrement available copies
        book.available_copies -= 1
        book.save()
        # Save the borrow instance with the logged-in user
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        borrow = serializer.instance

        # Construct a custom response
        response_data = {
            'id': borrow.id,
            'book': borrow.book.title,
            'user': borrow.user.username,
            'borrowed_at': borrow.borrowed_at,
            'returned_at': borrow.returned_at,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    


class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id, format=None):
        book = Book.objects.get(pk=book_id)
        try:
            borrow = Borrow.objects.get(user=request.user, book=book)
        except Borrow.DoesNotExist:
            return Response({'message': 'You have not borrowed this book'}, status=400)
        borrow.returned_at = request.data.get('returned_at')
        borrow.save()
        book.available_copies += 1
        book.save()
        return Response({'message': 'Book returned successfully'})
    

class ListBorrowedBooksView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        borrowed_books = Borrow.objects.filter(user=request.user, returned_at=None)
        serializer = BorrowListSerializer(borrowed_books, many=True)
        return Response(serializer.data)

