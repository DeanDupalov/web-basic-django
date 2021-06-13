from django import template

register = template.Library()

""" добавяме html клас с inclusive tag """


@register.inclusion_tag('templates_advanced/tags/bootstrap_form.html')
def bootstrap_form(form, action, method):
    """Тук можем да изпъняваме всякаква логика"""
    for (_, field) in form.fields.items():
        if 'class' not in field.widget.attrs:
            field.widget.attrs['class'] = ''

        field.widget.attrs['class'] += 'form-control'
        """Връщаме контекста"""
        return {
            'form': form,
            'action': action,
            'method': method,
        }
