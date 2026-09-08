from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Nurfadhil",
        "npm": "2506540765",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang percaya bahwa teknologi "
            "dan pendidikan adalah kombinasi terbaik untuk menciptakan perubahan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nurfadhil",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)