from django.shortcuts import render

# Create your views here.
def boot_cdn(request):
    return render(request,'boot_cdn.html')

def boot_download(request):
    return render(request,'boot_download.html')

def Carousel_download(request):
    return render(request,'Carousel_download.html')

def Carousel_cdn(request):
    return render(request,'Carousel_cdn.html')