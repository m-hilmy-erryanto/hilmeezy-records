from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application_name': 'Hilmeezy Records',
        'name': 'Muhammad Hilmy Erryanto',
        'class': 'PBP F',
    }

    return render(request, "main.html", context)
