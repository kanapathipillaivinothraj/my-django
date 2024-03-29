from django.db import models

# Create your models here.
class detail_dataBase(models.Model):
    No = models.IntegerField()
    Name = models.CharField(max_length=25,null=False,blank=False)
    Address = models.TextField(max_length=255,null=False,blank=False)
    Image = models.ImageField(upload_to="media/image",null=True,blank=True)
    Links = models.URLField(null=False,blank=True)
    Salary = models.FloatField()

    def __str__(self):
        return self.Name