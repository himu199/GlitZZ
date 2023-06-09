# Generated by Django 4.2.1 on 2023-05-31 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectioncarousel',
            name='media',
        ),
        migrations.RemoveField(
            model_name='productcarousel',
            name='media',
        ),
        migrations.RemoveField(
            model_name='promotioncarousel',
            name='media',
        ),
        migrations.AddField(
            model_name='collectioncarousel',
            name='large_file',
            field=models.FileField(default=None, upload_to='images/homepage/'),
        ),
        migrations.AddField(
            model_name='collectioncarousel',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='collectioncarousel',
            name='small_file',
            field=models.FileField(default=None, upload_to='images/homepage/'),
        ),
        migrations.AddField(
            model_name='productcarousel',
            name='large_file',
            field=models.FileField(default=None, upload_to='images/homepage/'),
        ),
        migrations.AddField(
            model_name='productcarousel',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='productcarousel',
            name='small_file',
            field=models.FileField(default=None, upload_to='images/homepage/'),
        ),
        migrations.AddField(
            model_name='promotioncarousel',
            name='large_file',
            field=models.FileField(default=None, upload_to='images/homepage/'),
        ),
        migrations.AddField(
            model_name='promotioncarousel',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='promotioncarousel',
            name='small_file',
            field=models.FileField(default=None, upload_to='images/homepage/'),
        ),
        migrations.AlterField(
            model_name='productcarousel',
            name='caption',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='promotioncarousel',
            name='caption',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
