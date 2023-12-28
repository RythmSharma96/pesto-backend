from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = 'To Do', _('To Do')
        IN_PROGRESS = 'In Progress', _('In Progress')
        DONE = 'Done', _('Done')

    title = models.CharField(max_length=100, blank=False, default=None)
    description = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    isEditing = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} , {self.description} , {self.status}  , {self.isEditing}'
