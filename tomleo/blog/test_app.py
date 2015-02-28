import pytest
from django.core.urlresolvers import reverse

from . import views
from .factories import PostFactory

@pytest.mark.django_db
def test_post_detail_view(client):
    post = PostFactory.create()
    response = client.get(reverse('post-detail', kwargs={ 'pk': post.id+1 }))
    assert response.status_code == 404

    response = client.get(reverse('post-detail', kwargs={ 'pk': post.id }))
    assert response.status_code == 200

