import factory
from faker import Factory as FakeFactory
from django.contrib.auth.models import User
from blog import models

faker = FakeFactory.create()

#TODO: move this out of blog app
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.email())


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    author = factory.SubFactory(UserFactory)
    title = factory.LazyAttribute(lambda x: faker.catch_phrase())
    intro = factory.LazyAttribute(lambda x: faker.sentence())
    content = factory.LazyAttribute(lambda x: faker.paragraph())

