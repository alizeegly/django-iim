from django.http import HttpResponseRedirect
from django.shortcuts import render

from letschat_app.models import Chat, Room

from .forms import ChatForm, RoomForm

def index(request):
   context = {}

   form = RoomForm(request.POST or None)
   if form.is_valid():
      if not Room.objects.filter(name=form.cleaned_data.get("name")).exists():
         form.save()
         return HttpResponseRedirect("/chat/"+form.cleaned_data.get("name")+"?username="+form.data.get("username"))
      else:
         return HttpResponseRedirect("/chat/"+form.cleaned_data.get("name")+"?username="+form.data.get("username"))

   context['form']= form

   return render(request, "letschat_app/index.html", context)

def room_name(request, name):
   context = {}

   username = request.GET.get("username", "Anonymous")

   formChat = ChatForm(request.POST or None)

   chats = Chat.objects.filter(room=Room.objects.get(name=name))

   context['form']= formChat
   context["room_name"] = name
   context["chats"] = chats
   context["username"] = username

   # if formChat.is_valid():
   #    message = formChat.cleaned_data['message']
   #    p = Chat(room=Room.objects.get(name=name), message=message, username=username)
   #    p.save()

   return render(request, 'letschat_app/chatroom.html', context)
