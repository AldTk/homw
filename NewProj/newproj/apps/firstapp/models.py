from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=40,db_index=True,verbose_name='Категория')
#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = 'Категория'
#         verbose_name = 'Категория'
#         ordering = ['name']


# class Medicine(models.Model):
#     title = models.CharField(max_length=30,verbose_name='Лекарство')
#     description = models.TextField(null=True,blank=True,verbose_name='Описание')
#     price = models.FloatField(null=False,blank=False,verbose_name='Цена')
#     count = models.FloatField(null=True,blank=True,verbose_name='Количество')
#     category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.PROTECT,verbose_name='Категория')
#     class Meta:
#         verbose_name_plural = 'Лекарства'
#         verbose_name = 'Лекарства'
#         ordering = ['-price']
