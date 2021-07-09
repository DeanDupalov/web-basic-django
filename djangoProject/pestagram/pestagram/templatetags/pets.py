from django import template

from common.models import Comment
from pets.models import Pet

register = template.Library()


@register.simple_tag()
def comments_counter():
    return Comment.objects.count()


@register.inclusion_tag('templatetags/pets_count.html')
def pet_counter():
    return {
        'pets_count': Pet.objects.count(),
    }
