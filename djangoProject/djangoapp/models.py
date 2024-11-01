from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
#
#
#

# class Category(models.Model):
# name = models.CharField(max_length=255,verbose_name='Название категории')
# def __str__(self):
#     return self.name
#
# class Meta:
#     verbose_name='Категория'
#     verbose_name_plural='Катерии'
#
# class News(models.Model):
#     title=models.CharField(max_length=255,verbose_name="Заголовок")
#     content=models.TextField(verbose_name='Содержание')
#     created_at=models.DateTimeField(auto_now=True,verbose_name='Дата создания')
#     update_at=models.DateTimeField(auto_now=True,verbose_name='Дата обновления')
#     is_published=models.BooleanField(default=True,verbose_name="Опубликовано")
#     category=models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name='Категория')
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name="Новость"
#         verbose_name_plural='Новости'
#         ordering =['-created_at']

#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Book(models.Model):
#     GENRE_CHOICES = [
#         ('FIC', 'Fictions'),
#         ('NON', 'Non_Fiction'),
#         ('SCI', 'Science Fiction'),
#         ('FAN', 'Fantasy'),
#         ('MYS', 'Mystery'),
#         ('THR', 'Thriller'),
#         ('ROM', 'Romance'),
#         ('HIS', 'Historical'),
#     ]
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     publication_date = models.DateField()
#     genre = models.CharField(
#         max_length=3,
#         choices=GENRE_CHOICES,
#         default='FIC',
#     )
#
#     def __str__(self):
#         return self.title
