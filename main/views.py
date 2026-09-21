# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect

from collections import OrderedDict
from main.models import Experience, Skills, Project
from main.forms import ProjectForm, ExperienceForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings


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

def _secret_key_valid(request):
    return request.POST.get("secret_key", "") == settings.OWNER_SECRET_KEY


def get_experience_json(request):
    experiences = Experience.objects.all()
    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]

    context = {
        "name": "Nurfadhil",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret Key Salah. Experience tidak dapat ditambahkan.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Experience baru berhasil ditambahkan!")
            return redirect("main:show_experience")

    context = {
        "name": "Nurfadhil",
        "form": form,
    }
    return render(request, "experience_form.html", context)
 
 
def update_experience(request, experience_id):
    experience = Experience.objects.filter(pk=experience_id).first()
    if experience is None:
        messages.error(request, "Experience tidak ditemukan, mungkin sudah dihapus.")
        return redirect("main:show_experience")
    form = ExperienceForm(request.POST or None, instance=experience)
 
    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Experience tidak diperbarui.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Experience berhasil diperbarui!")
            return redirect("main:show_experience")

    context = {
        "name": "Nurfadhil",
        "form": form,
    }
    return render(request, "experience_form.html", {"name": "Nurfadhil", "form": form, "is_edit": True})
 
 
def delete_experience(request, experience_id):
    experience = Experience.objects.filter(pk=experience_id).first()
    if experience is None:
        messages.error(request, "Experience tidak ditemukan, mungkin sudah dihapus.")
        return redirect("main:show_experience")
 
    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Experience tidak dihapus.")
        else:
            experience.delete()
            messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")
 
    return redirect("main:show_experience")

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

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Burhan",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Proyek tidak ditambahkan.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
 
    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Proyek tidak diperbarui.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Proyek berhasil diperbarui!")
            return redirect("main:show_projects")
 
    context = {
    "name": "Burhan",
    "form": form,
    "is_edit": True,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Proyek tidak dihapus.")
        else:
            project.delete()
            messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")