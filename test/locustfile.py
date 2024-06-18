from datetime import datetime

from locust import HttpUser, task, between
import os
from dotenv import load_dotenv
import json
import random

load_dotenv()

class BaseLoad(HttpUser):
    wait_time = between(1, 5)

    def random_login_credentials(self):
        credentials_list = [
            ("johnd", "m38rmF$"),
            ("mor_2314", "83r5^_"),
            ("kevinryan", "kev02937@"),
            ("donero", "ewedon"),
            ("derek", "jklg*_56"),
            ("david_r", "3478*#54"),
            ("snyder", "f238&@*$"),
            ("hopkins", "William56$hj"),
            ("kate_h", "kfejk@*_"),
            ("jimmie_k", "klein*#%*")
        ]

        random_username, random_password = random.choice(credentials_list)
        return random_username, random_password

    @task
    def base_load_login(self):
        payload = {
            'username': 'mor_2314',
            'password': '83r5^_'
        }
        while True:
            username, password = self.random_login_credentials()
            self.client.post("https://fakestoreapi.com/auth/login", json=payload)


    @task
    def spike_login(self):
        payload = {
            'username': 'mor_2314',
            'password': '83r5^_'
        }
        for i in range(1000):
            username, password = self.random_login_credentials()
            self.client.post("https://fakestoreapi.com/auth/login", json=payload)


class UserCreateSpike(HttpUser):
    wait_time = between(1, 5)

    def fake_user(self):
        fake_users = [
            {
                'email': 'example@gmail.com',
                'username': 'example_user',
                'password': 'P@ssw0rd!',
                'name': {
                    'firstname': 'John',
                    'lastname': 'Smith'
                },
                'address': {
                    'city': 'New York',
                    'street': '123 Main Street',
                    'number': 10,
                    'zipcode': '10001',
                    'geolocation': {
                        'lat': '40.7128',
                        'long': '-74.0060'
                    }
                },
                'phone': '1-123-456-7890'
            },
            {
                'email': 'user1@gmail.com',
                'username': 'user1',
                'password': 'Pass123!',
                'name': {
                    'firstname': 'Alice',
                    'lastname': 'Johnson'
                },
                'address': {
                    'city': 'Los Angeles',
                    'street': '456 Oak Avenue',
                    'number': 20,
                    'zipcode': '90001',
                    'geolocation': {
                        'lat': '34.0522',
                        'long': '-118.2437'
                    }
                },
                'phone': '1-987-654-3210'
            },
            {
                'email': 'user2@gmail.com',
                'username': 'user2',
                'password': 'SecurePass!',
                'name': {
                    'firstname': 'Bob',
                    'lastname': 'Miller'
                },
                'address': {
                    'city': 'Chicago',
                    'street': '789 Elm Street',
                    'number': 30,
                    'zipcode': '60601',
                    'geolocation': {
                        'lat': '41.8781',
                        'long': '-87.6298'
                    }
                },
                'phone': '1-567-890-1234'
            },
            {
                'email': 'user3@gmail.com',
                'username': 'user3',
                'password': 'StrongPassword!',
                'name': {
                    'firstname': 'Emily',
                    'lastname': 'Davis'
                },
                'address': {
                    'city': 'Houston',
                    'street': '321 Pine Lane',
                    'number': 40,
                    'zipcode': '77001',
                    'geolocation': {
                        'lat': '29.7604',
                        'long': '-95.3698'
                    }
                },
                'phone': '1-234-567-8901'
            }
        ]

        return random.choice(fake_users)

    @task
    def spike_create_account(self):
        self.client.post("https://fakestoreapi.com/users", json=self.fake_user())


class ProductSearchSpike(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_all_products(self):
        self.client.get("https://fakestoreapi.com/products")

    @task
    def get_single_product(self):
        product_id=random.randint(1, 20)
        self.client.get(f"https://fakestoreapi.com/products/{product_id}")
        return product_id

class FlashSaleOrderSpike(HttpUser):
    wait_time = between(1,5)

    #flash sale for all products
    @task
    def FlashSale(self):
        ProductSearchSpike.get_all_products(self)
        product_Id=ProductSearchSpike.get_single_product(self)

        quantity=random.randint(1,200)
        date= datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        user_Id=random.randint(1,10)

        payload={
            "userId":user_Id,
            "date":date,
            "products":[{"productId":product_Id,"quantity": quantity}]
        }

        self.client.post('https://fakestoreapi.com/carts', json=payload)

    #Flash sale for e specific product, specific ID
    @task
    def FlashSaleSpecificProduct(self):
        ProductSearchSpike.get_single_product(self)
        product_in_sale_id=ProductSearchSpike.get_single_product(self)
        quantity = random.randint(200, 1000)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_Id = random.randint(1, 10)
        payload = {
                "userId": user_Id,
                "date": date,
                "products": [{"productId":  product_in_sale_id, "quantity": quantity}]
            }
        self.client.post('https://fakestoreapi.com/carts', json=payload)



if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --host=https://fakestoreapi.com/")
