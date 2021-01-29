# Generated by Django 3.1.4 on 2020-12-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Name: ')),
                ('last_name', models.CharField(max_length=40, verbose_name='Surname: ')),
                ('username', models.CharField(max_length=50, verbose_name='Username: ')),
                ('email', models.EmailField(max_length=254, verbose_name='Email: ')),
                ('password', models.CharField(max_length=50)),
                ('gender', models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female')], verbose_name='Gender: ')),
                ('address', models.CharField(max_length=1024, verbose_name='Address: ')),
                ('biography', models.TextField(verbose_name='Biograpyhy')),
                ('image', models.ImageField(upload_to='media/users_images', verbose_name='Image: ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('image', models.ImageField(upload_to='media/categories_images', verbose_name='Image Category: ')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('-created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Basliq')),
                ('slug', models.SlugField(max_length=110, verbose_name='Slug')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Dessert'), (2, 'Drink'), (3, 'Isti yemek'), (4, 'Sulu yemek')], verbose_name='Kategoriya')),
                ('short_description', models.CharField(max_length=255, verbose_name='Qisa Mezmun')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mezmun')),
                ('image', models.ImageField(upload_to='media/recipe_images', verbose_name='Sekil')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='stories.author')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipe',
                'db_table': 'recipe',
                'ordering': ('-created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('-created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Basliq')),
                ('slug', models.SlugField(max_length=110, verbose_name='Slug')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Dessert'), (2, 'Drink'), (3, 'Isti yemek'), (4, 'Sulu yemek')], verbose_name='Kategoriya')),
                ('short_description', models.CharField(max_length=255, verbose_name='Qisa Mezmun')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mezmun')),
                ('image', models.ImageField(upload_to='media/recipe_images', verbose_name='Sekil')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='stories.author')),
                ('tags', models.ManyToManyField(related_name='stories', to='stories.Tag')),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
                'db_table': 'story',
                'ordering': ('-created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='RecipeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stories.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stories.author')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='stories.Tag'),
        ),
    ]