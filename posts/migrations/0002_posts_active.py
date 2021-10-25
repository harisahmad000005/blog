# Generated by Django 3.2.8 on 2021-10-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='active',
            field=models.CharField(choices=[('publish', 'Publish'), ('unpublish', 'Unpublish')], default='green', max_length=10),
        ),
    ]
