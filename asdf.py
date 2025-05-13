from sms import send_sms

send_sms(
    'Here is the message',
    '+12065550100',
    ['+441134960000'],
    fail_silently=False
)