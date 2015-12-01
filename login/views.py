from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from time import time
from .forms import LoginForm
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .models import Signin
from projects.models import Project, ProjectsDeveloper, Phase, Iteration, Activity, Defect

# Create your views here.

def developerphases(request):
	for name in request.POST:
		if name!="csrfmiddlewaretoken":
			project_name = name
	request.session['project_name']=project_name
	return render(request, "developerphases.html", {})

def developerinceptioniterations(request):
	request.session['phase_name']='Inception Phase'
	return render(request, "developerinceptioniterations.html")

def developerelaborationiterations(request):
	request.session['phase_name']='Elaboration Phase'
	return render(request, "developerelaborationiterations.html")

def developerconstructioniterations(request):
	request.session['phase_name']='Construction Phase'
	return render(request, "developerconstructioniterations.html")

def developertransitioniterations(request):
	request.session['phase_name']='Transition Phase'
	return render(request, "developertransitioniterations.html")

def login(request):
	title = "Please log in"
	c = {
		"title":title,
	}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username')
	request.session['username']=username
	password = request.POST.get('password')
	request.session['name']=username
	for instance in Signin.objects.all():
		if(instance.username==username):
			if(instance.password==password):
				request.session['name'] = username
				if(instance.role=="Manager"):
					return HttpResponseRedirect('/manager')
				elif(instance.role=="Developer"):
					return HttpResponseRedirect('/developer')
				elif(instance.role=='Admin'):
					return HttpResponseRedirect('/loggedin')
	return HttpResponseRedirect('/loggedin')

def loggedin(request):#this displays admin form and handles saving the form i.e. register user
	title_admin = "Please fill in the form to add a user."
	if request.method=='POST':
		print(request.POST)
		form = RegistrationForm(request.POST)#post in arg
		if form.is_valid():
			form.save()
			title_admin = "Add successful."
			c = {
				"title_admin": title_admin,
			}
			c.update(csrf(request))
			return render_to_response('admin.html',c)
		else:
			title_admin = "Form entered is not valid!"

	args = {
		"title_admin": title_admin,
	}
	args.update(csrf(request))
	args['reg_form']=RegistrationForm()#no post in arg, bog standard
	return render_to_response('admin.html',args)


def logout(request):
	auth.logout(request)
	title = "Logged out."
	c = {
		"title":title,
	}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def curruser(request):
	if request.method=='POST':
		print("following are DB info")
		print(request.POST)
	signin = Signin.objects.all()
	c={
		"signin":signin
	}
	return render_to_response('current_users.html',c,RequestContext(request))

def manager(request):
	projects = Project.objects.all()
	context = {
			"projects": projects,
			"name": request.session['name'],
		}
	return render_to_response('manager.html',context,RequestContext(request))

def developer(request):
	projects = ProjectsDeveloper.objects.all()
	context = {
			"projects": projects,
			"name": request.session['name'],
		}
	return render_to_response('developer.html',context,RequestContext(request))

def managerprojects(request):
	projects = Project.objects.all()
	if('add' in request.POST):
		project_name = request.POST.get('projectname')
		instance = Project.objects.create(project_name=project_name, manager=request.session['name'])
		instance.save()
		instance = Phase.objects.create(project_name=project_name, phase_name="Inception Phase")
		instance.save()
		instance = Phase.objects.create(project_name=project_name, phase_name="Elaboration Phase")
		instance.save()
		instance = Phase.objects.create(project_name=project_name, phase_name="Construction Phase")
		instance.save()
		instance = Phase.objects.create(project_name=project_name, phase_name="Transition Phase")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Inception Phase", iteration_name="Iteration 1")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Elaboration Phase", iteration_name="Iteration 1")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Elaboration Phase", iteration_name="Iteration 2")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Construction Phase", iteration_name="Iteration 1")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Construction Phase", iteration_name="Iteration 2")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Construction Phase", iteration_name="Iteration 3")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Transition Phase", iteration_name="Iteration 1")
		instance.save()
		instance = Iteration.objects.create(project_name=project_name, phase_name="Transition Phase", iteration_name="Iteration 2")
		instance.save()

		context = {
			"projects": projects,
			"name": request.session['name'],
		}
		return render(request, "manager.html", context)
	return render(request, "addprojectsform.html", {})

