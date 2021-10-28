from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages

from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import json
from django.http.response import JsonResponse
from django.views.generic.list import ListView
from .models import Message
from django.contrib.auth.models import User




def users(request):
    users = User.objects.all()
    return render(request , 'home.html', {'users':users})


@login_required
def discussion(request,pk):
    other_user = get_object_or_404(User,pk=pk)
    global messages
    messages = Message.objects.filter(
        Q(receiver=request.user,sender=other_user)
    )
    messages.update(seen=True)
    messages = messages  | Message.objects.filter(Q(receiver=other_user,sender=request.user))
    return render(request, 'discussion.html',{"other_user":other_user, "messages":messages})



@login_required
def ajax_load_messages(request,id):
    other_user = get_object_or_404(User,id=id)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user,sender=other_user)
    )   
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent" : message.sender == request.user
    } for message in messages]
    messages.update(seen=True)

    if request.method == 'POST':
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user,message=message)

        message_list.append({
            "sender": request.user.username,
            "message":m.message,
            "sent":True,
        })
        
    return JsonResponse(message_list, safe=False)


