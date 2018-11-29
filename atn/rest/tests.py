from hypothesis import given
from hypothesis.extra.django import TestCase
from hypothesis.strategies import text, characters
from rest_framework.test import APIClient

# define the range of name strings that hypothesis will present. Ensure that none start or end with <space>
# and that none is zero length.  This is used in @given()
# from: https://hypothesis.works/articles/generating-the-right-data/
names = text(characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')), min_size=1).map(
    lambda x: x.strip()).filter(lambda s: len(s) > 0)
addresses = text(characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')), min_size=1).map(
    lambda x: x.strip()).filter(lambda s: len(s) > 0)


class BasicApiTests(TestCase):

    @given(names, addresses)
    def test_create_client_and_retrieve(self, client_name, client_address):
        client = APIClient()

        # create the first Client
        params = {'name': client_name, 'address': client_address}
        response = client.post('/rest/clients/', params, format='json')
        assert response.status_code == 201

        # retrieve it
        response = client.get('/rest/clients/1/', format='json')
        assert response.status_code == 200

        # check it's the same as the original parameters.
        # (we did not put the url into params, but it is returned, so add it before the comparison).
        params['url'] = 'http://testserver/rest/clients/1/'
        assert response.data == params
