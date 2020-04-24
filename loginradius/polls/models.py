from django.db import models

# Create your models here.


class Contestant(models.Model):
    contestant_name = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+'_'+str(self.contestant_name)
