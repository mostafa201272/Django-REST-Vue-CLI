from django.shortcuts import render

# Create your views here.
def vue_app(request):
    data = {
        "Username": "Mostafa Mahmoud EL-sherbiniy"
    }
    return render(request, 'vue.html', data)
