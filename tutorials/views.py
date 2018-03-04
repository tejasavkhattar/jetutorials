from django.shortcuts import render

from .forms import ContactForm

# Create your views here.

def home(request):
	context={

	}
	return render(request,"index.html",context)

def contact(request):
	
	context={

	}
	return render(request,"contact.html",context)

def courses(request):
	context={

	}
	return render(request,"courses.html",context)

def about(request):
	context={

	}
	return render(request,"about.html",context)