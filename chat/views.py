from django.shortcuts import render,redirect
from .forms import ChatBoxForm
from .models import Chats

# Create your views here.
def chat(request):
    forms = ChatBoxForm()
    chats = Chats.objects.all()

    if request.method == 'POST':
        forms = ChatBoxForm(request.POST)
        if forms.is_valid():
            user = forms.cleaned_data['user']
            chat_box = forms.cleaned_data['chat_box']

            chats_object = Chats(user = user, chat_box = chat_box)
            chats_object.save()

            return redirect( 'chat')
    else:
        return render(request, 'chat.html' , {'forms': forms, 'chats': chats})