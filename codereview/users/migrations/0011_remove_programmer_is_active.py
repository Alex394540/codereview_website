# Generated by Django 2.2.4 on 2019-09-07 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_programmer_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmer',
            name='is_active',
        ),
    ]