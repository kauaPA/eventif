from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from contact.forms import ContactForm


def inicio(request):
    if request.method == 'POST':
       return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contacts/contact_form.html', {'form': form})
 

    _send_mail(
        'contacts/contact_email.txt',
        form.cleaned_data, 
        'Feito!',
        settings.DEFAULT_FROM_EMAIL,
        form.cleaned_data['email']


    )


    messages.success(request, 'Adicionado com sucesso!')
    return HttpResponseRedirect('/contact/')


def new(request):
    return render(request, 'contacts/contact_form.html', {'form': ContactForm()})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])
