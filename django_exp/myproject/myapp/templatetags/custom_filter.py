from django import template

register = template.Library()

@register.filter
def reverse_list(value):
    try:
        return value[::-1]
    except TypeError:
        return value