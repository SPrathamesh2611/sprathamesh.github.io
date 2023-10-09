from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from django.core.files.storage import FileSystemStorage
from .models import Project
from .forms import ProjectForm,ContactForm,LoginForm

# from PIL import Image
# from io import BytesIO
# from django.core.files.base import ContentFile 


	




# Create your views here.
# def index(request):
#     # Query the database to fetch the skills
#     skills = Skill.objects.all()  # You can adjust this query as needed

#     # Pass the skills to the template context
#     context = {'skills': skills}
    
#     return render(request, 'index.html', context)

a = False


def add_skills(request):
    if request.method == "POST":
        name = request.POST['name']
        level = request.POST['Level']
        image = request.FILES.get('image')
        
        

        
        
        
        skills = Skill(name=name, level=level)
        if image:
            
            
            # Save the image to the file system or database
            fs = FileSystemStorage(location='media/skills_logo/')
            unique_filename = f'{name}_logo.png'  # Use a unique filename
            # filename = fs.save(unique_filename, ContentFile(buffer.getvalue()))
            filename = fs.save(unique_filename,image)

            
            skills.logo = f'skills_logo/{filename}'  # Store the relative path in the database
            #skills.logo = image
        skills.save()
        alert = True
        #return render(request, "add_skills.html", {'alert': alert,'context':data},) 
    
    data = Skill.objects.all()
    context = {
        'data' : data
    }
    return render(request,'add_skills.html',{'context':data})

def base(request):
    # Query the database to fetch the skills
    data = Skill.objects.all()
    context = {
        'data' : data
    }
    projects = Project.objects.all()

    return render(request, 'base.html', { 'context':data, 'projects': projects})
def index(request):
    global a
    data = Skill.objects.all()
    context = {
        'data' : data
    }
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new ContactMessage instance and save it to the database
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact_message.save()
            if a==True:
                return render(request, 'index.html', {'a':a,'form': ContactForm(),'context':data, 'projects': projects, 'success_message': 'Your message has been sent successfully.'})
            else:
                return render(request, 'index.html', {'form': ContactForm(),'context':data, 'projects': projects, 'success_message': 'Your message has been sent successfully.'})
    else:
        form = ContactForm()
        a=False
    return render(request, 'index.html', {'a':a,'context':data, 'projects': projects,'form': form})
    #return render(request,"index.html", context,projects)

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Create a new ContactMessage instance and save it to the database
#             contact_message = ContactMessage(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 subject=form.cleaned_data['subject'],
#                 message=form.cleaned_data['message']
#             )
#             contact_message.save()

#             # Optionally, you can send an email notification here

#             # Redirect back to the contact page with a success message
#             return render(request, 'contact_form.html', {'form': ContactForm(), 'success_message': 'Your message has been sent successfully.'})
#     else:
#         form = ContactForm()

#     return render(request, 'contact_form.html', {'form': form})


# def add_project(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Save the form data to the database
#             project = form.save(commit=False)
#             skills = []
#             for key, value in request.POST.items():
#                 if key.startswith('skill') and value:
#                     skills.append(value)
#             project.skills = ' | '.join(skills)
#             project.save()
#             return redirect('add_project')  # Redirect to the same page after adding

#     else:
#         form = ProjectForm()

#     # Query all saved projects from the database
#     projects = Project.objects.all()
#     data = Skill.objects.all()
#     context = {
#         'data' : data
#     }

#     return render(request, 'add_project.html', {'form': form, 'projects': projects, 'context':data})



def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            project = form.save(commit=False)

            # Retrieve the selected skills from the form
            selected_skills = request.POST.getlist('selected_skills')
            project.skills = ' | '.join(selected_skills)

            project.save()

            return redirect('add_project')  # Redirect to the same page after adding

    else:
        form = ProjectForm()

    # Query all saved projects from the database
    projects = Project.objects.all()
    data = Skill.objects.all()

    context = {
        'form': form,
        'projects': projects,
        'context': data,
    }

    return render(request, 'add_project.html', context)


# def create_project(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('project_list')  # Redirect to the project list view after creating a project
#     else:
#         form = ProjectForm()
#     return render(request, 'myapp/create_project.html', {'form': form})


def custom_login(request):
    global a
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the provided credentials are for a superuser
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                a=True
                # Redirect to a success page or dashboard for superusers
                result = index(request)  # Call view1 from view2
                return result

            else:
                form.add_error(None, 'Invalid username or password for superuser.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# def project_info(request):
#     projects = Project.objects.all()
#     return render(request, 'project_info.html',{'projects': projects,})

def project_info(request, card_name):
    # Retrieve the card data from the database based on the card name
    card = get_object_or_404(Project, name=card_name)

    context = {
        'card': card,
    }

    return render(request, 'project_info.html', context)

def tryes(request):
    return render(request,'tryes.html')