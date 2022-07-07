import os
import smtplib
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, reverse
from django.views import generic
from cart.models import Order
from email.message import EmailMessage
from .forms import ContactForm

EMAIL_ADDRESS = os.environ.get('EMAIL_HOST_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     subject = 'Contact Form Message'
#     body = "Hello There Friend"

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(EMAIL_ADDRESS, 'delroybrown229@gmail.com', msg)


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We'll back to you ASAP!")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Received message below from {name}, Email: {email}
            ________________________
            
            {message}
            """
        send_mail(
            subject="Someone has messaged you via the Contact Form.",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )

        return super(ContactView, self).form_valid(form)
