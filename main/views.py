from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306256343',
        'name': 'Hafizh Surya Mustafa Zen',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)