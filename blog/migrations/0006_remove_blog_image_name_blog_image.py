# Generated by Django 5.1 on 2024-10-10 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image_name',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='relevant_images', verbose_name='relevant image'),
        ),
    ]
