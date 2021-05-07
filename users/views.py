from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView,DetailView,TemplateView
from .forms import AccountRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *



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


# class ShowProfilePage(DetailView):
#   model = Profile
#   template_name = 'users/profile.html'

#   def get_context_data(self,*args,**kwargs):
#       context = super(ShowProfilePage,self).get_context_data(*args,**kwargs)
#       user_page = get_object_or_404(Profile,id=self.kwargs['pk'])
#       context["user_page"] = user_page
#       return context


class DashboardView(LoginRequiredMixin,TemplateView):
  template_name = 'users/dashboard.html'
  login_url = reverse_lazy('home')


class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'users/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
  user_form = UserUpdateForm
  profile_form = ProfileUpdateForm
  template_name = 'users/profile.html'

  def post(self, request):
    post_data = request.POST or None
    file_data = request.FILES or None

    user_form = UserUpdateForm(post_data, instance=request.user)
    profile_form = ProfileUpdateForm(post_data, file_data, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Your profile is updated successfully!!!!')
      return HttpResponseRedirect(reverse_lazy('profile'))

    context = self.get_context_data(
                                    user_form=user_form,
                                    profile_form=profile_form
                                )

    return self.render_to_response(context)     

  def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)


# @login_required
# def profileUpdate(request):
#   if request.method == 'POST':
#     u_form = UserUpdateForm(request.POST,instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#       u_form.save()
#       p_form.save()
#       messages.success(request,'Your Profile Has Been Updated')
#       return redirect('profile')

#   else:
#     u_form = UserUpdateForm(instance=request.user)
#     p_form = ProfileUpdateForm(instance=request.user.profile)
  
#   context = {
#     'u_form':u_form,
#     'p_form':p_form
#   }
#   return render(request,'users/profile.html',context)