def projectpage(request):
	for name in request.POST:
		if name != "csrfmiddlewaretoken" and name!="back":
			request.session['project_name'] = name
	for instance in Project.objects.all():
		if instance.project_name == request.session['project_name']:
			if instance.is_started == False and instance.is_open == False:
				request.session['state'] = "started"
			elif instance.is_started == True and instance.is_open == True:
				request.session['state'] = "open"
			elif instance.is_started == True and instance.is_open == False:
				request.session['state'] = "close"
	context = {
					"state": request.session['state'],
					"open": "open",
					"close": "close",
					"started": "started",
					"project_name": request.session['project_name'],
				}
	return render(request, "projectpage.html", context)

def projectbuttons(request):
	for instance in Project.objects.all():
		if instance.project_name == request.session['project_name']:
			context={
				"project_name":request.session['project_name'],
			}
			if 'open' in request.POST:
				instance.is_open = True
				instance.is_started = True
				instance.save()
				context={
					"project_name":request.session['project_name'],
				}
				return render(request, "open.html", context)
			if 'close' in request.POST:
				print ("ok")
				instance.is_open = False
				instance.is_started = True
				instance.save()
				context={
					"project_name":request.session['project_name'],
				}
				return render(request, "close.html", context)
			if 'phases' in request.POST:
				print ("ok1")
				context={
					"project_name":request.session['project_name'],
				}
				return render(request, "phases.html", context)
			if 'add_developers' in request.POST:
				print ("ok2")
				context={
					"usernames":Signin.objects.all(),
					"role": "Developer",
				}
				return render(request, "add_developer.html", context)
			if 'metrics' in request.POST:
				return projectviewmetrics(request)
			if 'closesubmit' in request.POST:
				print ("ok")
				instance.sloc = request.POST.get('sloc')
				instance.save()
				context = {
					"state":"Data is saved."
				}
				return render(request, "close.html", context)
			if 'submit' in request.POST:
				instance.estimate_sloc = request.POST.get('estimate_sloc')
				instance.hours = request.POST.get('hours')
				instance.save()
				context = {
					"state":"Data is saved."
				}
				return render(request, "open.html", context)
			if 'back' in request.POST:
				context={
					"project_name":request.session['project_name'],
				}
				return render(request, "phases.html", context)
	return render(request, "projectpage.html", context)

def projectdata(request):
	if 'submit' in request.POST:
		for instance in Project.objects.all():
			if instance.project_name == request.session['project_name']:
				instance.estimate_sloc = request.POST.get('estimate_sloc')
				instance.hours = request.POST.get('hours')
				instance.save()
	return render(request, "projectpage.html", {})

def add_developer(request):
	developer_name = request.POST.get('name')
	is_present = False
	for instance in Signin.objects.all():
		if instance.role=="Developer" and instance.username==developer_name:
			instance = ProjectsDeveloper.objects.create(developer_name=developer_name, project_name=request.session['project_name'])
			instance.save()
			is_present = True
	if is_present is not True:
		context = {
			"state":"Developer doesnt exist in the database. Please verify the username",
			"usernames":Signin.objects.all(),
			"role": "Developer",
		}
		return render(request, "add_developer.html", context)
	context={
		"state":"Developer added",
		"usernames":Signin.objects.all(),
		"role": "Developer",
	}
	return render(request, "add_developer.html", context)

def add_message(request):
	return render(request, "add_message.html", {})

