from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')



def advertisement(request):
    return render(request, 'app_advertisements/advertisement.html')


def post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)



