from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    MEMORY_CHOICES = (
        ('64 GB', '64 gb'),
        ('128 GB', '128 gb'),
        ('256 GB', '256 gb'),
        ('512 GB', '512 gb'),
        ('1 TB', '1 tb'),
    )
    COLOR_CHOICES = (
        ('BLACK', 'black'),
        ('GOLD', 'gold'),
        ('SILVER', 'silver'),
    )
    STATUS_CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии'),
    )

    categories = models.ManyToManyField(Category, related_name='items')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    memory = models.CharField(max_length=6, choices=MEMORY_CHOICES)
    image = models.ImageField(upload_to='items', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='out of stock')


    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукции'
        ordering = ['price']

    def __str__(self) -> str:
        return self.name