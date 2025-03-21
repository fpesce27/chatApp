from . import socketio
from flask_socketio import emit
from flask_login import current_user
from .models import User
from .helpers import add_message


# Receive message from client
# Send message to proper client
# Update db
@socketio.on('chatMessage')
def handle_message(data):
    data = dict(data)
    add_message(message=data['message'], sender=current_user, receiver=User.query.get(data['receiver']))
    emit("message", data["message"], broadcast=True, include_self=False)
