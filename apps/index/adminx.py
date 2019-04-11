#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 11:34
# @Author  : 徐纪茂
# @File    : adminx.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
import xadmin
from .models import *

class UserXadmin(object):

    list_display = ['name', 'create_time', 'update_time', 'img', 'sex']


xadmin.site.register(User, UserXadmin)