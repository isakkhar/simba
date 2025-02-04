from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name='home/base.html')

def about(request):
    return render(request, template_name='home/about.html')

