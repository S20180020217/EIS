from django.http import HttpResponse
from django.shortcuts import render
def form(request):
	return render(request,'formaction.html')
def count(request):
	Firstname=request.GET['Firstname']
	return render(request,'count.html',{'Firstname':Firstname})
def about(request):
	return render(request,'about.html')