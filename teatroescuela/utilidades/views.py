from django.core.mail import EmailMessage
from django.template.loader import get_template, render_to_string
from teatroescuela import settings

def enviar_mail(**kwargs):

    """
        html: boolean
        to_email:
        cc_email
        subject
        attach
        email_message
        data
    """

    status = True
    message = None

    try:

        html          = True if 'html' in kwargs else False
        to_email      = kwargs['to_email']
        cc_email      = kwargs['cc_email'] if 'cc_email' in kwargs else []
        subject       = kwargs['subject']
        attach        = kwargs['attach'] if 'attach' in kwargs else False
        email_message = kwargs['message'] if 'message' in kwargs else ''
        data          = kwargs['data'] if 'data' in kwargs else {}

        if html:
            email_message = get_template(email_message).render(data)

        email = EmailMessage(subject, email_message, settings.EMAIL_HOST_USER, to_email, cc=cc_email)

        if attach:
            email.attach_file(attach)

        if html:
            email.content_subtype = 'html'

        email.send()

    except Exception as error:
        print(error)
        status = False
        message = str(error)

    return {
        'status': status,
        'message': message
    }
