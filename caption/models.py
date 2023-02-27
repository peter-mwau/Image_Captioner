from django.db import models

# Create your models here.

  
class UploadImage(models.Model):   
    image = models.ImageField(upload_to='images/') 
    caption = models.CharField(max_length=200, blank=True)  
  
    def __str__(self):  
        return self.caption  
    

# class SaveData(models.Model):
#     Image = models.ImageField(upload_to='images/')
#     Caption = models.CharField(max_length=200, blank=True)
#     Time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.caption

    

