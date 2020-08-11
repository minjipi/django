from django.shortcuts import render


def read_data(request):
    return render(request, 'getdata.html')
