from django import template
from decimal import Decimal

register = template.Library()

def valid_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)

@register.filter
def sub(value, arg):
    """Subtracts the arg from the value."""
    try:
        return valid_numeric(value) - valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''
sub.is_safe = False

@register.filter
def suma(value, arg):
    """Sum the arg from the value."""
    try:
        return valid_numeric(value) + valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
suma.is_safe = False

@register.filter
def cutstring(value, arg):
    string = str(value)
    cut_string = string.split(arg)
    new_string = cut_string[3]
    return new_string