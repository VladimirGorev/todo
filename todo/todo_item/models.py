from django.db import models
from main.models import ListModel

class ItemModel(models.Model):
    """
        Модель списка дел
    """
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    list_model = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expire_date = models.DateTimeField(blank=True)


    # def __str__(self):
    #     return self.name

class Meta:
    verbose_name = 'Основные пункты в деле'


