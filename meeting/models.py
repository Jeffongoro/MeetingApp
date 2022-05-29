from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    # User files will be stored in media folder.
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Meeting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meetings')
    id = models.AutoField(
        auto_created = True,
        primary_key = True,
        serialize = False,
        verbose_name ='id'
    )
    title = models.CharField(max_length=200)
    agenda = models.TextField()
    venue = models.CharField(max_length=200)
    guests = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    minutes = models.TextField(blank=True, null=True)
    attachments = models.FileField(upload_to=user_directory_path, blank=True, null=True)

    class Meta:
        db_table = 'meeting'
