from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    # source argument controls which attribute is used to populate a field, and
    # can point at any attribute on the serialized instance. It can also take
    # the dotted notation shown above, in which case it will traverse the given
    # attributes, in a similar way as it is used with Django's template
    # language

    class Meta:
        model = Post
        fields = ('author', 'title', 'slug', 'published', 'intro', 'content')

    def save(self, *args, **kwargs):
        #TODO: custom logic to parse rst files
        super(Post, self).save(*args, **kwargs)

class ReStructuredTextSerializer(serializers.ModelSerializer):

    rst_file = serializers.FileField()

    class Meta:
        model = Post
        fields = ('author', 'title', 'intro', 'content')

