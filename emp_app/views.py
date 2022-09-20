from nis import cat
from django.shortcuts import render,redirect
from .models import Employee, Department, Role
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages


def index(request):
    # return HttpResponse("Hello Gohil")
    return render(request,'index.html')

def all_emp(request):    
    employee = Employee.objects.all()
    context = {
        'obj_list' : employee
    }
    return render(request,'all_emp.html', context)

def add_emp(request):    
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['department'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']     
        # try:
        emp_new = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,hire_date=hire_date, dept_id=dept, role_id=role)       
        emp_new.save()
        # except Exception as e:
        #     print('%s' % type(e))
        # return render(request,'add_emp.html')
        return HttpResponse("Record Added successfully <br/> <a class='btn btn-primary' href='/all-emp'> Go Back To List </a> <br/><br/> <a href='/add-emp'> Add Onther Record</a>")
    else:
        dept = Department.objects.all()
        role = Role.objects.all()
        context = {
        'obj_dept' : dept,
        'obj_role' : role
        }
        return render(request,'add_emp.html', context)

def update_emp(request, emp_id=None):  
    if emp_id and request.method=='GET':      
        emp = Employee.objects.get(id=emp_id)
        dept = Department.objects.all()
        role = Role.objects.all()
        context = {
        'obj_list' : emp,
        'obj_dept' : dept,
        'obj_role' : role
        }
        return render(request,'update_emp.html',context)
    elif request.method=='POST':        
        emp = Employee.objects.get(pk=emp_id)
        emp.first_name = request.POST['first_name']
        emp.last_name = request.POST['last_name']        
        emp.dept.id = int(request.POST['department'])
        emp.role.id = int(request.POST['role'])
        emp.salary = int(request.POST['salary'])
        emp.bonus = int(request.POST['bonus'])
        emp.phone = int(request.POST['phone'])
        emp.hire_date = request.POST['hire_date']     
        emp.save()     
        messages.success(request, 'Employee details updated successfully.')  
        return redirect('/all-emp') 
    else:
        return render(request,'all_emp.html')

def delete_emp(request, emp_id=None):  
    if emp_id:
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()  
            messages.info(request, 'Record Deleted Successfully')
            return redirect('/all-emp')
        except:
            print("Not deleted employee details")
    return render(request,'all_emp.html')

def filter_emp(request):  
    if request.GET.get('name') or request.GET.get('role'):
        employee_data = Employee.objects.all()        
        name = request.GET.get('name',None)
        role = request.GET.get('role',None)
        employee_data = employee_data.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        employee_data = employee_data.filter(Q(role__name__icontains=role))
        context = {
        'obj_list' : employee_data
        }
        return render(request,'filter_emp.html', context) 
        
    employee = Employee.objects.all()
    context = {
        'obj_list' : employee
    }
    return render(request,'filter_emp.html', context)    
    
