from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from faker import Faker
from book.models import Book


class BookAppTest(APITestCase):
    """
    Test cases for book api.
    """
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.data = { 'name': self.fake.name(), 'edition': '2nd', 'author': self.fake.name(), 'price': self.fake.random_digit(), 'timestamp': self.fake.date(), 'time': self.fake.date(), 'is_sold': True, 'is_available': True, 'isbn': self.fake.credit_card_number() }
        isntance = Book(**self.data)
        isntance.save()
        print(self.data)

    def test_to_get_all_books(self):
        """
        Test to get all users and check status.
        """
        url = reverse('book-list')
        res = self.client.get(url)
        print('Response: ', res.status_code)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_create_new_book(self):
        """
        test create new book with valid data and check result.
        """
        url = reverse('book-list')
        print('URL : ----->', url)
        data = { 'name': self.fake.name(), 'edition': '2nd', 'author': self.fake.name(), 'price': self.fake.random_digit(), 'timestamp': self.fake.date(), 'time': self.fake.date(), 'is_sold': True, 'is_available': True, 'isbn': self.fake.credit_card_number() }
        print(data)
        response = self.client.post(url, data, format='json')
        print('Response: ', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_new_book_invalid_data(self):
        """
        test create new book with invalid data and check result.
        """
        url = reverse('book-list')
        data = { 'name': self.fake.name(), 'author': self.fake.name(), 'price': self.fake.random_digit(), 'timestamp': self.fake.date(), 'time': self.fake.date(), 'is_sold': True, 'is_available': True, 'isbn': self.fake.credit_card_number() }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_retrieve_book_api(self):
        """
        test retrieve book api by Id.
        """
        url = reverse('book-detail', args=[1])
        response = self.client.get(url)
        print('Response: ', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_api(self):
        """
        test update book api by Id.
        """
        url = reverse('book-detail', args=[1])
        data = self.data
        data['name'] = 'Rohit Kumar Verma'
        response = self.client.put(url, data, format='json')
        print('Response: ', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

