# Generated by Django 3.2.3 on 2021-06-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name_plural': 'pets'},
        ),
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to='pets_images'),
        ),
    ]