def phase(request):
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	if 'inception' in request.POST:
		request.session['phase_name'] = "Inception Phase"
	if 'elaboration' in request.POST:
		request.session['phase_name'] = "Elaboration Phase"
	if 'construction' in request.POST:
		request.session['phase_name'] = "Construction Phase"
	if 'transition' in request.POST:
		request.session['phase_name'] = "Transition Phase"
	if 'viewmetrics' in request.POST:
		return phaseviewmetrics(request)

	for instance in Phase.objects.all():
		if instance.project_name == request.session['project_name'] and instance.phase_name == request.session['phase_name']:
			if instance.is_started == False and instance.is_open == False:
				request.session['state'] = "started"
			elif instance.is_started == True and instance.is_open == True:
				request.session['state'] = "open"
			elif instance.is_started == True and instance.is_open == False:
				request.session['state'] = "close"

	for instance in Phase.objects.all():
		if instance.project_name == request.session['project_name'] and instance.phase_name == request.session['phase_name']:
			if 'open' in request.POST:
				request.session['state'] = "open"
				instance.is_open = True
				instance.is_started = True
				instance.save()
			if 'close' in request.POST:
				request.session['state'] = "close"
				instance.is_started = True
				instance.is_open = False
				instance.save()
			if 'iterations' in request.POST:
				context={
					"project_name": request.session['project_name'],
					"phase_name": request.session['phase_name'],
				}
				if instance.phase_name == "Elaboration Phase":
					return render(request, "elaboration_iteration.html", context)
				elif instance.phase_name == "Inception Phase":
					return render(request, "inception_iteration.html", context)
				elif instance.phase_name == "Construction Phase":
					return render(request, "construction_iteration.html", context)
				elif instance.phase_name == "Transition Phase":
					return render(request, "transition_iteration.html", context)
			if 'metrics' in request.POST:
				return phaseviewmetrics(request)
	context = {
		"state": request.session['state'],
		"open": "open",
		"close": "close",
		"started": "started",
		"project_name": request.session['project_name'],
		"phase_name": request.session['phase_name'],
	}
	return render(request, "phasespage.html", context)

def iteration(request):
	if 'Iteration1' in request.POST:
		request.session['iteration_name'] = "Iteration 1"
	if 'Iteration2' in request.POST:
		request.session['iteration_name'] = "Iteration 2"
	if 'Iteration3' in request.POST:
		request.session['iteration_name'] = "Iteration 3"
	print (request.session['phase_name'])
	for instance in Iteration.objects.all():
		if(instance.project_name == request.session['project_name']):
			if(instance.phase_name == request.session['phase_name']):
				if(instance.iteration_name == request.session['iteration_name']):
					print ("ok")
					if instance.is_started == False and instance.is_open == False:
						request.session['state'] = "started"
					elif instance.is_started == True and instance.is_open == True:
						request.session['state'] = "open"
					elif instance.is_started == True and instance.is_open == False:
						request.session['state'] = "close"
	if 'open' in request.POST:
		for instance in Iteration.objects.all():
			if(instance.project_name == request.session['project_name'] and
				instance.phase_name == request.session['phase_name'] and
				instance.iteration_name == request.session['iteration_name']):
				request.session['state'] = "open"
				instance.is_open = True
				instance.is_started = True
				instance.save()
	if 'close' in request.POST:
		for instance in Iteration.objects.all():
			if(instance.project_name == request.session['project_name'] and
				instance.phase_name == request.session['phase_name'] and
				instance.iteration_name == request.session['iteration_name']):
				request.session['state'] = "close"
				instance.is_open = False
				instance.is_started = True
				instance.save()
	if 'metrics' in request.POST:
		return phaseviewmetrics(request)
	context = {
		"state": request.session['state'],
		"open": "open",
		"close": "close",
		"started": "started",
		"project_name": request.session['project_name'],
		"phase_name": request.session['phase_name'],
		"iteration_name": request.session['iteration_name'],
	}
	return render(request, "iterationphase.html", context)

def activityDashboard(request):
	if request.POST.get("Iteration 1"):
		request.session['iteration_name']="Iteration 1"
	elif request.POST.get("Iteration 2"):
		request.session['iteration_name']="Iteration 2"
	elif request.POST.get("Iteration 3"):
		request.session['iteration_name']="Iteration 3"
	print (request.session['project_name'])
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	username = request.session['username']
	if ('development' in request.POST):
		activity_type = 'Development'
		request.session['activity_type'] = activity_type
		url = reverse('developmentActivity')
		return HttpResponseRedirect(url)
	elif ('defects' in request.POST):
		activity_type = 'Defect Removal'
		request.session['activity_type'] = activity_type
		url = reverse('defectsActivity')
		return HttpResponseRedirect(url)
	elif ('management' in request.POST):
		activity_type = 'Management'
		request.session['activity_type'] = activity_type
		url = reverse('managementActivity')
		return HttpResponseRedirect(url)

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
	}
	return render(request, "ActivityDashboard.html", context)

