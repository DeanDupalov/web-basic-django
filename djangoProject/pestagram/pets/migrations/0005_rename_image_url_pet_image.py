# Generated by Django 3.2.3 on 2021-06-17 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image_url',
            new_name='image',
        ),
    ]
