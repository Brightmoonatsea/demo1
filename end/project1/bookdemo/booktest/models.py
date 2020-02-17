from django.db import models

# Create your models here.


# 每一张表就是一个模型类
# 有了ORM后我们就可以定义表对应的模型类
class Book(models.Model):
    """
    book 继承了Model类  因为Model拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")

    def __str__(self):
        return self.title


# class HeroManager(models.Manager):
#
#     def deletehero(self, heroid):
#         hero = self.get(id=heroid)
#         hero.delete()
#
#     def createhero(self, name, gender, content):
#         hero = self.model()
#         hero.name = name
#         hero.gender = gender
#         hero.content = content
#         hero.save()


class Hero(models.Model):
    """
    hero 类继承了Model类
    """

    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # object = HeroManager()

    def __str__(self):
        return self.name


class Account(models.Model):
    username = models.CharField(max_length=10, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    email = models.EmailField(default="1150242343@qq.com")
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="con")


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="标签名")
    articles = models.ManyToManyField(Article, related_name='tags')



# django orm关联查询
# 多方Hero   一方Book
# 1多找一， 多方对象.关系字段    exp: h1.book
# 2一找多， 一方对象.小写多方类名_set.all()   exp:  b1.hero_set.all()
