from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    published = models.DateTimeField()
    intro = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        ordering = ['published', 'title']

    def save(self, *args, **kwargs):
        if not self.id:
            self.published = timezone.now()
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.id, 'slug': self.slug})

