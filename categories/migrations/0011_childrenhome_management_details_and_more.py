# Generated by Django 4.1.7 on 2023-04-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_childrenhome_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='childrenhome',
            name='management_details',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='management_image',
            field=models.ImageField(default=2, upload_to='childrenhomes_media'),
            preserve_default=False,
        ),
    ]