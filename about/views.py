from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import ContactForm
from newsletter.forms import NewsletterForm


def about_view(request):
    about_content = About.objects.first()
    contact_form = ContactForm()
    newsletter_form = NewsletterForm()

    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Your message has been sent!')
                return redirect('about:about')

        elif 'newsletter_submit' in request.POST:
            newsletter_form = NewsletterForm(request.POST)
            if newsletter_form.is_valid():
                newsletter_form.save()
                messages.success(request, 'You have successfully subscribed to our newsletter!')
                return redirect('about:about')

    return render(request, 'about/about.html', {
        'about_content': about_content,
        'contact_form': contact_form,
        'newsletter_form': newsletter_form,
    })
