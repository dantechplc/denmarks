from django.core.mail import EmailMultiAlternatives


class EmailSender:
    def inquiry(*args, **kwargs):
        subject = "New Request"
        to_email = "support@denmarkgov.com"
        email = kwargs.get('email', None)
        message = f"Hello Admin. \n Client with this email {email}, have submitted a request kindly check your dashboard. " \
                  f"\n Kindly verify their request.  "
        email = EmailMultiAlternatives(
            subject, message, to=[to_email]
        )
        email.send()