def activity(request):
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	username = request.session['username']
	activity_type = request.session['activity_type']
	activity_status = 'N/A'
	sloc = 'N/A'
	defects = 'N/A'
	duration = 'N/A'
	error = 'No error'
		
	try:
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		activity_status = str(instance.is_open)
		sloc = str(instance.sloc)
		defects = str(instance.defects)
		duration = str(instance.duration)

	except Activity.DoesNotExist:
		error = 'No error'

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"activity_type": activity_type,
		"activity_status": activity_status,
		"sloc": sloc,
		"defects": defects,
		"error": error,
		"duration": duration,
	}
	
	if ('start' in request.POST):
		canstart = True
		cproject = Project.objects.get(project_name = project_name)
		cphase = Phase.objects.get(phase_name = phase_name, project_name = project_name)
		citeration = Iteration.objects.get(iteration_name = iteration_name, phase_name = phase_name, project_name = project_name)
		if (cproject.is_open == False):
			error = 'Project is closed'
			canstart = False
		if (cphase.is_open == False):
			error = 'Phase is closed'
			canstart = False
		if (citeration.is_open == False):
			error = 'Iteration is closed'
			canstart = False

		if (canstart):
			exist = False
			for instance in Activity.objects.all():
				if (instance.project_name==project_name and instance.phase_name==phase_name and instance.iteration_name==iteration_name and username==username):
					if (instance.activity_type==activity_type):
						exist = True
						if (instance.is_open == False):
							instance.start_time = str(time())
							instance.is_open = True
							activity_status = str(True)
							sloc = str(instance.sloc)
							defects = str(instance.defects)
							duration = str(instance.duration)
							instance.save()
							error = 'Start: Timer started'
						else:
							error = 'Start: Timer is already running'
					else:
						if (instance.is_open==True):
							pause = time()
							start = float(instance.start_time)
							instance.pause_time = str(pause)
							total = float(instance.duration) + (pause - start)
							instance.duration = str(total)
							instance.is_open = False
							instance.save()
			if (exist == False):
				instance = Activity.objects.create(start_time=str(time()), is_open=True, activity_type=activity_type, project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username)
				activity_status = str(True)
				sloc = str(instance.sloc)
				defects = str(instance.defects)
				duration = str(instance.duration)
				instance.save()
				error = 'Start: Timer started'

	elif ('pause' in request.POST):
		# error = 'Not found'
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			if (instance.is_open == True):
				pause = time()
				start = float(instance.start_time)
				instance.pause_time = str(pause)
				total = float(instance.duration) + (pause - start)
				instance.duration = str(total)
				instance.is_open = False
				instance.save()
				error = 'Timer paused'
				activity_status = str(False)
				sloc = str(instance.sloc)
				defects = str(instance.defects)
				duration = str(instance.duration)
			else:
				error = 'Pause: Timer has not been started'
		except Activity.DoesNotExist:
			error = 'Pause: Timer has not been started'
		except Activity.MultipleObjectsReturned:
			error = 'Pause: Multiple timers for this user in this activity'

	elif ('stop' in request.POST):
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			return render(request, "ActivityForm.html", context)
		except Activity.DoesNotExist:
			error = 'Stop: Timer has not been started'
	elif ('edit' in request.POST):
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			return render(request, "ActivityEdit.html", context)
		except Activity.DoesNotExist:
			error = 'Edit: Timer has not been started'
	elif ('submit_metrics' in request.POST):
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		lines = float(request.POST['sloc'])
		defect = int(float(request.POST['defects']))
		instance.sloc += lines
		instance.defects += defect
		if (instance.is_open == True):
			pause = time()
			start = float(instance.start_time)
			instance.pause_time = str(pause)
			total = float(instance.duration) + (pause - start)
			instance.duration = str(total)
			instance.is_open = False
			instance.save()
			activity_status = str(False)
			sloc = str(instance.sloc)
			defects = str(instance.defects)
			duration = str(instance.duration)
		else:
			instance.save()
			activity_status = str(False)
			sloc = str(instance.sloc)
			defects = str(instance.defects)
			duration = str(instance.duration)
	elif ('edit_metrics' in request.POST):
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		lines = float(request.POST['sloc'])
		defect = int(float(request.POST['defects']))
		dur = str(request.POST['duration'])
		instance.sloc = lines
		instance.defects = defect
		instance.duration = dur
		instance.save()
		sloc = str(instance.sloc)
		defects = str(instance.defects)
		duration = str(instance.duration)


	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"activity_type": activity_type,
		"activity_status": activity_status,
		"sloc": sloc,
		"defects": defects,
		"error": error,
		"duration": duration,
	}
	return render(request, "Activity.html", context)

