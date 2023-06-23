from django.shortcuts import render, redirect
from .forms import ChatBoxForm
from .models import Chats

# Create your views here.

# View for the chat functionality
def chat(request):
    forms = ChatBoxForm()  # Create an instance of the chat form
    chats = Chats.objects.all()  # Retrieve all chat objects from the database

    if request.method == 'POST':
        forms = ChatBoxForm(request.POST)
        if forms.is_valid():
            user = forms.cleaned_data['user']  # Extract the user value from the form
            chat_box = forms.cleaned_data['chat_box']  # Extract the chat message from the form

            chats_object = Chats(user=user, chat_box=chat_box)  # Create a new chat object with the extracted values
            chats_object.save()  # Save the chat object to the database

            return redirect('chat')  # Redirect the user back to the chat page after submitting the form
    else:
        return render(request, 'chat.html', {'forms': forms, 'chats': chats})  # Render the chat page with the form and existing chat objects
