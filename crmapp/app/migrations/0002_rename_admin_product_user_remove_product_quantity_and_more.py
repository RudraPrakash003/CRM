# Generated by Django 5.0.4 on 2024-04-08 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='admin',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]