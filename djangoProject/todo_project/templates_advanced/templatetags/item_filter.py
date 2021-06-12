from django import template

register = template.Library()


@register.filter(name="odd ID")
def filter_odd_id(items):

    return [item for item in items if item % 2 == 1]
