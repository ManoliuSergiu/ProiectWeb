# Generated by Django 2.2.7 on 2019-12-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191128_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='uploads/default.jpg', upload_to='images/'),
        ),
    ]
