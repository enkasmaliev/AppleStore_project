from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings


def create_activation_code(user):
    user.activation_code = get_random_string(10)
    user.save()


def send_activation_code(user):
    activation_url = f'http://localhost:8000/account/activation/{user.activation_code}'
    message = f"""
        Thank you for signing up.
        PLease, activate your account.
        Activation link: {activation_url}
    """
    send_mail(
        subject="Activate your account",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )

