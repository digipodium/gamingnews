from django.http import request
from django.http.response import HttpResponse
from users.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News
from django.core import serializers

# Create your views here.
def index(request):
    ctx = {'title':'Welcome'}
    return render(request, 'index.html',ctx)

@login_required
def dashboard(request):
    ctx = {'title':'Dashboard'}
    return render(request, 'registration/dashboard.html',ctx)


def register(request):
    form  = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created!')
            return redirect('login')
        else:
            messages.error(request, 'Error!')
    ctx = {'title':'Register', 'form':form}
    return render(request, 'registration/register.html',ctx)

def search(request):
    query = request.GET.get('q')
    if query:
        results = News.objects.filter(title__icontains=query)
        if len(results)>0:
            qlist = serializers.serialize('json', results)
            return HttpResponse(qlist, content_type="text/json")
    return HttpResponse("{}",content_type='text/json')

