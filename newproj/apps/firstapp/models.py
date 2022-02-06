from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    ACCOUNT_FULL_NAME_MAX_LENGTH = 40
    
    full_name = models.CharField(max_length = ACCOUNT_FULL_NAME_MAX_LENGTH)
    
    description = models.TextField()

    def __str__(self):
        return f'Аккаунт:{self.user.id}/{self.full_name}'

    class Meta:
        verbose_name_plural = 'Аккаунты'
        verbose_name = 'Аккаунт'
        ordering = (
            'full_name',
        )

class Group(models.Model):

    name = models.CharField(
        max_length=20
    )

    def __str__(self) -> str:
        return f'Группа {self.name}'

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = (
            'name',
        )


class Student(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )

    age = models.IntegerField(
        null=True,
        verbose_name = 'Возраст'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        verbose_name = 'Группа'
    )

    gpa = models.FloatField(
        verbose_name = 'Средняя оценка'
    )

    def __str__(self):
        return f'Студент {self.account.full_name}/Группа {self.group.name}'


    class Meta:
        verbose_name_plural = 'Студенты'
        verbose_name = 'Студент'
        ordering = (
            'account',
        )
