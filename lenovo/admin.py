# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Poll

from .models import Choice

admin.site.register(Poll)

admin.site.register(Choice)

# Register your models here.
