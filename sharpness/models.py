from django.db import models

# Create your models here.
from car.models import Car


class Sharpness(models.Model):

    create_time = models.DateTimeField(verbose_name='时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='汽车品牌')
    speed = models.CharField(verbose_name='速度形式', max_length=50)
    condition = models.CharField(verbose_name='工况', max_length=100)
    status = models.CharField(verbose_name='荷载状态', max_length=100)
    left = models.FloatField(verbose_name='尖锐度左耳-acum')
    right = models.FloatField(verbose_name='尖锐度右耳-acum')
    image = models.FileField(upload_to='upload_image', default=" ")

    class Meta:
        verbose_name = '尖锐度数据'
        db_table = 'sharpness'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '左耳: %s |  右耳: %s' % (self.left, self.right)