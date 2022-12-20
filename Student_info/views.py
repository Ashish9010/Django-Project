from django.shortcuts import render
from Student_info.models import Student_info,Admission,marks,Stu_Feedback
# Create your views here.

def view_Student(request):
    stu1=Student_info.objects.all()
    
    
    return render(request,'Student.html',{'s':stu1})

def view_Admission(request):
    Addm=Admission.objects.all()
    
    return render(request,'Admiss.html',{'ad':Addm})

def view_Marks(request):
    mar=marks.objects.all()
    
    return render(request,'Total_marks.html',{'mk':mar})

def view_Feedback(request):
    feed=Stu_Feedback.objects.all()
    
    return render(request,'Feedback.html',{'fd':feed})

def view_home(request):
        return render(request,'home.html')

def view_navi(request):
    if request.method=='POST':
        Studentname = request.POST.get('Studentname')
        RegNO = request.POST.get('RegNO')
        image = request.POST.get('image')
        address = request.POST.get('address')
        Taluka = request.POST.get('Taluka')
        District = request.POST.get('District')
        pincode = request.POST.get('pincode')

        student = Student_info (
            Studentname = Studentname,
            RegNO=RegNO,
            image=image,
            address=address,
            Taluka=Taluka,
            District=District,
            pincode=pincode

        )
        student.save()
        return render(request,'reg.html',{'title':f"Hello {Studentname}, You have successfully registered"})

    return render(request,'navi.html')

def view_eg(request):
        return render(request,'eg.html')        

def view_data(request):
        return render(request,'data.html')     
