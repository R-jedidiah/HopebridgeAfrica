# Generated by Django 4.1.7 on 2023-04-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_delete_childrenhomedetails_childrenhome_activities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(default=1, max_length=155),
            preserve_default=False,
        ),
    ]