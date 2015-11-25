from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import LoginForm
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

# Create your views here.
'''
def login(request): #passes in a request using GET request
    title = 'Welcome'
    form = LoginForm(request.POST) #parantheses creates an instance of that form

    context = {#this is a dictionary
        "title": title,
        "form": form,
    }
    context.update(csrf(request))

    if form.is_valid():
        form_instance = form.save(commit=False)
        form_instance.save()
        print(form_instance.email)
        print(form_instance.timestamp)
        context = {
            "title": "Thank You"
        }

    if request.method == "POST":
        print(request.POST)
    return render(request, "login.html", context) #server responds to GET request, should replace {} with context

'''
def login(request):
    title = "Please log in"
    c = {
        "title":title,
    }
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    #if request.method == "POST":
        #print(request.POST)#for debugging
    username = request.POST.get('username','defaultusr')#second param is default
    password = request.POST.get('password','defaultpw')
    user = auth.authenticate(username=username, password=password)
    #if match is found, a user object is returned. if no match, None is ret.

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        title = "Your login details are invalid, please try again."
        c = {
            "title":title,
        }
        c.update(csrf(request))
        return render_to_response('login.html',c)

def loggedin(request):#this displays admin form and handles saving the form i.e. register user
    title_admin = "Please fill in the form to add a user."
    if request.method=='POST':
        print(request.POST)
        form = RegistrationForm(request.POST)#post in arg
        if form.is_valid():
            form.save()
            title_admin = "Add successful."
            c = {
                "title_admin": title_admin,
            }
            c.update(csrf(request))
            return render_to_response('admin.html',c)
        else:
            title_admin = "Form entered is not valid!"
    args = {
        "title_admin": title_admin,
    }
    args.update(csrf(request))
    args['reg_form']=RegistrationForm()#no post in arg, bog standard
    return render_to_response('admin.html',args)


def logout(request):
    auth.logout(request)
    title = "Logged out."
    c = {
        "title":title,
    }
    c.update(csrf(request))
    return render_to_response('login.html',c)

def curruser(request):
    c={}
    c.update(csrf(request))
    return render_to_response('current_users.html',c)