# Generated by Django 3.2.16 on 2023-02-11 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_added_image_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('pub_date',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
