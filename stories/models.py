from django.db import models

# Create your models here.


class Author(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField('Name: ', max_length=30)
    last_name = models.CharField('Surname: ', max_length=40)
    username = models.CharField(("Username: "), max_length=50)
    email = models.EmailField("Email: ", max_length=254)
    password = models.CharField(max_length=50)
    gender = models.PositiveIntegerField(("Gender: "), choices=CATEGORY_CHOICES)
    address = models.CharField("Address: ", max_length=1024)
    biography = models.TextField(("Biograpyhy"))
    image = models.ImageField("Image: ", upload_to='media/users_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        verbose_name = ('User')
        verbose_name_plural = ('Users')
    def __str__(self):
        return self.first_name


class Tag(models.Model):
    title = models.CharField('Title', max_length=100, db_index=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField("Image Category: ", upload_to='media/categories_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """
    Bu Model reseptler ucun meselen Alma piroqu, ...
    """
    # CATEGORY_CHOICES = (
    #     (1, 'Dessert'),
    #     (2, 'Drink'),
    #     (3, 'Isti yemek'),
    #     (4, 'Sulu yemek'),
    # )

    # relations
    tags = models.ManyToManyField(Tag, related_name='recipes')
    owner = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes')
    
    # informations
    title = models.CharField('Basliq', max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=110)
    # category = models.CharField('Kategoriya', max_length=110)
    # category = models.PositiveSmallIntegerField('Kategoriya', choices=CATEGORY_CHOICES)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    description = models.TextField('Mezmun', null=True, blank=True)
    image = models.ImageField('Sekil', upload_to='media/recipe_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recipe'
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipe'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class Story(models.Model):
    """
    Bu Model story-ler ucun nezerde urulubt ...
    """
    CATEGORY_CHOICES = (
        (1, 'Dessert'),
        (2, 'Drink'),
        (3, 'Isti yemek'),
        (4, 'Sulu yemek'),
    )

    # relations
    tags = models.ManyToManyField(Tag, related_name='stories')
    owner = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='stories')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='stories')
    
    # informations
    title = models.CharField('Basliq', max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=110)
    # category = models.PositiveSmallIntegerField('Kategoriya', choices=CATEGORY_CHOICES)
    # category = models.PositiveSmallIntegerField('Kategoriya', choices=CATEGORY_CHOICES)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    description = models.TextField('Mezmun', null=True, blank=True)
    image = models.ImageField('Sekil', upload_to='media/story_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'story'
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class RecipeComment(models.Model):
    # relations
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')

    # informations
    text = models.TextField('Text')

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=50)
    subject = models.CharField('Subject', max_length=100)
    content = models.TextField('Message')

    # moderations
    status = models.BooleanField('status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_message'
        verbose_name = 'Contact_Message'
        verbose_name_plural = 'Contact_Messages'
        ordering = ('-created_at',)

    def __str__(self):
        return self.subject