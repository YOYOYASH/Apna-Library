# Generated by Django 4.2.3 on 2023-07-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Roll_No',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]