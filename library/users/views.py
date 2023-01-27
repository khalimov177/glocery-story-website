from django.shortcuts import render,redirect
from django.contrib.auth import login , logout
from . import forms
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    form = forms.SignUpForm()
    return render(request,'sign_up.html',{'form': form })

def sign_in(request):
    if request.method == 'POST':
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('product_list')
    form = forms.SignInForm()
    return render(request,'product_list.html',{'form': form })

def sign_out(request):
    logout(request)
    return redirect('sign_in')
