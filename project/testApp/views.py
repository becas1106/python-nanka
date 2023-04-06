from django.shortcuts import render, redirect
from .forms import LoginForm

TEMPLATE_INDEX = 'testApp/index.html'
def index(request):
    template_name = TEMPLATE_INDEX
    form = LoginForm(request.POST or None)
    context = {}
    context['form'] = form
    request.session.clear()

    if form.is_valid():
        template_name = TEMPLATE_TOP
        request.session['loggedin'] = True
     
    print(template_name)
    return render(request,template_name,context)


TEMPLATE_REGISTER = 'testApp/register.html'
def register(request):
    template_name = TEMPLATE_REGISTER
    form = LoginForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        template_name = TEMPLATE_INDEX
    print(template_name)
    return render(request,template_name,context)


TEMPLATE_TOP = 'testApp/top.html'
def top(request):
    loggedin = request.session.get('loggedin')
    if loggedin:
        return render(request, TEMPLATE_TOP)
    else:
        return redirect('/test')