import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, FileResponse, HttpResponseNotFound, JsonResponse
from main.forms import RecordForm
from django.urls import reverse
from main.models import Record
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime

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

# def create_record(request):
#     form = RecordForm(request.POST or None)

#     if form.is_valid() and request.method == "POST":
#         # record = form.save(commit=False)
#         user = request.user
#         name = form.cleaned_data['name']
#         amount = form.cleaned_data['amount']
#         description = form.cleaned_data['description']
#         genre = form.cleaned_data['genre']
#         price = form.cleaned_data['price']
#         picture = request.FILES['picture']
#         new_record = Record(user=user, name=name, amount=amount, description=description,
#                         price=price, genre=genre, picture=picture)
#         # record.save()
#         new_record.save()
#         return HttpResponseRedirect(reverse('main:show_main'))
#     context = {'form': form}
#     return render(request, "create_record.html", context)

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

def edit_record(request, id):
    record = Record.objects.get(pk = id)
    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_record.html", context)

def delete_record(request, id):
    record = Record.objects.get(pk = id)
    record.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# def get_photo(request, nama_file_photo):
#     try:
#         file = open(f'photo/{nama_file_photo}', 'rb')
#         response = FileResponse(file)

#         ext = nama_file_photo.split('.')[-1]
#         if (ext == 'png'):
#             response['Content-Type'] = 'image/png'
#         elif (ext in ['jpg', 'jpeg']):
#             response['Content-Type'] = 'image/jpeg'
#         elif (ext == 'webp'):
#             response['Content-Type'] = 'image/webp'

#         return response
#     except:
#         return Http404()
#

def get_record_json(request):
    record_item = Record.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', record_item))

@csrf_exempt
def add_record_ajax(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        price = request.POST.get("price")
        genre = request.POST.get("genre")
        image = request.POST.get("image")
        new_record = Record(user=user, name=name, amount=amount, description=description,
                            price=price, genre=genre, image=image)
        new_record.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Record.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"],
            genre = data["genre"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)