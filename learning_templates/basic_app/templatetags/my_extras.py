from django import template

register = template.Library()

# This is use decorate methods
@register.filter(name='cut')
def cut(value,arg):
    """
    
    This cut out all values of "arg" from the string!
    """

    return value.replace(arg,'')

register.filter('cut',cut)