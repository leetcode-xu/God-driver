from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    email = models.EmailField(verbose_name='电子邮箱')
    phone = models.CharField(max_length=11, verbose_name='手机')
    sex = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    img = models.ImageField(null=True, blank=True, upload_to='touxiang')

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'User'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


