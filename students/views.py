from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from .forms import StudentsForm

# Create your views here.


def test(request):
   return render(request, 'pages/index.html')

def student (request):
  students = Student.objects.all()
  return render(request, 'pages/add-student.html', {'Data': students})

def manage_students(request):
  students = Student.objects.all()
  return render(request, 'pages/manage-students.html', {'stu': students})



def add_student(request):
  print("test")
  if request.method == 'POST':
    fm = StudentsForm(request.POST)
    students = Student.objects.all()
    
    if fm.is_valid():
      fn  = fm.cleaned_data['firstname']
      ln  = fm.cleaned_data['lastname']
      em  = fm.cleaned_data['email']
      ag  = fm.cleaned_data['age']
      ge  = fm.cleaned_data['gender']
      r_student  = Student(first_name=fn, last_name=ln,email= em, age = ag, gender=ge)
      r_student.save()
    else:
      error = "please fill all field"
      return render(request, 'pages/add-student.html', {'error': error, 'Data': students})
    return render(request, 'pages/add-student.html', {'Data': students})

def delete(request, id):
  Student.objects.filter(id=id).delete()
  return redirect("/")




def edit(request, id):
  if id:
    info = Student.objects.get(id=id)
    return render(request, "pages/edit-student.html", context={'info': info})

def update(request, id):
    info = Student.objects.get(id=id)
    stu = StudentsForm(request.POST, instance = info)
    if stu.is_valid():  
        stu.save()  
        return redirect("/student")


def filter(request):

  stu = Student.objects.all()
  if  'up' or 'down' or 'age' or 'firstname' or 'lastname' or 'email' or 'male' or 'female' in request.POST:
        # fetch all data form database
    stu = Student.objects.all()
        #------>custom search<---------
        # ----->define variables<------
    up         = request.POST.get('up', False)
    down       = request.POST.get('down', False)
    age        = request.POST.get('age', False)
    firstname  = request.POST.get('firstname', False)
    lastname   = request.POST.get('lastname', False)
    email      = request.POST.get('email', False)
    male       = request.POST.get('male', False)
    female     = request.POST.get('female', False)

     # ===================filter age proparties with gender  =====================#

    if age and (up or down) and (male or female):

      # ===================filter age more than with gender  =====================#
      if age and up:
        ff2 =Student.objects.filter(age__gte= age )

        if male and female:
          return render(request, 'pages/manage-students.html',{'stu': ff2})


        if male or female:
          if female:
            ff =ff2.filter(gender= female )
            return render(request, 'pages/manage-students.html',{'stu': ff})
        
          if male:
            ff =ff2.filter(gender= male )
            return render(request, 'pages/manage-students.html',{'stu': ff})
            

    # ===================filter age less than with gender  =====================#
    if age and down:
      ff1 =Student.objects.filter(age__lte = age )
    
      
      if male and female:
        return render(request, 'pages/manage-students.html',{'stu': ff1})

      if male or female:
        if male :
          ff =ff1.filter(gender= male )
          return render(request, 'pages/manage-students.html',{'stu': ff})

        if female:
          ff =ff1.filter(gender= female )
          return render(request, 'pages/manage-students.html',{'stu': ff})


   # ===================filter age with gender  =====================#
    if age:
      ff3 =Student.objects.filter(age= age )
      return render(request, 'pages/manage-students.html',{'stu': ff3})

    
      if male and female:
        return render(request, 'pages/manage-students.html',{'stu': ff3})
      if male or female:
        if male :
          ff =ff3.filter(gender= male )
          return render(request, 'pages/manage-students.html',{'stu': ff})


        if female:
          ff =ff3.filter(gender= female )
          return render(request, 'pages/manage-students.html',{'stu': ff})



    # ===================filter name with gender =====================#
    if firstname and lastname and (female or male):
      ff1 =Student.objects.filter(first_name__startswith= firstname )
      ff2 =ff1.filter(last_name__startswith= lastname )
      if male and female:
        return render(request, 'pages/manage-students.html',{'stu': ff2})

      if male :
        ff =ff2.filter(gender= male )
        return render(request, 'pages/manage-students.html',{'stu': ff})
        print(male)
      if female:
        ff =ff2.filter(gender= female )
        return render(request, 'pages/manage-students.html',{'stu': ff})
        print(female)


    # ===================filter firstname with lastname =====================#
    if firstname and lastname:
      ff1 =Student.objects.filter(first_name__startswith= firstname )
      ff =ff1.filter(last_name__startswith= lastname )
      return render(request, 'pages/manage-students.html',{'stu': ff})


    # ===================filter each field =====================#
    if firstname:
      ff =Student.objects.filter(first_name__startswith= firstname )
      return render(request, 'pages/manage-students.html',{'stu': ff})
     
    if lastname:
      ff =Student.objects.filter(last_name__startswith= lastname )
      return render(request, 'pages/manage-students.html',{'stu': ff})
      print(s)

    if email:
      ff =Student.objects.filter(email__startswith= email )
      return render(request, 'pages/manage-students.html',{'stu': ff})
  
    # ===================filter age with proparties =====================#
    if age and up:
      ff =Student.objects.filter(age__gte= age )
      return render(request, 'pages/manage-students.html',{'stu': ff})

    if age and down:
      ff =Student.objects.filter(age__lte = age )
      return render(request, 'pages/manage-students.html',{'stu': ff})

    if age:
      ff =Student.objects.filter(age= age )
      return render(request, 'pages/manage-students.html',{'stu': ff})


    # ===================filter gender =====================#
    if male and female:
        ff =Student.objects.all()
        return render(request, 'pages/manage-students.html',{'stu': ff})
    if male or female:
      if male :
        ff =Student.objects.filter(gender= male )
        return render(request, 'pages/manage-students.html',{'stu': ff})
        print(male)
      if female:
        ff =Student.objects.filter(gender= female )
        return render(request, 'pages/manage-students.html',{'stu': ff})
        print(female)
      
    
  return render(request, 'pages/manage-students.html',{'stu': stu})