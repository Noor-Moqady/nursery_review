from django.shortcuts import render

def render_nursery(request):
    return render (request, "index.html")

def render_aboutus(request):
    return render (request, "about.html")

def render_register(request):
    return render (request, "appointment.html")

def render_contactus(request):
    return render (request, "contact.html")


def render_nurseries(request):
    return render (request, "team.html")
