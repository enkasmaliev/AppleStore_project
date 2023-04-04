from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
    
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

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    memory = models.CharField(max_length=6, choices=MEMORY_CHOICES)
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='articles', null=True, blank=True)