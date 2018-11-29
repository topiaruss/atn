from django.test import TestCase
from rest_framework.test import APIClient


class BasicApiTests(TestCase):

    def test_create_client_and_retrieve(self):
        client = APIClient()

        # create the first Client
        params = {'name': 'first client', 'address': 'first street'}
        response = client.post('/rest/clients/', params, format='json')
        assert response.status_code == 201

        # retrieve it
        response = client.get('/rest/clients/1/', format='json')
        assert response.status_code == 200

        # check it's the same as the original parameters.
        # (we did not put the url into params, but it comes back, so add it before the comparison).
        params['url'] = 'http://testserver/rest/clients/1/'
        assert response.data == params



