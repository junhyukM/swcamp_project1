from django.db import models
# from django_resized import ResizedImageField
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    release = models.DateField()
    genre = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    showtime = models.TimeField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)
    imgfile = models.ImageField(upload_to="", blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    nickname = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text