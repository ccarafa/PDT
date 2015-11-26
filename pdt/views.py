from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import ManagerPhase
from .models import ManagerIteration
from .models import DeveloperPhase
from .models import DeveloperIteration
from .forms import PhaseOpenForm
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
def home(request):
	name = "Project 1"
	request.session['projectname'] = name
	context = {
		"projectname": name
	}
	return render(request, "home.html", context)
	
def minception(request):
	if ('minception' in request.POST):
		context = {
			"projectname": request.session['projectname']
		}
		return render(request, "minception.html", context)
	else:
		return render(request, "home.html", {})
	
def minceptioniterations(request):
	
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "minceptioniterations.html", context)

def minceptionopen(request):
	title = "Please fill in these estimates to open the inception phase"
	'''
	form = PhaseOpenForm(request.POST)#post in arg
	if form.is_valid():
		form.save()
		title = "Inception Phase is now open"
		c = {
			"title": title,
		}
		c.update(csrf(request))
		return render_to_response('minceptionopen.html',c)
	else:
		title_admin = "One or more estimate is not valid!"
		args = {
		"title": title,
		"projectname": request.session['projectname']
		}
		args.update(csrf(request))
		return render_to_response('minceptionopen.html',args)'''
	if request.method=='POST':
		#phase = Phase.objects.get(title=offset)
		est_sloc = request.POST.get('est_sloc')
		hours = request.POST.get('hours')
		defects = request.POST.get('defects')
		phase_obj = ManagerPhase(phase_name='Inception Phase', project_name=request.session['projectname'], est_sloc=est_sloc, defects=defects, hours=hours, is_open=True)
		phase_obj.save()
	args = {
		"title": title,
		"projectname": request.session['projectname']
	}
	args.update(csrf(request))
	return render_to_response('minceptionopen.html')

def minceptionclose(request):
	title = "Please fill in these info to close the inception phase"
	form = PhaseOpenForm(request.POST)#post in arg
	if form.is_valid():
		form.save()
		title = "Inception Phase is now closed"
		c = {
			"title": title,
		}
		c.update(csrf(request))
		return render_to_response('minceptionclose.html',c)
	else:
		title_admin = "One or more estimate is not valid!"
	if request.method=='POST':
		#phase = Phase.objects.get(title=offset)
		sloc = request.POST.get('sloc')
		#hours = request.POST.get('hours')
		#defects = request.POST.get('defects')
		ManagerPhases= ManagerPhase.objects.all()
		for instance in ManagerPhases:
			if instance.project_name == request.session['projectname'] and instance.phase_name == 'Inception Phase':
					instance.sloc = sloc
					instance.is_open = False
					instance.save()
	args = {
		"title": title,
		"projectname": request.session['projectname']
	}
	args.update(csrf(request))
	return render_to_response('minceptionclose.html',args)
'''print(request.POST)
		form = PhaseOpenForm(request.POST)#post in arg
		if form.is_valid():
			form.save()
			title = "Inception Phase is now open"
			c = {
				"title": title,
			}
			c.update(csrf(request))
			return render_to_response('minceptionopen.html',c)
		else:
			title_admin = "One or more estimate is not valid!"
	else:
		print("test")
	args = {
		"title": title,
		"projectname": request.session['projectname']
	}
	args.update(csrf(request))
	args['PhaseOpenForm']=PhaseOpenForm()#no post in arg, bog standard
	return render_to_response('minceptionopen.html',args)'''
	
def melaboration(request):
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "melaboration.html", context)

def mconstruction(request):
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "mconstruction.html", context)
	
def mtransition(request):
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "mtransition.html", context)

def melaborationiterations(request):
	
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "melaborationiterations.html", context)
	
def mconstructioniterations(request):
	
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "mconstructioniterations.html", context)
	
def mtransitioniterations(request):
	
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "mtransitioniterations.html", context)
	
def developer(request):
	
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "dhome.html", context)

def miteration(request):
	
	context = {
		"projectname": request.session['projectname']
	}
	return render(request, "miteration.html", context)