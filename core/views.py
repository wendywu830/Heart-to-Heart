from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import HealthProfile
from core.data import classify
from random import randrange

# Create your views here.
def splash(request):
  return render(request, "splash.html", {})

def home(request):
  if request.user.is_authenticated:
    return render(request, "home.html", {})
  else:
    redirect('/')

def analyze(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      age = request.POST['age']
      sex = request.POST['sex'] #1 = male, 0 = female
      cpt = request.POST['cpt'] # 1= typical angina, 2= atypical angina, 3= non-anginal pain, 4= asymptomatic
      restbps = request.POST['restbps']
      chol = request.POST['chol']
      fbs = request.POST['fbs']# (> 120 mg/dl, 1 = true; 0 = false)
      rest_ecg = request.POST['rest_ecg'] #0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria
      max_heart_rate = request.POST['max_heart_rate']
      ex_ang = request.POST['ex_ang'] #1 = yes; 0 = no
      oldpeak = request.POST['oldpeak']
      slope = request.POST['slope'] #1: upsloping, Value 2: flat, Value 3: downsloping
      vessels = request.POST['vessels'] # (0-3) # vessels
      thal = request.POST['thal']# 3 = normal; 6 = fixed defect; 7 = reversable defect
      data_arr = [age, sex, cpt, restbps, chol, fbs, rest_ecg, max_heart_rate, ex_ang, oldpeak, slope, vessels, thal]
      pred = classify(data_arr) 

      prof = HealthProfile.objects.create(age=age, sex=sex, cpt=cpt, restbps=restbps, chol=chol, fbs=fbs, rest_ecg=rest_ecg, 
      max_heart_rate=max_heart_rate, ex_ang=ex_ang, oldpeak=oldpeak, slope=slope, vessels=vessels, thal=thal,
      disease=pred, user=request.user)
      
      return render(request, "analyze.html", {"result": pred})
    else:
      return render(request, "analyze.html", {"result": 2})
  else:
    redirect('/')

habits = ["Don't smoke.","Have a normal body mass index (BMI).", "Get moderate to vigorous exercise for at least 2.5 hours a week." \
          , "Watch 7 or fewer hours of television weekly.", "Limit sugary drinks, processed and red meats, trans fats, and sodium.", \
          "Drink one or fewer alcoholic beverages daily.", "Get enough sleep.", \
          "Eat a healthy diet of fruits and vegetables, whole grains, or omega-3 fatty acids."]

def learn(request):
  rand_num = randrange(len(habits))
  if request.user.is_authenticated:
    return render(request, "learn.html", {"habit": habits[rand_num]})
  else:
    redirect('/')

  #renders sign up page
def signup(request):
  if request.method == "POST":
    user = User.objects.create_user(first_name= request.POST['first_name'], last_name= request.POST['last_name'], email=request.POST['email'], username=request.POST['username'], password=request.POST['password'])
    login(request, user)
    return redirect('/home')
  return render(request, "signup.html", {})

#log out and redirect to login/splash page
def logout_view(request):
  logout(request)
  return redirect("/")

#validates login and redirects 
def login_view(request):
  if request.method == "POST":
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      login(request, user)
      return redirect('/home')
  return redirect('/')