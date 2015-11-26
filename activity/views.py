from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from time import time

from .models import Activity

# Create your views here.

def activityDashboard(request):
	request.session['project_name'] = 'one'
	request.session['phase_name'] = 'elaboration'
	request.session['iteration_name'] = 'one'
	request.session['username'] = 'frank'
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	username = request.session['username']
	shit = 'Nothing'
	if ('development' in request.POST):
		activity_type = 'Development'
		request.session['activity_type'] = activity_type
		url = reverse('activity')
		return HttpResponseRedirect(url)
		# return render(request, "Activity.html", context)
	elif ('defects' in request.POST):
		activity_type = 'Defect Removal'
		request.session['activity_type'] = activity_type
		url = reverse('activity')
		return HttpResponseRedirect(url)
		# return render(request, "Activity.html", context)
	elif ('management' in request.POST):
		activity_type = 'Management'
		request.session['activity_type'] = activity_type
		url = reverse('activity')
		return HttpResponseRedirect(url)

	context = {
		"project_name": project_name,
		"phase_name": phase_name,
		"iteration_name": iteration_name,
		"username": username,
		"shit": shit,
	}
	return render(request, "ActivityDashboard.html", context)

def activity(request):
	project_name = request.session['project_name']
	phase_name = request.session['phase_name']
	iteration_name = request.session['iteration_name']
	username = request.session['username']
	activity_type = request.session['activity_type']
	# print (activity_type)
	activity_status = 'N/A'
	sloc = 'N/A'
	defects = 'N/A'
	duration = 'N/A'
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
	try:
		instance = Activity.objects.get(project_name=project_name, phase_name=phase_name, iteration_name=iteration_name, username=username, activity_type=activity_type)
		activity_status = str(instance.is_open)
		sloc = str(instance.sloc)
		defects = str(instance.defects)
		duration = str(instance.duration)

	except Activity.DoesNotExist:
		error = 'No error'
		
	if ('start' in request.POST):
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

