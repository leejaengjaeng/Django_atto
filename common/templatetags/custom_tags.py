# -*- coding: UTF-8 -*-
from django import template

register = template.Library()

@register.simple_tag
def sub(var1, var2):
    return var1 - var2