# Generated by Django 3.2.5 on 2021-07-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commlion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionpost',
            name='session_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]
