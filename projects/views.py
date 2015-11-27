from django.shortcuts import render
from .models import ManagerProject

# Create your views here.
def managerprojects(request):
	projects = ManagerProject.objects.all()
	if('add' in request.POST):
		uid = request.POST.get('uid')
		project_name = request.POST.get('projectname')
		#hours = request.POST.get('hours')
		#SLOC = request.POST.get('SLOC')
		instance = ManagerProject.objects.create(project_name=project_name)
		instance.save()
		context = {
			"projects": projects,
			"name": "Tina",
		}
		for obj in ManagerProject.objects.all():
			if obj.project_name == project_name:
				obj.manager = "Tina"
				obj.project_id = uid
				#obj.hours = hours
				#obj.sloc = SLOC
				obj.save()
		return render(request, "manager.html", context)
	return render(request, "addprojectsform.html", {})

def projectpage(request):
	for name in request.POST:
		print name
		request.session['project_name'] = name
	return render(request, "projectpage.html", {})

def projectbuttons(request):
	for instance in ManagerProject.objects.all():
		if instance.project_name == request.session['project_name']:
			if 'open' in request.POST:
				instance.is_open = True
				instance.save()
				return render(request, "openform.html", {})
			if 'close' in request.POST:
				instance.is_open = False
				instance.save()
				return render(request, "closeproject.html", {})
			if 'phases' in request.POST:
				return render(request, "phases.html", {})
			if 'add_developers' in request.POST:
				print ("developers need to be added")
			if 'metrics' in request.POST:
				print ("metrics")
	return render(request, "projectpage.html", {})