from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import render_template, request
from win10toast import ToastNotifier
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'azhiyaroil@gmail.com'
app.config['MAIL_PASSWORD'] = 'lpyf eais tgdb onyp'  # Use the generated app password here
app.config['MAIL_DEFAULT_SENDER'] = 'azhiyaroil@gmail.com'


mail = Mail(app)

from flask_mail import Message

# ... (your existing imports)

def send_order_confirmation_email(user_email, order_details):
    subject = 'Order Confirmation - Azhiyaar Oil'
    recipients = ['azhiyaroil@gmail.com']  # Replace with the email where you want to receive order confirmations
    body = f"User Email: {user_email}\n\nOrder Details:\n{order_details}"
    
    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)

# ... (your existing code)

@app.route('/place_order', methods=['POST'])
def place_order():
    if request.method == 'POST':
        name = request.form.get('name')  # Use request.form.get to avoid NameError

        phone_number = request.form['phone_number']
        address = request.form['address']
        oil_type = request.form['oil_type']
        quantity = request.form['quantity']

        # Compose the email message
        subject = 'New Order'
        body = f"Name: {name}\nPhone Number: {phone_number}\nAddress: {address}\nOil Type: {oil_type}\nQuantity: {quantity}"

        # Send the email
        message = Message(subject, recipients=['azhiyaroil@gmail.com'], body=body)
        mail.send(message)

    return '''
    <html>
        <head>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    background-image: url('/static/ty.gif');
                    width: 100%;
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: flex-start;
                    align-items: center;
                }

                p {
                    color: black; /* Green color */
                    font-size: 32px;
                    font-weight: bold;
                    text-align: center;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
                    background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
                    max-width: 600px; /* Limit the width for better readability */
                    margin-top: 55px; /* Add some space from the top */
                    margin-bottom: auto; /* Push the element to the top */
                }
            </style>
        </head>
        <body>
            <p>Order Sucessfull</p>
        </body>
    </html>
'''

    return 'Invalid request.'

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+'C:/Users/iliya/Desktop/oil_web (2)/backend connected_oil/oil_web/unwrap/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Move the ToastNotifier creation inside the route or function where you want to trigger the notification
toaster = ToastNotifier()

with app.app_context():
    db.create_all()

from unwrap import routes
