from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FAQ
from .forms import FAQForm
from products.models import Category


def faq_list(request):
    categories = Category.objects.all()
    return render(request, 'faqs/faq_list.html', {'categories': categories})


@login_required
def add_faq(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ added successfully.')
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faqs/faq_form.html', {'form': form})


@login_required
def edit_faq(request, faq_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, id=faq_id)
    original_faq = {
        'question': faq.question,
        'answer': faq.answer,
        'category': faq.category
    }

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
                return render(request, 'faqs/edit_faq_confirm.html', {
                    'form': form,
                    'original_faq': original_faq,
                    'updated_faq': form.cleaned_data
                })
    else:
        form = FAQForm(instance=faq)

    return render(request, 'faqs/faq_form.html', {'form': form, 'faq': faq})


@login_required
def delete_faq(request, faq_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, id=faq_id)

    if request.method == 'POST':
        if 'confirm' in request.POST:
            faq.delete()
            messages.success(request, 'FAQ deleted successfully.')
            return redirect('faq_list')
        else:
            return redirect('faq_list')

    return render(request, 'faqs/delete_faq_confirm.html', {'faq': faq})
