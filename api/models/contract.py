from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Contract(models.Model):

  class JobType(models.TextChoices):
    UI = 'UI', _('UI')
    UX = 'UX', _('UX')
    FRONTEND = 'FE', _('Front End')
    BACKEND = 'BE', _('Back End')
    FULLSTACK = 'FS', _('Full Stack')
    REFACTOR = 'RE', _('Refactor')

  
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  deadline = models.DateTimeField(auto_now=False)
  jobtype = models.CharField(max_length=2, choices=JobType.choices, default=None)
  tags = models.CharField(max_length=100)
  price = models.CharField(max_length=8)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return self.title

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'deadline': self.deadline,
        'Job Type': self.jobtype,
        'price': self.price,
        'tags': self.tags,
        'owner': self.owner,
    }
