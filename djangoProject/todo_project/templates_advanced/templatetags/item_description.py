from django import template

register = template.Library()

@register.simple_tag()
def items_description(item):
    return f'<p>{item.description}</p>'