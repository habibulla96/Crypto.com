from django.core.mail import send_mail


def send_activation_mail(email, activation_code):
    subject = 'Активация Аккаунта'
    message = f'Чтобы активировать ваш аккаунт перейдите по ссылке: http://localhost:8000/v1/api/account/activate/{activation_code}/'
    from_ = 'test@test.com'
    emails = [email, ]

    send_mail(subject, message, from_, emails, fail_silently=True)






# def send_activation_code(email, activation_code):
#     activation_url = f'http://localhost:8000/v1/api/account/activate/{activation_code}/'
#     message = f'Thank you for signing up.\nPlease activate your account.\nActivation link: {activation_url}'
#     send_mail(
#         'Activate your account',
#         message,
#         'test@test.com',
#         [email, ],
#         fail_silently=False
#     )
