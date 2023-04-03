# Generated by Django 4.1.7 on 2023-04-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0008_alter_donor_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childrenhome',
            name='image',
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='image1',
            field=models.ImageField(default=11, upload_to='childrenhomes_media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='image2',
            field=models.ImageField(default=1, upload_to='childrenhomes_media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='image3',
            field=models.ImageField(default=2, upload_to='childrenhomes_media'),
            preserve_default=False,
        ),
    ]
