from django.db import models


# Create your models here.
class FileModel(models.Model):
    name = models.CharField(max_length=50) # 标签
    myText = models.TextField(max_length=10000,default='请在这里输入相关信息') # 解释信息
    myFile = models.FileField(upload_to='../media/') # 文件

    def __str__(self):
        return self.name

class TextModel(models.Model):
    name = models.CharField(max_length=50) # 标签
    myText = models.TextField(max_length=10000,default='请在这里输入相关信息') # 解释信息

    def __str__(self):
        return self.name