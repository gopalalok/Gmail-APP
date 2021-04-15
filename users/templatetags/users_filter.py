from django import template


register = template.Library()

@register.filter(name='no_of_email')
def no_of_email(number): 
    return (number-1)*2