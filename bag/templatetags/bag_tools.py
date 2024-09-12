from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    print(f"Calculating subtotal: {price} * {quantity}")
    return price * quantity
