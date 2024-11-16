from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("<h1>Welcome to the Shopping Cart API</h1><p>Visit <a href='/swagger/'>API Documentation</a>.</p>")
