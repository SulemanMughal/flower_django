# Generated by Django 3.1.4 on 2021-12-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
    ]
