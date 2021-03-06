# Generated by Django 2.2.2 on 2019-06-13 17:02

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('publishedDate', models.DateField(verbose_name='date published')),
                ('industryIdentifiers', jsonfield.fields.JSONField(default=dict)),
                ('pageCount', models.IntegerField()),
                ('imageLinks', models.CharField(max_length=300)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
    ]
