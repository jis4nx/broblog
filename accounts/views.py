from django.shortcuts import redirect, render
from .forms import SignUpForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from blog.models import Blog
from django.views.generic import ListView 

def register(request):
    form = SignUpForm()
    is_registered = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            is_registered = True
        else:
            is_registered = False
    return render(request, 'accounts/signup.html', {'form':form, 'registered':is_registered})



def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect("home")
        else:
            messages.error(request, "Failed to login")
    return render(request, 'accounts/signin.html')


@login_required
def signout(request):
    logout(request)
    messages.warning(request,"You've been logged out!")
    return redirect('accounts:login')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html' )


def profileEdit(request):
    pform = UserForm(instance=request.user)
    if request.method == "POST":
        pform = UserForm(request.POST, request.FILES, instance=request.user.userprofile)
        if pform.is_valid():
            pform.save()
    return render(request, 'accounts/edit_profile.html', {'pform':pform})


class MyBlogs(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'accounts/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyBlogs, self).get_context_data(**kwargs)
        blogs = Blog.objects.filter(author=self.request.user)
        context['blogs'] = blogs
        return context
    
