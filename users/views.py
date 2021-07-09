from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {'title':'Welcome'}
    return render(request, 'index.html',ctx)

def dashboard(request):
    ctx = {'title':'Dashboard'}
    return render(request, 'dashboard.html',ctx)