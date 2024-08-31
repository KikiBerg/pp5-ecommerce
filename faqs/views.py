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
        if 'confirm' in request.POST:
            form = FAQForm(request.POST, instance=faq)
            if form.is_valid():
                form.save()
                messages.success(request, 'FAQ updated successfully.')
                return redirect('faq_list')
        elif 'cancel' in request.POST:
            return redirect('faq_list')
        else:
            # This is the initial POST with the edited data
            form = FAQForm(request.POST, instance=faq)
            if form.is_valid():
                return render(request, 'faqs/edit_faq_confirm.html', {'form': form, 'faq': faq})
    else:
        form = FAQForm(instance=faq)

    return render(request, 'faqs/faq_form.html', {'form': form, 'faq': faq})

@user_passes_test(lambda u: u.is_superuser)
def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            faq.delete()
            messages.success(request, 'FAQ deleted successfully.')
            return redirect('faq_list')
        else:
            return redirect('faq_list')

    return render(request, 'faqs/delete_faq_confirm.html', {'faq': faq})