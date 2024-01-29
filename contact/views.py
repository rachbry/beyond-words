from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                'Contact Form Submission',
                f'Name: {your_name}\nEmail: {your_email}\n\nMessage:\n{message}',
                'from@example.com',  # Change to your email address
                ['to@example.com'],  # Change to the recipient's email address
            )

            # Redirect after successful submission
            return redirect('contact_success')  # Create a 'contact_success' URL pattern

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
