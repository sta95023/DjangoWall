from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import datetime

def index(request):
    return render(request, "wall/reg_log.html")
def register(request): # Post
    pw_hash = bcrypt.hashpw(request.POST['user_password'].encode(), bcrypt.gensalt())
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
    u = Users.objects.create(first_name = request.POST["user_firstname"], last_name = request.POST["user_lastname"], email = request.POST["user_email"], password = pw_hash)
    request.session['my_val'] = u.id
    return redirect('/message_wall')
def login(request):
    listOfmatchingUsers = Users.objects.filter(email = request.POST['user_email'])
    if bcrypt.checkpw(request.POST['user_password'].encode(), listOfmatchingUsers[0].password.encode()):
        request.session['my_val'] = listOfmatchingUsers[0].id
        return redirect('/message_wall')
    else:
        return redirect ("/")
def messageWall(request):
    if "my_val" not in request.session:
       return redirect("/")
    if request.method == "POST":
        m = Messages.objects.create(messages = request.POST["user_messages"])
        return redirect("/message_wall")
    if request.method == "GET":
        context = {
            'user': Users.objects.get(id=request.session["my_val"]),
            'all_messages': Messages.objects.all()
        }
        return render(request, "wall/message_wall.html", context)
def commentsAll(request):
    if request.method == "POST":
        c = Comments.objects.create(comments = request.POST["user_comments"], message=Messages.objects.get(id=request.POST['message']))
        return redirect("/message_wall")
def logOut(request):
    request.session.clear()
    return redirect("/")