def developmentActivity(request):
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	username = request.session['username']
	activity_type = "Development"
	activity_status = 'N/A'
	sloc = 'N/A'
	duration = 'N/A'
	error = 'No error'

	try:
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		activity_status = str(instance.is_open)
		sloc = str(instance.sloc)
		defects = str(instance.defects)
		duration = str(instance.duration)

	except Activity.DoesNotExist:
		error = 'No error'

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"activity_type": activity_type,
		"activity_status": activity_status,
		"sloc": sloc,
		"error": error,
		"duration": duration,
	}

	if ('start' in request.POST):
		canstart = True
		cproject = Project.objects.get(project_name = project_name)
		cphase = Phase.objects.get(phase_name = phase_name, project_name = project_name)
		citeration = Iteration.objects.get(iteration_name = iteration_name, phase_name = phase_name, project_name = project_name)
		if (cproject.is_open == False):
			error = 'Project is closed'
			canstart = False
		if (cphase.is_open == False):
			error = 'Phase is closed'
			canstart = False
		if (citeration.is_open == False):
			error = 'Iteration is closed'
			canstart = False
		
		if (canstart):
			exist = False
			for instance in Activity.objects.all():
				if (instance.project_name==project_name and instance.phase_name==phase_name and instance.iteration_name==iteration_name and username==username):
					if (instance.activity_type==activity_type):
						exist = True
						print (str(instance.is_open))
						if (instance.is_open == False):
							instance.start_time = str(time())
							instance.is_open = True
							activity_status = str(True)
							sloc = str(instance.sloc)
							defects = str(instance.defects)
							duration = str(instance.duration)
							instance.save()
							error = 'Start: Timer started'
						else:
							error = 'Start: Timer is already running'
					else:
						if (instance.is_open==True):
							pause = time()
							start = float(instance.start_time)
							instance.pause_time = str(pause)
							total = float(instance.duration) + (pause - start)
							instance.duration = str(total)
							instance.is_open = False
							instance.save()
			if (exist == False):
				instance = Activity.objects.create(start_time=str(time()), is_open=True, activity_type=activity_type, project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username)
				activity_status = str(True)
				sloc = str(instance.sloc)
				defects = str(instance.defects)
				duration = str(instance.duration)
				instance.save()
				error = 'Start: Timer started'

	elif ('pause' in request.POST):
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			if (instance.is_open == True):
				pause = time()
				start = float(instance.start_time)
				instance.pause_time = str(pause)
				total = float(instance.duration) + (pause - start)
				instance.duration = str(total)
				instance.is_open = False
				instance.save()
				error = 'Timer paused'
				activity_status = str(False)
				sloc = str(instance.sloc)
				defects = str(instance.defects)
				duration = str(instance.duration)
			else:
				error = 'Pause: Timer has not been started'
		except Activity.DoesNotExist:
			error = 'Pause: Timer has not been started'
		except Activity.MultipleObjectsReturned:
			error = 'Pause: Multiple timers for this user in this activity'

	elif ('stop' in request.POST):
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			return render(request, "developmentForm.html", context)
		except Activity.DoesNotExist:
			error = 'Stop: Timer has not been started'

	elif ('submit_metrics' in request.POST):
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		lines = float(request.POST['sloc'])
		instance.sloc += lines
		if (instance.is_open == True):
			pause = time()
			start = float(instance.start_time)
			instance.pause_time = str(pause)
			total = float(instance.duration) + (pause - start)
			instance.duration = str(total)
			instance.is_open = False
			instance.save()
			activity_status = str(False)
			sloc = str(instance.sloc)
			duration = str(instance.duration)
		else:
			instance.save()
			activity_status = str(False)
			sloc = str(instance.sloc)
			duration = str(instance.duration)

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"activity_type": activity_type,
		"activity_status": activity_status,
		"sloc": sloc,
		"error": error,
		"duration": duration,
	}

	return render(request, "developmentActivity.html", context)

