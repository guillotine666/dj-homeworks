# Generated by Django 2.2.5 on 2019-11-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(upload_to='products/%Y/%m/%d/'),
        ),
    ]
