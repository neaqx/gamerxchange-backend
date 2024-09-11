from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class PostListVeiwTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='test')
    
    def test_create_post(self):
        test=User.objects.get(username='test')
        Post.objects.create(owner=test, title='Test', content='Test')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print (response.data)
        print(len(response.data))
        
    def test_logged_in_user_can_create_post(self):
        test=User.objects.get(username='test')
        response = self.client.post('/posts/', {'title':'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title':'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)