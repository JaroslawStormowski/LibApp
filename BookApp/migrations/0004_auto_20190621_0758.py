# Generated by Django 2.2.2 on 2019-06-21 05:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0003_auto_20190618_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='id_uuid',
            field=models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]