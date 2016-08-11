from django.db import models
from django.core.urlresolvers import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=1, null=False)
    date_of_birth = models.DateField(null=True)
    ULN = models.CharField(max_length=10, null=True)

    def get_absolute_url(self):
        return reverse('student:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



