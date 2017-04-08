from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from form import SendMailForm
from django.core.mail import send_mail


def contact(request):

    if request.method == "POST":
        send_form = SendMailForm(request.POST)
        confirm = []
        if send_form.is_valid():
            subject = "Contact"
            messages = send_form.cleaned_data['sender_text']
            from_email = settings.EMAIL_HOST_USER
            to_list = [send_form.cleaned_data['sender_email'],settings.EMAIL_HOST_USER]
            send_mail(subject,messages,from_email,to_list,fail_silently=True)
            confirm.append("Mesajul a fost trimis!")
            return render(request, 'contact/contact.html', context={'form': send_form,
                                                                    'messages': confirm})
        else:
            return render(request, 'contact/contact.html', context={'form': send_form})
    else:
        send_form = SendMailForm()
        return render(request, 'contact/contact.html', context={'form': send_form})