from django import forms
from .models import Chats

class ChatBoxForm(forms.ModelForm):
# Define a form for the Chats model

    class Meta:
        model = Chats
        # Associate the form with the Chats model

        fields = ['user','chat_box', ]
        # Specify the fields to include in the form

        widgets = {
             'user': forms.TextInput(attrs={'max_length': 50, 'required': True}),
            # The user field as a CharField with a maximum length of 50 characters and is required

            'chat_box' : forms.Textarea(attrs={'max_length': 500, 'required':True}),
            # The chat_box field as a textarea with a maximum length of 500 characters and is required
        }