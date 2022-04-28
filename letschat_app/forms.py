from django import forms
from .models import Chat, Room
 
 
# creating a form
class RoomForm(forms.ModelForm):
    username = forms.CharField(
        label= 'Username',
    )
    class Meta:
        model = Room
        fields = [
            "name"
        ]
        labels = {
            'name': "Nom de la salle ",
        }
        widgets={
            "name":forms.TextInput(
                attrs={
                    'id':'room-name-input', 
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                }
            )
        }  

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = [
            "message"
        ]
        labels = {
            'message': '',
        }
        widgets={
            "message":forms.TextInput(attrs={'id':'chat-message-input'}),
        }  