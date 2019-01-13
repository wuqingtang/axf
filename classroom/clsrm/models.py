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

