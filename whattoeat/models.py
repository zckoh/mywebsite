from django.db import models
from django.utils import timezone

# class CookingDish(models.Model):
#     name = models.CharField(max_length=200)

#     #ingredients

# class ComplexityChoice(models.Model):
#     cookingdish = models.ForeignKey(CookingDish, on_delete=models.CASCADE)
#     complexity = models.CharField(max_length=200)

#     def __str__(self):
#         return self.complexity

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    no_of_visits = models.IntegerField(default=0)
    date_added = models.DateTimeField('Date Added',auto_now_add=True)

    def __str__(self):
        return self.name