from django.db import models

# Create your models here.


# 每一张表就是一个模型类
# 有了ORM后我们就可以定义表对应的模型类
class Book(models.Model):
    """
    book 继承了Model类  因为Model拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")


class Hero(models.Model):
    """
    hero 类继承了Model类
    """

    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
