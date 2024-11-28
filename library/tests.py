from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book, Borrow

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Author', bio='Test Author Bio')
        self.book = Book.objects.create(title='Test Book', author=self.author, description='Test Book Description', available_copies=10)
        
    def test_list_books(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
    
