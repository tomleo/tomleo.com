from django.test import TestCase
from django.core.urlresolvers import reverse

from . import views
from blog.factories import PostFactory

class TestFactories(TestCase):
    
    def test_user_factory(self):
        pass

    def test_post_factory(self):
        pass

class TestViews(TestCase):

    def test_post_detail_view_json(self):
        post = PostFactory.create()
        response = self.client.get(reverse('post', kwargs={
            'pk': 1,
            'slug': 'test'
        }))
        self.assertEqual(response.status_code, 200)

