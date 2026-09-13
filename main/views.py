from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from collections import OrderedDict
from main.models import Experience, Skills


def show_main(request):
    context = {
        "name": "Nurfadhil Kurniawan",
        "username": "Nurfadhil",
        "npm": "2506540765",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student who enjoys tinkering with technology, especially in cybersecurity and web development. "
            "Currently part of the CTF COMPFEST 18 team. Outside of that, I also enjoy playing various sports,"
            "but not quite at an athlete's level, but I like trying my hand at many of them."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nurfadhil",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    skills = Skills.objects.all()
    grouped = OrderedDict()
    for value, label in Skills.SKILL_CHOICE:
        items = skills.filter(category=value)
        if items.exists():
            grouped[label] = items
    context = {
        "name" : "Nurfadhil",
        "grouped_skills": grouped}
    return render(request, 'skills.html', context)