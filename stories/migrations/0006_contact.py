# Generated by Django 3.1.4 on 2020-12-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20201207_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('subject', models.CharField(max_length=100, verbose_name='Name')),
                ('content', models.TextField(verbose_name='Mezmun')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact_Message',
                'verbose_name_plural': 'Contact_Messages',
                'db_table': 'contact_message',
                'ordering': ('-created_at',),
            },
        ),
    ]
