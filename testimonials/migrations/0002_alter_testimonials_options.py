# Generated by Django 3.2.16 on 2023-01-26 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonials',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Testimonials'},
        ),
    ]
