from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Task(models.Model):
  description = models.CharField(max_length=256)
  due_by = models.DateField(default=None, blank=True, null=True)

  def __str__(self):
    return self.description

