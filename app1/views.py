from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import Class, Teacher
from .forms import Class_in, Class_se, Teacher_in, Teacher_se

# Create your views here.
def handler400(request, *args, **argv):
    response = render(
        request,
        'app1/400.html',
        {
            'title': "400 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 400
    return response

def handler404(request, *args, **argv):
    response = render(
        request,
        'app1/404.html',
        {
            'title': "404 Not found",
            'year':datetime.now().year,
        }
    )
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(
        request,
        'app1/500.html',
        {
            'title': "500 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 500
    return response

def handler503(request, *args, **argv):
    response = render(
        request,
        'app1/503.html',
        {
            'title': "503 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 503
    return response

def home(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return render(
            request,
            'app1/index.html',
            {
                'title': "Home Page",
                'year':datetime.now().year,
            }
        )

    else:
        messages.error(request, "Login First.")
        return redirect("app1:login")

    

def login_re(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in.")
        return redirect("app1:home")

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("app1:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request,
        "app1/login.html",
        {
            'title': "Registeration Page",
            'year': datetime.now().year,
            'form': form
        }
    )

def logout_request(request):
    assert isinstance(request, HttpRequest)
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("app1:login")

def cla(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Class_se(request.POST)
            if form.is_valid():
                cln = form.cleaned_data['Number']
                cle = form.cleaned_data['Section']
                if Class.objects.filter(Number = cln).filter(Section = cle):     
                    # messages.info(request, f"You are Viewing Time table for: {cln} {cle}")
                    # return HttpResponseRedirect('cla_slug', nu_slug = cln, se_slug = cle)
                    # return redirect('cla_slug', nu_slug = cln, se_slug = cle)
                    return cla_slug(request, cln, cle)
                
                else:
                    messages.error(request, f"No Time table found for: {cln} {cle}")
            else:
                messages.error(request, f"Invalid Entry")
            
        form = Class_se
        return render(
            request,
            "app1/class.html",
            {
                'title': "Class Timetable",
                'year': datetime.now().year,
                'form': form,
                'classes': Class.objects.all,
            }
        )

    else:
        return redirect("app1:login")

def cla_slug(request, nu_slug, se_slug):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        nu_slug = int(nu_slug)
        cl = Class.objects.get(Number=nu_slug, Section=se_slug)
        messages.info(request, f"You are Viewing Time table for: {nu_slug} {se_slug}")
        return render(
            request,
            "app1/class_sp.html",
            {
                'title': "Class Timetable for " + str(cl.Number) + " " + cl.Section,
                'year': datetime.now().year,
                'class': cl,
            }
        )

    else:
        return redirect("app1:login")

def cla_in(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Class_in(request.POST)
            if form.is_valid():
                cln = form.cleaned_data['Number']
                cle = form.cleaned_data['Section']
                form.save()
                messages.success(request, f"New Time table created for: {cln} {cle}")
                return redirect("app1:home")
            else:
                messages.error(request, f"Invalid Entry")
        
        form = Class_in
        return render(
            request,
            "app1/class_in.html",
            {
                'title': "Insert a new Class",
                'year': datetime.now().year,
                'class': form,
            }
        )

    else:
        return redirect("app1:login")

def cla_del(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Class_se(request.POST)
            if form.is_valid():
                cln = form.cleaned_data['Number']
                cle = form.cleaned_data['Section']
                if Class.objects.filter(Number = cln).filter(Section = cle):     
                    messages.success(request, f"You have deleted Time table for: {cln} {cle}")
                    Class.objects.filter(Number = cln).filter(Section = cle).delete()
                    # ob = Class.objects.get(Number = cln)
                    # ob = ob.get(Section = cle)
                    # ob.delete()
                    return redirect("app1:home")
                
                else:
                    messages.error(request, f"No Time table found for: {cln} {cle}")
            else:
                messages.error(request, f"Invalid Entry")
            
        form = Class_se
        messages.warning(request, f"You will permenantly delete a class using this page")
        return render(
            request,
            "app1/class_del.html",
            {
                'title': "Delete Class Timetable",
                'year': datetime.now().year,
                'form': form,
                'classes': Class.objects.all,
            }
        )

    else:
        return redirect("app1:login")

def cla_edit_slug(request, nu_slug, se_slug):
    assert isinstance(request, HttpRequest)
    nu_slug = int(nu_slug)
    cl = Class.objects.get(Number=nu_slug, Section=se_slug)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Class_in(request.POST, instance = cl)
            if form.is_valid():
                cln = form.cleaned_data['Number']
                cle = form.cleaned_data['Section']
                form.save()
                messages.success(request, f"Updated Time table created for: {cln} {cle}")
                return cla_slug(request, cln, cle)
            else:
                messages.error(request, f"Invalid Entry")
        
        form = Class_in(instance = cl)
        return render(
            request,
            "app1/class_up.html",
            {
                'title': "Edit a new Class",
                'year': datetime.now().year,
                'class': form,
            }
        )

    else:
        return redirect("app1:login")

def cla_all(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        cl = Class.objects.all()
        messages.info(request, f"You are Viewing Time table for all classes")
        return render(
            request,
            "app1/class_all.html",
            {
                'title': "Class Timetable for all classes",
                'year': datetime.now().year,
                'classes': cl,
            }
        )

    else:
        return redirect("app1:login")

def teacher_in(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Teacher_in(request.POST)
            if form.is_valid():
                fn = form.cleaned_data['First_Name']
                ln = form.cleaned_data['Last_Name']
                form.save()
                t = Teacher.objects.get(First_Name = fn, Last_Name = ln)
                messages.success(request, f"Created Time table created for: {fn} {ln}")
                return add_class_slug(request, t.id)
            else:
                messages.error(request, f"Invalid Entry")
        
        form = Teacher_in()
        return render(
            request,
            "app1/teacher_in.html",
            {
                'title': "Insert a new Teacher",
                'year': datetime.now().year,
                'teacher': form,
            }
        )

    else:
        return redirect("app1:login")

def add_class(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Teacher_se(request.POST)
            if form.is_valid():
                fn = form.cleaned_data['First_Name']
                ln = form.cleaned_data['Last_Name']
                t = Teacher.objects.get(First_Name = fn, Last_Name = ln)
                messages.success(request, f"Adding classes to the teacher: {fn} {ln}")
                return add_class_slug(request, t.id)
            else:
                messages.error(request, f"Invalid Entry")
        
        form = Teacher_se()
        teach = Teacher.objects.all()
        return render(
            request,
            "app1/add_class.html",
            {
                'title': "Add a Class to a Teacher",
                'year': datetime.now().year,
                'form': form,
                'teachers': teach,
            }
        )

    else:
        return redirect("app1:login")

def add_class_slug(request, slug):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if Teacher.objects.filter(id=slug):
            t = Teacher.objects.get(id=slug)
            if request.method == "POST":
                form = Class_se(request.POST)
                if form.is_valid():
                    n = form.cleaned_data['Number']
                    s = form.cleaned_data['Section']
                    c = Class.objects.get(Number = n, Section = s)
                    t.classes.add(c)
                    messages.success(request, f"Added class {n} {s} to the teacher {t.First_Name} {t.Last_Name}")
                    return redirect("app1:add_class_slug", slug = t.id)
                else:
                    messages.error(request, f"Invalid Entry")
        
            form = Class_se()
            clas = Class.objects.all()
            return render(
                request,
                "app1/add_class_slug.html",
                {
                    'title': t.First_Name + " " + t.Last_Name,
                    'year': datetime.now().year,
                    'form': form,
                    'teach': t,
                    'classes': clas,
                }
            )

        messages.error(request, f"Teacher not found")
        return redirect("app1:add_class")

    else:
        return redirect("app1:login")

def teacher(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Teacher_se(request.POST)
            if form.is_valid():
                fn = form.cleaned_data['First_Name']
                ln = form.cleaned_data['Last_Name']
                if Teacher.objects.filter(First_Name = fn).filter(Last_Name = ln):
                    t = Teacher.objects.get(First_Name = fn, Last_Name = ln)
                    # messages.info(request, f"You are Viewing Time table for: {cln} {cle}")
                    # return HttpResponseRedirect('cla_slug', nu_slug = cln, se_slug = cle)
                    # return redirect('cla_slug', nu_slug = cln, se_slug = cle)
                    return teacher_slug(request, t.id)
                
                else:
                    messages.error(request, f"No Time table found for: {fn} {ln}")
            else:
                messages.error(request, f"Invalid Entry")
            
        form = Teacher_se
        return render(
            request,
            "app1/teacher.html",
            {
                'title': "Teacher Timetable",
                'year': datetime.now().year,
                'form': form,
                'classes': Teacher.objects.all,
            }
        )

    else:
        return redirect("app1:login")

def teacher_slug(request, slug):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        cl = Teacher.objects.get(id=slug)
        cl.create_timetable(Class.objects.all())
        messages.info(request, f"You are Viewing Time table for: {cl.First_Name} {cl.Last_Name}")
        return render(
            request,
            "app1/teacher_sp.html",
            {
                'title': cl.First_Name + " " + cl.Last_Name,
                'year': datetime.now().year,
                'class': cl,
            }
        )

    else:
        return redirect("app1:login")

def teacher_del(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Teacher_se(request.POST)
            if form.is_valid():
                fn = form.cleaned_data['First_Name']
                ln = form.cleaned_data['Last_Name']
                if Teacher.objects.filter(First_Name = fn).filter(Last_Name = ln):     
                    messages.success(request, f"You have deleted Time table for: {fn} {ln}")
                    Teacher.objects.filter(First_Name = fn).filter(Last_Name = ln).delete()
                    # ob = Class.objects.get(Number = cln)
                    # ob = ob.get(Section = cle)
                    # ob.delete()
                    return redirect("app1:home")
                
                else:
                    messages.error(request, f"No Time table found for: {fn} {ln}")
            else:
                messages.error(request, f"Invalid Entry")
            
        form = Teacher_se
        messages.warning(request, f"You will permenantly delete a teacher using this page")
        return render(
            request,
            "app1/teacher_del.html",
            {
                'title': "Delete Teacher Timetable",
                'year': datetime.now().year,
                'form': form,
                'classes': Teacher.objects.all,
            }
        )

    else:
        return redirect("app1:login")

def teacher_up(request, slug):
    assert isinstance(request, HttpRequest)
    cl = Teacher.objects.get(id = slug)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Teacher_in(request.POST, instance = cl)
            if form.is_valid():
                fn = form.cleaned_data['First_Name']
                ln = form.cleaned_data['Last_Name']
                form.save()
                messages.success(request, f"Updated Time table for: {fn} {ln}")
                return teacher_slug(request, slug)
            else:
                messages.error(request, f"Invalid Entry")
        
        form = Teacher_in(instance = cl)
        return render(
            request,
            "app1/teacher_up.html",
            {
                'title': "Edit a new Class",
                'year': datetime.now().year,
                'class': form,
            }
        )

    else:
        return redirect("app1:login")

def teacher_all(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        cl = Teacher.objects.all()
        messages.info(request, f"You are Viewing Time table for all teachers")
        return render(
            request,
            "app1/teacher_all.html",
            {
                'title': "Class Timetable for all Teachers",
                'year': datetime.now().year,
                'classes': cl,
            }
        )

    else:
        return redirect("app1:login")

def user_info(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return render(
            request,
            "app1/user.html",
            {
                'title': request.user.first_name + " " + request.user.last_name,
                'year': datetime.now().year,
            }
        )

    else:
        return redirect("app1:login")