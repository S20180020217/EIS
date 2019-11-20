from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
Config = {
    'apiKey': "AIzaSyA6eJc8HWKf-Pn_M0l0LU18t1b44ANRE9g",
    'authDomain': "eisproject-520c0.firebaseapp.com",
    'databaseURL': "https://eisproject-520c0.firebaseio.com",
    'projectId': "eisproject-520c0",
    'storageBucket': "eisproject-520c0.appspot.com",
    'messagingSenderId': "38568259347",
    'appId': "1:38568259347:web:8d6d01c859f83ad4cdf4e6",
    'measurementId': "G-9CPEN6YSCV"
  }
firebase= pyrebase.initialize_app(Config)
auth=firebase.auth()
def home(request):
  return render(request,'a.html')
def form(request):
	return render(request,'formaction.html')
def count(request):
	email=request.GET['email']
	passWord=requst.Get['password']
	user=auth.sign_in_with_email_and_password(email,passWord)
	return render(request,'count.html',{'email':email})
def about(request):
	return render(request,'about.html')