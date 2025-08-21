from django.shortcuts import render

skills = ["Python", "Django", "React", "Bootstrap", "CSS"]
projects_list = [
    {"name": "Portfolio Website", "description": "My personal portfolio site", "link": "#"},
    {"name": "Blog App", "description": "A Django blog application", "link": "#"},
    {"name": "E-commerce Store", "description": "React + Django store", "link": "#"},
]

def home(request):
    context = {"skills": skills}
    return render(request, "portfolio_app/home.html", context)

def about(request):
    return render(request, "portfolio_app/about.html")

def projects(request):
    context = {"projects": projects_list}
    return render(request, "portfolio_app/projects.html", context)

def contact(request):
    return render(request, "portfolio_app/contact.html")
