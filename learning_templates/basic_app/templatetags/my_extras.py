from django import templates

register = template.Library()

## METHOD 1: WITHOUT DECORATORS
# # define a function that will be used as a filter
# def cut(value, arg):
#     """
#     This cuts out all values of "arg" from string!
#     """
#     return value.replace(arg, "")
#
# # Register the filter:
# # 1st parameter is the filter name,
# # 2nd param is the function that implements the filter
# register.filter('cut', cut)

# METHOD 2: WITH DECORATORS
# define a function that will be used as a filter
# and wrap it in a decorator register.filter

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from string!
    """
    return value.replace(arg, "")
