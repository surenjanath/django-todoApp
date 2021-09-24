from django.db import models

# To clear data from recent actions use :
# python manage.py shell
# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()


# If error such as no table found use the following sets
'''
1. delete db.sqlite3
2. delete migration

3. Create and run the migrations:

python manage.py makemigrations
python manage.py migrate

4. Sync the database:
manage.py migrate --run-syncdb

'''


# Create your models here.
class TodoTask(models.Model):
    text        = models.CharField(max_length = 45)
    completed   = models.BooleanField(default = False)

    def __str__(self):
        return self.text
