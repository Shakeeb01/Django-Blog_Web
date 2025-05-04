from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

    def __str__(self):
        return self.name
    
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    posted = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-posted']
        
    def __str__(self):
        return f'{self.title} is created at {self.posted} of category {self.category.name}'