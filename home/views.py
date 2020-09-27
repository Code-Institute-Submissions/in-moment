from django.shortcuts import render

# Create your views here.
# A view rendering home page template.
def index(request):
    return render(request, "home/index.html")
