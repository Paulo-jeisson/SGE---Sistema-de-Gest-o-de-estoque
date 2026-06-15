from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #auto complementa a data atmtc
    updated_at = models.DateTimeField(auto_now=True) #atualiza a data a cada auteração

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