def defectsActivity(request):
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	username = request.session['username']
	activity_type = "Defect Removal"
	activity_status = 'N/A'
	sloc = 'N/A'
	duration = 'N/A'
	error = 'No error'
		
	try:
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		activity_status = str(instance.is_open)
		sloc = str(instance.sloc)
		duration = str(instance.duration)

	except Activity.DoesNotExist:
		error = 'No error'

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"activity_type": activity_type,
		"activity_status": activity_status,
		"error": error,
		"duration": duration,
	}

	if ('start' in request.POST):
		canstart = True
		cproject = Project.objects.get(project_name = project_name)
		cphase = Phase.objects.get(phase_name = phase_name, project_name = project_name)
		citeration = Iteration.objects.get(iteration_name = iteration_name, phase_name = phase_name, project_name = project_name)
		if (cproject.is_open == False):
			error = 'Project is closed'
			canstart = False
		if (cphase.is_open == False):
			error = 'Phase is closed'
			canstart = False
		if (citeration.is_open == False):
			error = 'Iteration is closed'
			canstart = False
		
		if (canstart):
			exist = False
			for instance in Activity.objects.all():
				if (instance.project_name==project_name and instance.phase_name==phase_name and instance.iteration_name==iteration_name and username==username):
					if (instance.activity_type==activity_type):
						exist = True
						print (str(instance.is_open))
						if (instance.is_open == False):
							instance.start_time = str(time())
							instance.is_open = True
							activity_status = str(True)
							duration = str(instance.duration)
							instance.save()
							error = 'Start: Timer started'
						else:
							error = 'Start: Timer is already running'
					else:
						if (instance.is_open==True): #To stop some other activity whose timer is running
							pause = time()
							start = float(instance.start_time)
							instance.pause_time = str(pause)
							total = float(instance.duration) + (pause - start)
							instance.duration = str(total)
							instance.is_open = False
							instance.save()
			if (exist == False): #Start new timer if it doesn't exist before
				instance = Activity.objects.create(start_time=str(time()), is_open=True, activity_type=activity_type, project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username)
				activity_status = str(True)
				duration = str(instance.duration)
				instance.save()
				error = 'Start: Timer started'
	elif ('pause' in request.POST):
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			if (instance.is_open == True):
				pause = time()
				start = float(instance.start_time)
				instance.pause_time = str(pause)
				total = float(instance.duration) + (pause - start)
				instance.duration = str(total)
				instance.is_open = False
				instance.save()
				error = 'Timer paused'
				activity_status = str(False)
				duration = str(instance.duration)
			else:
				error = 'Pause: Timer has not been started'
		except Activity.DoesNotExist:
			error = 'Pause: Timer has not been started'
		except Activity.MultipleObjectsReturned:
			error = 'Pause: Multiple timers for this user in this activity'
	elif ('stop' in request.POST):
		try:
			instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
			if (instance.is_open == True):
				pause = time()
				start = float(instance.start_time)
				instance.pause_time = str(pause)
				total = float(instance.duration) + (pause - start)
				instance.duration = str(total)
				instance.is_open = False
				instance.save()
				error = 'Timer stopped'
				activity_status = str(False)
				duration = str(instance.duration)
			else:
				error = 'Stop: Timer has not been started'
			return render(request, "defectsForm.html", context)
		except Activity.DoesNotExist:
			error = 'Stop: Timer has not been started'
	elif ('submit_metrics' in request.POST):
		defect_type = request.POST['defect_type']
		injected_phase = request.POST['injected_phase']
		injected_iteration = request.POST['injected_iteration']
		defect_description = request.POST['defect_description']
		instance = Defect.objects.create(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, defect_description=defect_description, defect_type=defect_type, injected_phase=injected_phase, injected_iteration=injected_iteration)
		instance.save()

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"activity_type": activity_type,
		"activity_status": activity_status,
		"error": error,
		"duration": duration,
	}

	return render(request, "defectsActivity.html", context)

