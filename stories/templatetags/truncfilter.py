from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter(name='get_date')
@stringfilter
def trunc_str(str_value):

    firts10 = str_value[0:10]
    
    return f'{firts10}...'


str_word = 'Tech Academy is coding bootcamp'

# print(trunc_str(str_word))