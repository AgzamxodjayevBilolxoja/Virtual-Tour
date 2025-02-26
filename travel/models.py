from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.FloatField()
    language = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='blogs')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):  
        return self.title


class CityImages(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='city_images/')