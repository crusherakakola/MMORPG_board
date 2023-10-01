import os
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@receiver(m2m_changed, sender=Post.postCategory.through)
def notify_about_new_post(sender, instance, **kwargs):

    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        for category in categories:
            subscribers = category.subscribers.all()
       # subscribers = instance.category.values('subscribers__email', 'subscribers__username')

            # Отправляем письмо каждому подписчику
            for subscriber in subscribers:
                html_content = render_to_string(
                    'subscribe_mail.html',
                    {
                        'category': category,
                        'title': instance.title,
                        'text': instance.text

                    }
                )
                msg = EmailMultiAlternatives(
                    subject={category},
                    body='',
                    from_email=os.getenv('FULL_MAIL'),
                    to=[subscriber.email],
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()