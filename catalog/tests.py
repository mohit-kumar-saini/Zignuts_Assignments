from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductAPITests(APITestCase):

    def setUp(self):
        self.list_url = reverse('product-list')
        self.sample = {
            'name': 'Mouse',
            'description': 'Wireless mouse',
            'price': '19.50',
            'stock_quantity': 15,
            'category': 'Peripherals',
        }
        self.invalid = {
            'name': 'Bad item',
            'description': 'Negative price',
            'price': '-10.00',
            'stock_quantity': 5,
            'category': 'Misc',
        }

    def test_create_product_success(self):
        resp = self.client.post(self.list_url, data=self.sample, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(resp.data['name'], self.sample['name'])

    def test_fetch_list_and_detail(self):
        p = Product.objects.create(**{
            'name': 'Keyboard',
            'description': 'Mechanical',
            'price': '49.99',
            'stock_quantity': 7,
            'category': 'Peripherals',
        })
        list_resp = self.client.get(self.list_url)
        self.assertEqual(list_resp.status_code, status.HTTP_200_OK)
        detail_url = reverse('product-detail', args=[p.id])
        detail_resp = self.client.get(detail_url)
        self.assertEqual(detail_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_resp.data['name'], 'Keyboard')

    def test_update_and_delete_product(self):
        p = Product.objects.create(**{
            'name': 'Item',
            'description': 'desc',
            'price': '10.00',
            'stock_quantity': 3,
            'category': 'Misc',
        })
        detail_url = reverse('product-detail', args=[p.id])
        update_resp = self.client.put(detail_url, data={
            'name': 'Item Updated',
            'description': 'desc',
            'price': '11.00',
            'stock_quantity': 2,
            'category': 'Misc'
        }, format='json')
        self.assertEqual(update_resp.status_code, status.HTTP_200_OK)
        p.refresh_from_db()
        self.assertEqual(p.name, 'Item Updated')

        del_resp = self.client.delete(detail_url)
        self.assertEqual(del_resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_create_product_invalid_negative_price(self):
        resp = self.client.post(self.list_url, data=self.invalid, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('price' in resp.data or any('price' in k for k in resp.data))
