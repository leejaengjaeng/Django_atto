# -*- coding: UTF-8 -*-
from django import template
import application.common.customUserHandler as cuh

register = template.Library()

@register.simple_tag
def sub(var1, var2):
    if type(var1) != int:
        var1 = int(var1)
    if type(var2) != int:
        var2 = int(var2)
    return var1 - var2


@register.simple_tag
def setSession(request):
    cuh.setMenuToSession(request)
    return " "