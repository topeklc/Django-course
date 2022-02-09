from django.shortcuts import render
from django.http import HttpResponse


projectslist = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where i buit out my portfolio.'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am stll working'
    }
]


def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectslist}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectslist:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
