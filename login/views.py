from django.shortcuts import render

# def login(request):
#     return render(request, 'login.html')

from login.Forms import Bbs_dataForm
from login.models import Bbs_data


def login(request):
    if request.method == "GET":
        form = Bbs_dataForm()

        return render(request, 'senddata.html', {'form': form})

    elif request.method == "POST":
        form = Bbs_dataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
        return render(request, 'getdata.html', {'form': form})
