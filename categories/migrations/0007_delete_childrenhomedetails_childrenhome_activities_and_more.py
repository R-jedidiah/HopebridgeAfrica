# Generated by Django 4.1.7 on 2023-03-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_remove_childrenhomedetails_childrenhome_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildrenHomeDetails',
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='activities',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='age_group',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='image',
            field=models.ImageField(default=2, upload_to='categories_media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='main_challenges',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childrenhome',
            name='num_children',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]