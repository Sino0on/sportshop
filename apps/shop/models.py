from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=123, verbose_name=_('Название'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    code = models.CharField(max_length=123, unique=True)
    price = models.DecimalField(max_length=123, decimal_places=2, max_digits=10)
    brand = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_preview_image(self):
        images = self.images.all()
        if images.exists():
            return images[0]
        return None


    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
        ordering = ['-created_at']


class ProductImage(models.Model):
    image = models.ImageField(upload_to='imgs/product/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    star = models.PositiveIntegerField()
    content = models.CharField(max_length=244)
    image = models.ImageField(upload_to='reviews/')