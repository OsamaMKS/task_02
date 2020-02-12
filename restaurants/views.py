from django.shortcuts import render

def x(request):
	context ={
		"msg": "Hello World!"
	}
	return render(request, "x.html", context)

def r(request):
	context = {
		"msg":"Hello World!"
	}
	return render(request,"hello.html",context)
