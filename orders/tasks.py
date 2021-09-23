from celery import task
from django.core.mail import send_mail
from .models import Order
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


@task
def order_created(order_id):
    # order = Order.objects.get(id=order_id)
    # subject = f'Order nr. {order.id}'
    # to = order.email
    # message = render_to_string('', {
    #     'user': order.first_name,
    #     'order_id': order.id,
    #
    # })
    # welcome_email = EmailMessage(
    #     subject=subject,
    #     body=message,
    #     from_email='message.me.aamy@gmail.com',  # change from email here
    #     to=[to],  # to email list here
    #
    # )
    # welcome_email.content_subtype = "html"
    # welcome_email.send()
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'sendto.test.email@gmail.com',
                          [order.email])
    return mail_sent
