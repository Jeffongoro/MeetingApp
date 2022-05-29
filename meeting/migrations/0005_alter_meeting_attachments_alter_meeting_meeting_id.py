# Generated by Django 4.0.4 on 2022-05-26 00:06

from django.db import migrations, models
import meeting.models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_meeting_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to=meeting.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
