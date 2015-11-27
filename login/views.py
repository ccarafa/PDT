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
from projects.models import Project, ProjectsDeveloper, Phase, Iteration, Activity

# Create your views here.

def developerphases(request):
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
        instance = Phase.objects.create(project_name=project_name, phase_name="Inception")
        instance.save()
        instance = Phase.objects.create(project_name=project_name, phase_name="Elaboration")
        instance.save()
        instance = Phase.objects.create(project_name=project_name, phase_name="Construction")
        instance.save()
        instance = Phase.objects.create(project_name=project_name, phase_name="Transition")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Inception", iteration_name="Iteration 1")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Elaboration", iteration_name="Iteration 1")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Elaboration", iteration_name="Iteration 2")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Construction", iteration_name="Iteration 1")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Construction", iteration_name="Iteration 2")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Construction", iteration_name="Iteration 3")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Transition", iteration_name="Iteration 1")
        instance.save()
        instance = Iteration.objects.create(project_name=project_name, phase_name="Transition", iteration_name="Iteration 2")
        instance.save()
    
        context = {
            "projects": projects,
            "name": request.session['name'],
        }
        return render(request, "manager.html", context)
    return render(request, "addprojectsform.html", {})

def projectpage(request):
    for name in request.POST:
        if name != "csrfmiddlewaretoken":
            request.session['project_name'] = name
    return render(request, "projectpage.html", {})

def projectbuttons(request):
    for instance in Project.objects.all():
        if instance.project_name == request.session['project_name']:
            if 'open' in request.POST:
                instance.is_open = True
                instance.save()
                return render(request, "open.html", {})
            if 'close' in request.POST:
                instance.is_open = False
                instance.save()
                return render(request, "close.html", {})
            if 'phases' in request.POST:
                return render(request, "phases.html", {})
            if 'add_developers' in request.POST:
                return render(request, "add_developer.html", {})
            if 'metrics' in request.POST:
                return projectviewmetrics(request)
            if 'closesubmit' in request.POST:
                instance.sloc = request.POST.get('sloc')
                instance.save()
    return render(request, "projectpage.html", {})

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
    instance = ProjectsDeveloper.objects.create(developer_name=developer_name, project_name=request.session['project_name'])
    instance.save()
    return render(request, "add_message.html", {})

def add_message(request):
    return render(request, "add_message.html", {})

def phase(request):
    if 'inception' in request.POST:
        request.session['phase_name'] = "Inception"
    if 'elaboration' in request.POST:
        request.session['phase_name'] = "Elaboration"
    if 'construction' in request.POST:
        request.session['phase_name'] = "Construction"
    if 'transition' in request.POST:
        request.session['phase_name'] = "Transition"
    if 'viewmetrics' in request.POST:
        return phaseviewmetrics(request)
    for instance in Phase.objects.all():
        if instance.project_name == request.session['project_name'] and instance.phase_name == request.session['phase_name']:
            if 'open' in request.POST:
                instance.is_open = True
                instance.save()
            if 'close' in request.POST:
                instance.is_open = False
                instance.save()
            if 'iterations' in request.POST:
                if instance.phase_name == "Elaboration":
                    return render(request, "elaboration_iteration.html", {})
                elif instance.phase_name == "Inception":
                    return render(request, "inception_iteration.html", {})
                elif instance.phase_name == "Construction":
                    return render(request, "construction_iteration.html", {})
                elif instance.phase_name == "Transition":
                    return render(request, "transition_iteration.html", {})
            if 'metrics' in request.POST:
                return phaseviewmetrics(request)
    return render(request, "phasespage.html", {})

def iteration(request):
    if 'Iteration1' in request.POST:
        request.session['iteration_name'] = "Iteration 1"
    if 'Iteration2' in request.POST:
        request.session['iteration_name'] = "Iteration 2"
    if 'Iteration3' in request.POST:
        request.session['iteration_name'] = "Iteration 3"
    if 'open' in request.POST:
        for instance in Iteration.objects.all():
            if(instance.project_name == request.session['project_name'] and 
                instance.phase_name == request.session['phase_name'] and 
                instance.iteration_name == request.session['iteration_name']):
                instance.is_open = True
                instance.save()
    if 'close' in request.POST:
        for instance in Iteration.objects.all():
            if(instance.project_name == request.session['project_name'] and 
                instance.phase_name == request.session['phase_name'] and 
                instance.iteration_name == request.session['iteration_name']):
                instance.is_open = False
                instance.save()
    if 'metrics' in request.POST:
        return phaseviewmetrics(request)
    return render(request, "iterationphase.html", {})

def activityDashboard(request):
    if request.POST.get("Iteration 1"):
        request.session['iteration_name']="Iteration 1"
    elif request.POST.get("Iteration 2"):
        request.session['iteration_name']="Iteration 2"
    elif request.POST.get("Iteration 3"):
        request.session['iteration_name']="Iteration 3"
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
    elif ('defects' in request.POST):
        activity_type = 'Defect Removal'
        request.session['activity_type'] = activity_type
        url = reverse('activity')
        return HttpResponseRedirect(url)
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
				effort = effort + int(float(obj.duration))
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
	for obj in activities:
		if obj.project_name == project_name and obj.phase_name == phase_name:
			effort = effort + int(obj.duration)
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

def sloc_per_est_sloc(sloc, est_sloc):
    avg = sloc / est_sloc
    return avg

def effort_per_est_hours(est_hours, effort):
	average = effort / est_hours * 100
	return average

def sloc_per_effort(sloc, effort):
	result = sloc / effort
	return result

def injections_per_effort(injections, effort):
	result = injections / effort
	return result

def removals_per_effort(removals, effort):
	result = removals / effort
	return result

def injections_per_ksloc(injections, sloc):
	ksloc = sloc / 1000
	result = injections / ksloc
	return result

def defect_yield(injections, removal):
	result = removal / injections * 100
	return result