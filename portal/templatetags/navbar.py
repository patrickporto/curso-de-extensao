from django.core.urlresolvers import reverse
from django import template

register = template.Library()

@register.simple_tag
def item(request, name, *args):
	current_url = request.path
	if request.path == '/':
		current_url = reverse('home')
	info = {
		'class': '',
		'link': reverse(name, args=args),
		'name': name.capitalize(),
	}

	if current_url == info['link']:
		info['class'] = 'active'
	output = "<li class=\"{class}\"><a href=\"{link}\">{name}</a></li>".format(**info)
	return output