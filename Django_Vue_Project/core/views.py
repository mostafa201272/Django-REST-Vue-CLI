from django.shortcuts import render

# Create your views here.
def vue_app(request):
    return render(request, 'vue.html')
