from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    imageUrl=models.CharField(max_length=200)

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "imageUrl": self.imageUrl
        }
    
    def __str__(self):
        return self.name


class Dish(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    imageUrl=models.CharField(max_length=200)
    is_gloten_free=models.BooleanField(default=False)
    is_vegetarian=models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "price": self.price,
            "description": self.description,
            "imageUrl": self.imageUrl,
            "is_gloten_free": self.is_gloten_free,
            "is_vegetarian":self.is_vegetarian,
            "category":self.category.id
        }

    def __str__(self):
        return self.name