def managementActivity(request):
	b = True

def projectviewmetrics(request):
	project_name = request.session['project_name']
	phase_name=''
	iteration_name=''
	est_sloc = 0
	sloc = 0
	activities = Activity.objects.all()
	projects = Project.objects.all()
	project = ''
	injections=0
	removals=0
	effortperesthours=0
	slocpereffort=0
	injectionspereffort=0
	removalsperefort=0
	defectsyield=0
	injectionsperksloc=0
	effort = 0
	for obj in projects:
		if obj.project_name == project_name:
			project = obj
			est_sloc = obj.estimate_sloc
			sloc = obj.sloc
	average_sloc=sloc_per_est_sloc(sloc, est_sloc)

	for obj in activities:
			if obj.project_name == project_name:
				effort = effort + float(obj.duration)
				if obj.activity_type == 'Development':
					injections = injections + int(obj.defects)
				elif obj.activity_type == 'Defect Removal':
					removals = removals + int(obj.defects)
	effortperesthours = effort_per_est_hours(project.hours, effort)
	slocpereffort = sloc_per_effort(project.sloc, effort)
	injectionspereffort = injections_per_effort(injections, effort)
	removalsperefort = removals_per_effort(removals, effort)
	injectionsperksloc = injections_per_ksloc(injections, effort)
	defectsyield = defect_yield(injections, sloc)

	if (effortperesthours==-1):
		effortperesthours = "Unavailable"
	if (slocpereffort==-1):
		slocpereffort = "Unavailable"
	if (injectionspereffort==-1):
		injectionspereffort = "Unavailable"
	if (removalsperefort==-1):
		removalsperefort = "Unavailable"
	if (injectionsperksloc==-1):
		injectionsperksloc = "Unavailable"
	if (defectsyield==-1):
		defectsyield = "Unavailable"
	print(sloc)
	c={
		"average_sloc":average_sloc,
		"sloc":sloc,
		"effortperesthours":effortperesthours,
		"slocpereffort":slocpereffort,
		"injectionspereffort":injectionspereffort,
		"removalsperefort":removalsperefort,
		"injectionsperksloc":injectionsperksloc,
		"defectsyield":defectsyield,
		"removals":removals,
		"injections":injections,
		"average_sloc":average_sloc,
	}

	return render(request,"calculatemetrics.html",c)

def phaseviewmetrics(request):

	project_name = request.session['project_name']
	phase_name=''
	iteration_name=''
	est_sloc = 0
	sloc = 0
	activities = Activity.objects.all()
	projects = Project.objects.all()
	project = ''
	injections=0
	removals=0
	effortperesthours=0
	slocpereffort=0
	injectionspereffort=0
	removalsperefort=0
	defectsyield=0
	injectionsperksloc=0

	effort = 0
	for obj in projects:
		if obj.project_name == project_name:
			project = obj
			est_sloc = obj.estimate_sloc
			sloc = obj.sloc
	average_sloc=sloc_per_est_sloc(sloc, est_sloc)

	phase_name = request.session['phase_name']
	print ("Project: " + project_name + " Phase: " + phase_name)
	for obj in activities:
		if obj.project_name == project_name and obj.phase_name == phase_name:
			effort = effort + float(obj.duration)
			print("duration is "+(obj.duration))
			if obj.activity_type == 'Development':
				injections = injections + int(obj.defects)
			elif obj.activity_type == 'Defect Removal':
				removals = removals + int(obj.defects)
	effortperesthours = effort_per_est_hours(project.hours, effort)
	slocpereffort = sloc_per_effort(project.sloc, effort)
	injectionspereffort = injections_per_effort(injections, effort)
	removalsperefort = removals_per_effort(removals, effort)
	injectionsperksloc = injections_per_ksloc(injections, effort)
	defectsyield = defect_yield(injections, sloc)

	if (effortperesthours==-1):
		effortperesthours = "Unavailable"
	if (slocpereffort==-1):
		print ("slocpereffort: " + str(slocpereffort))
		slocpereffort = "Unavailable"
	if (injectionspereffort==-1):
		injectionspereffort = "Unavailable"
	if (removalsperefort==-1):
		removalsperefort = "Unavailable"
	if (injectionsperksloc==-1):
		injectionsperksloc = "Unavailable"
	if (defectsyield==-1):
		defectsyield = "Unavailable"
	c={
		"average_sloc":average_sloc,
		"sloc":sloc,
		"effortperesthours":effortperesthours,
		"slocpereffort":slocpereffort,
		"injectionspereffort":injectionspereffort,
		"removalsperefort":removalsperefort,
		"injectionsperksloc":injectionsperksloc,
		"defectsyield":defectsyield,
		"removals":removals,
		"injections":injections,
		"average_sloc":average_sloc,
	}
	return render(request,"calculatemetrics_phases.html",c)

