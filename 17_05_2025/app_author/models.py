from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name= models.CharField(max_length=100)
    brith_date= models.DateField()
    books_count= models.IntegerField()
    biography= models.TextField()
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    slug= models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table= 'author'
        ordering= ['name']
        verbose_name= 'Author'
        verbose_name_plural= 'Authors'
        
