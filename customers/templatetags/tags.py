from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern):
    import re
    request = context['request'];
    if re.search(pattern, request.path):
        return ' class="active"'
    return ''