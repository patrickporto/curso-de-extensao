from django import template

register = template.Library()

@register.filter
def breadcrumb(request):
    splitted = str(request.path).split('/')
    return [item.replace('_', ' ').capitalize() for item in splitted if item]

