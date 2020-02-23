from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Contacts
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AddContacts
from django.contrib import messages
# Create your views here.
class index(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contacts
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(user=self.request.user)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                            request, 'Registration Successfull')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})


def add(request):
    if request.method == 'POST':
        form = AddContacts(request.POST)
        if form.is_valid():
            publish = form.save(commit=False)
            publish.user = request.user
            publish.save()
            messages.success(
                            request, 'Your contact has been successfully Added!')
            return redirect('index')
    else:
        form = AddContacts()
    return render(request,'add.html',{'form':form})

def delete(request,id):
    contact = Contacts.objects.get(pk=id)
    contact.delete()
    messages.success(
                    request, 'Your contact has been deleted!')
    return redirect('index')

class edit(LoginRequiredMixin, UpdateView):
    model = Contacts
    template_name = 'edit.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']

    def form_valid(self, form):
        instance = form.save()
        messages.success(
            self.request, 'Your contact has been successfully updated!')
        return redirect('index')
