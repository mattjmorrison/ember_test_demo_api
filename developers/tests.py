import simplejson as json
from django.test import TestCase
from developers.models import Developer


class DeveloperTests(TestCase):

    def test_gets_developers(self):
        Developer.objects.create(first_name='Matt', last_name='Morrison')
        response = self.client.get('/developers/')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.content)['data'][0]
        self.assertEqual('Developer', data['type'])
        self.assertEqual('Matt', data['attributes']['first_name'])
        self.assertEqual('Morrison', data['attributes']['last_name'])

    def test_creates_developer(self):
        response = self.client.post('/developers/', json.dumps({
            'data': {
                'type': 'Developer',
                'attributes': {
                    'first_name': 'Matt',
                    'last_name': 'Morrison',
                }
            }
        }), 'application/vnd.api+json')
        self.assertEqual(201, response.status_code)
        dev = Developer.objects.get()
        self.assertEqual('Matt', dev.first_name)
        self.assertEqual('Morrison', dev.last_name)

    def test_updates_developer(self):
        dev = Developer.objects.create(first_name='Matt', last_name='Morrison')
        response = self.client.patch('/developers/{}/'.format(dev.pk), json.dumps({
            'data': {
                'id': dev.pk,
                'type': 'Developer',
                'attributes': {
                    'first_name': 'Matthew',
                }
            }
        }), 'application/vnd.api+json')
        self.assertEqual(200, response.status_code, response.content)
        dev2 = Developer.objects.get()
        self.assertEqual('Matthew', dev2.first_name)

    def test_deletes_developer(self):
        dev = Developer.objects.create(first_name='Matt', last_name='Morrison')
        response = self.client.delete('/developers/{}/'.format(dev.pk))
        self.assertEqual(204, response.status_code)
        self.assertEqual(0, Developer.objects.count())
