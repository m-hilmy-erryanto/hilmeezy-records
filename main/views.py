from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Application Name': 'hilmeezy records',
        'Name': 'Muhammad Hilmy Erryanto',
        'Class': 'PBP F',
    }

    return render(request, "main.html", context)
