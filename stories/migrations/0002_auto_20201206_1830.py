# Generated by Django 3.1.4 on 2020-12-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(max_length=110, verbose_name='Kategoriya'),
        ),
    ]
