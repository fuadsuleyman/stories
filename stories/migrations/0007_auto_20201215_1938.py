# Generated by Django 3.1.4 on 2020-12-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Subject'),
        ),
    ]
