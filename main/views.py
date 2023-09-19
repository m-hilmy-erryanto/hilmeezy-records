from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import RecordForm
from django.urls import reverse
from main.models import Record
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    records = Record.objects.all()
    context = {
        'application_name': 'Hilmeezy Records',
        'name': 'Muhammad Hilmy Erryanto',
        'class': 'PBP F',
        'records': records
    }

    return render(request, "main.html", context)

def create_record(request):
    form = RecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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
