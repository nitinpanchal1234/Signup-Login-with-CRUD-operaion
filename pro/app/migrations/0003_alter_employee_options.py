# Generated by Django 4.2.2 on 2023-08-22 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id']},
        ),
    ]