from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'To Pimp a Butterfly',
        'amount': '1',
        'description': 'Kendrick Lamar',
        'category': 'Rap',
        'price': '$14'
    }

    return render(request, "main.html", context)
