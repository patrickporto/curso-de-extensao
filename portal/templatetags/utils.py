from django import template

register = template.Library()

@register.filter
def split(value, token):
	splitted = str(value).split(token)
	return [item for item in splitted if item]