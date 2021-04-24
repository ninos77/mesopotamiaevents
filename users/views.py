from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import AccountRegisterForm
from django.contrib import messages



# Create your views here.

# class UserRegisterView(SuccessMessageMixin, CreateView):
#   template_name = 'users/user-register.html'
#   form_class = AccountRegisterForm
#   success_url = '/'
#   success_message = 'Your user account has been created'
  

#   def form_valid(self, form):
#     user = form.save()
#     user.save()

#     return redirect(self.success_url)

def register(request):
  if request.method == 'POST':
    form = AccountRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data.get('email')
      messages.success(request,f'Account created for {email}!')
      return redirect('login')
  else:
    form = AccountRegisterForm()
  context = {'form':form}  
  return render(request,'users/user-register.html',context)

