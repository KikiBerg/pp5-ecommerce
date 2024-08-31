from django.shortcuts import render
from products.models import Category


def faq_list(request):
    categories = Category.objects.all()
    return render(request, 'faqs/faq_list.html', {'categories': categories})
