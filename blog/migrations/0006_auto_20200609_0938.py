# Generated by Django 3.0.7 on 2020-06-09 09:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200609_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
    ]
