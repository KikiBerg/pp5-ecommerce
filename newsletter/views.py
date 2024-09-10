from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have successfully subscribed to our newsletter!'
            )
            return redirect('home')
    else:
        form = NewsletterForm()

    return render(request, 'newsletter/signup.html', {'form': form})
