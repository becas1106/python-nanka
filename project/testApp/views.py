from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User

TEMPLATE_INDEX = 'testApp/index.html'
def index(request):
    template_name = TEMPLATE_INDEX
    form = LoginForm(request.POST or None)
    context = {}
    context['form'] = form
    request.session.clear()

    if form.is_valid():
        try:
            targetUser = User.objects.get(user_id = form.cleaned_data['user'], password = form.cleaned_data['password'])
        except User.DoesNotExist:
            return redirect('./')
        
        template_name = TEMPLATE_TOP
        request.session['id'] = str(targetUser.id)
        request.session['loggedin'] = True
    return render(request,template_name,context)


TEMPLATE_REGISTER = 'testApp/register.html'
def register(request):
    template_name = TEMPLATE_REGISTER
    form = RegisterForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == 'POST' :
        if form.is_valid():
            template_name = TEMPLATE_INDEX
            form.save()
            return redirect('/test')
    return render(request,template_name,context)


TEMPLATE_TOP = 'testApp/top.html'
def top(request):
    loggedin = request.session.get('loggedin')
    id = request.session.get('id')
    context = {}
    context['user'] = id
    if loggedin:
        return render(request, TEMPLATE_TOP, context)
    else:
        return redirect('/test')