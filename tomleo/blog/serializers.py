from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('author', 'title', 'slug', 'published', 'intro', 'content')

    def save(self, *args, **kwargs):
        #TODO: custom logic to parse rst files
        super(Post, self).save(*args, **kwargs)

