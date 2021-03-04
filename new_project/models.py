from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title     

class Image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to ='photos')
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    added_date=models.DateTimeField(auto_now=True,null=False)
    
    def __str__(self):
        return self.title    