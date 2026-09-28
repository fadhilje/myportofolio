# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from collections import OrderedDict
from main.models import Experience, Skills, Project
from main.forms import ProjectForm, ExperienceForm

# Tutorial 4
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
import datetime

# Tugas 4
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
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
        "last_login" : last_login,
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

@login_required(login_url="/login/")
@permission_required("main.add_experience", raise_exception=True)
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Experience tidak dapat ditambahkan.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Experience baru berhasil ditambahkan!")
            return redirect("main:show_experience")

    context = {
        "name": "Nurfadhil",
        "form": form,
        "is_edit": False,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
@permission_required("main.change_experience", raise_exception=True)
def update_experience(request, experience_id):
    experience = Experience.objects.filter(pk=experience_id).first()
    if experience is None:
        if request.method == "POST" and not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Experience tidak diperbarui.")
        else:
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
        "is_edit": True,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
@permission_required("main.delete_experience", raise_exception=True)
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Experience tidak dihapus.")
        else:
            experience = Experience.objects.filter(pk=experience_id).first()
            if experience is None:
                messages.error(request, "Experience tidak ditemukan, mungkin sudah dihapus.")
            else:
                experience.delete()
                messages.success(request, "Experience berhasil dihapus!")

    return redirect("main:show_experience")

def show_skills(request):
    skills = Skills.objects.all()
    grouped = OrderedDict()
    for value, label in Skills.SKILL_CHOICE:
        items = skills.filter(category=value)
        if items.exists():
            grouped[label] = items
    context = {
        "name": "Nurfadhil",
        "grouped_skills": grouped,
    }
    return render(request, "skills.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    only_starred = request.GET.get("starred") == "1"
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    if only_starred and request.user.is_authenticated:
        projects = projects.filter(starred_by=request.user)

    projects_json = serializers.serialize("json", projects, fields=("title", "description", "tech_stark", "project_url", "project_image_url"))
    return HttpResponse(projects_json, content_type="application/json")


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nurfadhil",
        "project_list": projects,
        "title_query": title_query,
        "only_starred": request.GET.get("starred") == "1" and request.user.is_authenticated,
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
@permission_required("main.add_project", raise_exception=True)
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
        "name": "Nurfadhil",
        "form": form,
        "is_edit": False,
    }
    return render(request, "projects_form.html", context)

# Key tetap di butuhkan oleh editor agar pemilik web tahu ketika editor ingin merubah page projek baik itu create/update/delete
@login_required(login_url="/login/")
@permission_required("main.change_project", raise_exception=True)
def update_project(request, project_id):
    project = Project.objects.filter(pk=project_id).first()

    if project is None:
        if request.method == "POST" and not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Proyek tidak diperbarui.")
        else:
            messages.error(request, "Proyek tidak ditemukan, mungkin sudah dihapus.")
        return redirect("main:show_projects")

    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Proyek tidak diperbarui.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Proyek berhasil diperbarui!")
            return redirect("main:show_projects")

    context = {
        "name": "Nurfadhil",
        "form": form,
        "is_edit": True,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    if request.method == "POST":
        if not _secret_key_valid(request):
            messages.error(request, "Secret key salah. Proyek tidak dihapus.")
        else:
            project = Project.objects.filter(pk=project_id).first()
            if project is None:
                messages.error(request, "Proyek tidak ditemukan, mungkin sudah dihapus.")
            else:
                project.delete()
                messages.success(request, "Proyek berhasil dihapus!")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silahkan login.")
        return redirect("main:login")

    context = {
        "name" : "Nurfadhil Kurniawan",
        "form" : form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context ={
        "name" : "Nurfadhil Kurniawan",
        "form" : form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)

    next_url = request.META.get("HTTP_REFERER")
    if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        return redirect(next_url)
    return redirect("main:show_projects")