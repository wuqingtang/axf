from django.db import models


#父类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True


#轮播图,继承，
class Wheel(Base):

    #给表重命名
    class Meta:
        db_table = 'axf_wheel'


#导航图，继承
class Nav(Base):
    #给表重命名
    class Meta:
        db_table = 'axf_nav'

#一定买轮播图
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

#商品部分
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

"""
insert into axf_mainshow(
trackid,name,img,categoryid,brandname,
img1,childcid1,productid1,longname1,
price1,marketprice1,img2,childcid2,
productid2,longname2,price2,marketprice2,
img3,childcid3,productid3,longname3,price3,marketprice3)
"""

#商品主体
class MainShop(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'



