

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse
from django.utils import timezone

from webapp.all_lists import symptom
from webapp.app_forms import DoctorForm, PatientForm
from webapp.authentication import UserManager
from webapp.machine_learning import learn
from webapp.models import Disease, Doctor
from webapp.sentiment_Analysis import analyze_feedback


def home(req):
    return render(req, "homepage.html")

def homepage(req):
    return render(req, "homepage.html")

# @login_required(login_url='sign-in')
def dashboard(req):

    def convert(s):
        s = s.replace(' ', '_')
        s = s[0].lower() + s[1:]
        return s

    if req.method == 'POST':
        l = []
        l.append(convert(req.POST.get('1')))
        l.append(convert(req.POST.get('2')))
        l.append(convert(req.POST.get('3')))
        l.append(convert(req.POST.get('4')))
        l.append(convert(req.POST.get('5')))
        res = learn(l)
        return render(req, "patient-dashboard.html", {'symptoms': symptom, "disease" : res})

    return render(req, "patient-dashboard.html", {'symptoms': symptom})


def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        # print(user.email)
        user = authenticate(request, email=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'sign-in.html', {'error': 'Invalid login credentials.'})
    else:
        return render(request, 'sign-in.html')


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'add.html', {'form': form})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            user = UserManager()
            email = form.data['email']
            password = form.data['password']
            user.create_user(email, password)
            user.create_superuser(email, password)
            return HttpResponseRedirect('sign-in')
    else:
        form = PatientForm()
        return render(request, 'add.html', {'form': form})

def suggest_doctor(request):
    disease = request.POST['disease']
    location = request.POST['location']
    specialization = Disease.objects.get(disease=disease).specialization
    listOfDoctors = Doctor.objects.filter(specialization = specialization, location = location)
    print(type(listOfDoctors))
    listOfDoctors = sorted(listOfDoctors, key=lambda x: x.get_rating(), reverse=True)
    return render(request, "list-of-doctors.html", {'list' : listOfDoctors})

def appointment(request):

    id = request.GET['id']
    return render(request, "feedback.html", {"id": id})

def feedback(request):
    id = request.POST['id']
    doctor = Doctor.objects.get(id=id)
    feed = request.POST['feedback']
    sentiment = analyze_feedback(feed)
    if(sentiment == 0):
        doctor.negative += 1
    else:
        doctor.positive += 1
    doctor.save()
    return render(request, "homepage.html")
