# Generated by Django 2.2.3 on 2019-07-30 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20190717_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bucket',
            old_name='access_key',
            new_name='access_key_id',
        ),
    ]