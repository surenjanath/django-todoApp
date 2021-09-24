from django.db import models

# To clear data from recent actions use :
# python manage.py shell
# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()

# Create your models here.
class TodoTask(models.Model):
    text        = models.CharField(max_length = 45)
    completed   = models.BooleanField(default = False)

    def __str__(self):
        return self.text
