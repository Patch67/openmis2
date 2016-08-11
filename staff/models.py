from django.db import models
from django_markdown.models import MarkdownField


class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    biography = models.TextField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def test(self):
        return self
