# Generated by Django 4.2.3 on 2024-03-21 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Writer',
        ),
    ]
