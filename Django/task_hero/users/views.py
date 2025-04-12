from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save
            messages.success(request, "Account Succesfully created")
            return redirect('users:login')
    return render(request, 'users/sign-up.html', context={"form": form,})
