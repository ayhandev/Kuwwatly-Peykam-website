from django.shortcuts import render, redirect
import smtplib
import ssl
from .forms import ClientForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from .models import Gallery, Photo
from decouple import config

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()

            try:
                ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE

                with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp_server:
                    smtp_server.starttls(context=ssl_context)
                    smtp_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

                    msg = MIMEMultipart()
                    msg['From'] = settings.EMAIL_HOST_USER
                    msg['To'] = config('EMAIL_HOST_USER')
                    msg['Subject'] = 'Новое предложение!'

                    body = f'Предложение от: {client.name}\n' \
                            f'Телефон: {client.phone}\n' \
                            f'Email: {client.email}\n' \
                            f'Сообщение: {client.message}\n' \
                            
                    msg.attach(MIMEText(body, 'plain'))

                    smtp_server.send_message(msg)
                    
            except Exception as e:
                print(f"Ошибка при отправке email: {e}")

            return redirect('home')
    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})


from django.utils.translation import gettext as _
from django.shortcuts import render
from .models import Gallery

def gallery(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery.html', {'galleries': galleries})