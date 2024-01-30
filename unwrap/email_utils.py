# email_utils.py
from flask_mail import Message
from . import mail

def send_order_confirmation_email(user_email, order_details, phone_number, address, oil_type, quantity):
    subject = 'Order Confirmation - Azhiyaar Oil'
    recipients = [user_email]
    body = f"User Email: {user_email}\n\nOrder Details:\n{order_details}\n\nPhone Number: {phone_number}\nAddress: {address}\nOil Type: {oil_type}\nQuantity: {quantity}"

    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)
