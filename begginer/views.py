from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Project
from .forms  import ProjectForm

# projectsList=[
#     {
#         'id':'1',
#         'title':'E-commerce Website',
#         'description':'Full functional e commerce Website',
#         'topRated':True,
#     },
#     {
#         'id':'2',
#         'title':'Portfolio Website',
#         'description':'A person website to write articles ',
#         'topRated':False,
#     },
#     {
#         'id':'3',
#         'title':'Social Network',
#         'description':'An open source Project built by the community',
#         'topRated':True,
#     }
# ]



def projects(request): 
    projects = Project.objects.all()
    print('PROJECTS:',projects)
  
    context = {'projects':projects}
    return render(request, 'begginer/begin.html' , context)

def project(request, pk):
    ##projectObject = None
   ## for i in projectsList:
     ##   if i['id'] == str(pk):
      ##      projectObject = i
    projectObj =Project.objects.get(id=pk)
    tags= projectObj.tags.all()
    reviews=projectObj.reviews.all()
    context={'project':projectObj, 'tags':tags , 'reviews':reviews}
    return render(request,'begginer/best.html',context)

def createProject(request):
    form =ProjectForm()
    
    if request.method =='POST':
         form =ProjectForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('projects')
    context={'form':form}
    return render(request, 'begginer/project-form.html',context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method =='POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context={'form':form}
    return render(request,'begginer/project-form.html',context)

def deleteProject(request , pk):
    project = Project.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('projects')
    return render(request, 'begginer/delete.html',{'object':project})