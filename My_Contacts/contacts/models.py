from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your models here.
class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    phone = models.IntegerField()
    info = models.CharField(max_length = 150)
    gender = models.CharField(max_length=50,
                                choices =( 
                                    ('male','Male'),
                                    ('female','Female')
                                ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
    
    
    
    