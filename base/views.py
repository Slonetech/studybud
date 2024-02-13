from django.shortcuts import render
from .models import Room

# Create your views here.

"""rooms = [
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'design with figma'},
    {'id':3, 'name':'frontend development'},
]
"""
 #moved from studybud/urls.py
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)
