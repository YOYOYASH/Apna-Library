# Generated by Django 4.2.3 on 2023-07-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='cover_image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]