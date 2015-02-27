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
    #TODO: add file field for Plain text files (support for RST, Markdown, and Latex)
    # 1. rst files will be read, meta data will be parsed to populate other Post fields
    # 2. rst file will be updated to include meta data on the Post object in the database
    #
    # This will allow for plain text ReStructuredText representations of Post objects.
    # Maintaining RST files (potentially version controlled) will allow other
    # colaberators to submit edits to blog posts via Github.
    #
    # TODO: figure out how images and files embended inside RST files should be
    # stored in the database (base64 encode them?)
    class Meta:
        ordering = ['published', 'title']

    def save(self, *args, **kwargs):
        if not self.id:
            self.published = timezone.now()
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.id, 'slug': self.slug})

