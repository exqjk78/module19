from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30,verbose_name='Имя покупателя')
    balance = models.DecimalField(decimal_places=2,max_digits=9,default=0,verbose_name='Баланс')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100,default='Unnamed',verbose_name='Название игры')
    cost = models.DecimalField(decimal_places=2,max_digits=9,verbose_name='Стоимость')
    size = models.DecimalField(decimal_places=2,max_digits=9,verbose_name='Размер (мегабайты)')
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer,related_name='buyers')

    def __str__(self):
        return self.title
