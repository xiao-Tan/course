from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description, Comment

def index(request):
    context = {
        "all_courses": Course.objects.all()
    }    
    if request.method == "GET":
        return render(request, "courses_app/index.html", context)
    if request.method == "POST":
        new_desc = Description.objects.create(content=request.POST['description'])
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Course.objects.create(name=request.POST['name'], desc=new_desc)
            return redirect('/')

def comment(request,num):
    this_course = Course.objects.get(id=num)
    context = {
        "id": this_course.id,
        "name": this_course.name,
        "all_comment": this_course.comments.all()
    }
    if request.method == "GET":
        return render(request, "courses_app/comment.html", context)
    if request.method == "POST": 
        errors = Comment.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/courses/' + num + '/comment')
        else:
            Comment.objects.create(content=request.POST['comment'], course=this_course)
            return redirect('/courses/' + num + '/comment')

def destory(request,num):
    this_course = Course.objects.get(id=num)
    context = {
        "id": this_course.id,
        "name": this_course.name,
        "description": this_course.desc.content
    }
    return render(request, "courses_app/delete_page.html", context)

def delete(request):
    this_id = request.POST['id_num']
    this_course = Course.objects.get(id=this_id)
    this_course.delete()
    return redirect('/')