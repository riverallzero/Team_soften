from django.shortcuts import render


# Create your views here.
def scheduler(request):
    return render(
        request,
        'scheduler/home.html',
    )