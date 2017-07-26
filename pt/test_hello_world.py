from django.test import TestCase



class TestHelloWorld(TestCase):

    def test_hello_world(self):

        response = self.client.get('/hi/')



        self.assertEqual(response.status_code,200)



        self.asserrtEqual(response.content,'Hello World!')



    def test_hello_world(client):

        response = client.get('/hi/')



        assert response.status_code == 200

        assert response.content == 'Hello World!'