def iterationviewmetrics(request):

	project_name = request.session['project_name']
	phase_name=''
	iteration_name=''
	est_sloc = 0
	sloc = 0
	activities = Activity.objects.all()
	projects = Project.objects.all()
	project = ''
	injections=0
	removals=0
	effortperesthours=0
	slocpereffort=0
	injectionspereffort=0
	removalsperefort=0
	defectsyield=0
	injectionsperksloc=0
	effort = 0
	for obj in projects:
		if obj.project_name == project_name:
			project = obj
			est_sloc = obj.estimate_sloc
			sloc = obj.sloc
	average_sloc=sloc_per_est_sloc(sloc, est_sloc)

	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	for obj in activities:
		if obj.project_name == project_name and obj.phase_name == phase_name and iteration_name == iteration_name:
			effort = effort + int(obj.duration)
		if obj.activity_type == 'Development':
			injections = injections + int(obj.defects)+1
		elif obj.activity_type == 'Defect Removal':
			removals = removals + int(obj.defects)
	effortperesthours = effort_per_est_hours(project.hours, effort)
	slocpereffort = sloc_per_effort(project.sloc, effort)
	injectionspereffort = injections_per_effort(injections, effort)
	removalsperefort = removals_per_effort(removals, effort)
	injectionsperksloc = injections_per_ksloc(injections, effort)
	defectsyield = defect_yield(injections, sloc)

	if (effortperesthours==-1):
		effortperesthours = "Unavailable"
	if (slocpereffort==-1):
		print ("slocpereffort: " + str(slocpereffort))
		slocpereffort = "Unavailable"
	if (injectionspereffort==-1):
		injectionspereffort = "Unavailable"
	if (removalsperefort==-1):
		removalsperefort = "Unavailable"
	if (injectionsperksloc==-1):
		injectionsperksloc = "Unavailable"
	if (defectsyield==-1):
		defectsyield = "Unavailable"

	c={
		"average_sloc":average_sloc,
		"sloc":sloc,
		"effortperesthours":effortperesthours,
		"slocpereffort":slocpereffort,
		"injectionspereffort":injectionspereffort,
		"removalsperefort":removalsperefort,
		"injectionsperksloc":injectionsperksloc,
		"defectsyield":defectsyield,
		"removals":removals,
		"injections":injections,
		"average_sloc":average_sloc,
	}
	return render(request,"calculatemetrics_iteration.html",c)

def sloc_per_est_sloc(sloc, est_sloc):
	if est_sloc is not 0:
		avg = sloc / est_sloc
		return avg
	else:
		return -1

def effort_per_est_hours(est_hours, effort):
	if est_hours is not 0:
		print (est_hours)
		effort = effort / 3600
		average = effort / est_hours * 100
		return average
	else:
		return -1

def sloc_per_effort(sloc, effort):
	print ("effort in function: " + str(effort))
	if effort is not 0:
		effort = effort / 3600
		result = sloc / effort
		print ("slocpereffort in function: " + str(result))
		return result
	else:
		return -1

def injections_per_effort(injections, effort):
	if effort is not 0:
		effort = effort / 3600
		result = injections / effort
		return result
	else:
		return -1

def removals_per_effort(removals, effort):
	if effort is not 0:
		effort = effort / 3600
		result = removals / effort
		return result
	else:
		return -1

def injections_per_ksloc(injections, sloc):
	if sloc is not 0:
		ksloc = sloc / 1000
		result = injections / ksloc
		return result
	else:
		return -1

def defect_yield(injections, removal):
	if injections is not 0:
		result = removal / injections * 100
		return result
	else:
		return -1