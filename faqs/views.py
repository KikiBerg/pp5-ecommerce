from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import FAQ
from .forms import FAQForm
from products.models import Category


def faq_list(request):
    categories = Category.objects.all()
    return render(request, 'faqs/faq_list.html', {'categories': categories})

@user_passes_test(lambda u: u.is_superuser)
def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ added successfully.')
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faqs/faq_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ updated successfully.')
            return redirect('faq_list')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faqs/faq_form.html', {'form': form, 'faq': faq})