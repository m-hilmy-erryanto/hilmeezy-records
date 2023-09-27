from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import RecordForm
from django.urls import reverse
from main.models import Record
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    records = Record.objects.filter(user=request.user)
    context = {
        'application_name': 'Hilmeezy Records',
        'name': request.user.username,
        'records': records,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_record(request):
    form = RecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        record = form.save(commit=False)
        record.user = request.user
        record.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_record.html", context)

def show_xml(request):
    record = Record.objects.all()
    return HttpResponse(serializers.serialize("xml", record), content_type="application/xml")

def show_json(request):
    record = Record.objects.all()
    return HttpResponse(serializers.serialize("json", record), content_type="application/json")

def show_xml_by_id(request, id):
    record = Record.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", record), content_type="application/xml")

def show_json_by_id(request, id):
    record = Record.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", record), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_one(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    record.amount += 1
    record.save()
    return redirect('main:show_main')

def remove_one(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if record.amount > 0:
        record.amount -= 1
        record.save()
    return redirect('main:show_main')

def delete_record(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    record.delete()
    return redirect('main:show_main')