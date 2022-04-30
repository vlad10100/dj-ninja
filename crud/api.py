from ninja import NinjaAPI
from typing import List

from django.shortcuts import get_object_or_404

from crud.schema import EmployeeIn, EmployeeOut
from crud.models import Employee, Department


api = NinjaAPI()



# get

# List 
@api.get("employees/", response=List[EmployeeOut])
def all_employees(request):
    all_employees = Employee.objects.all()
    return all_employees


# Detail
@api.get("employees/{employee_id}", response=EmployeeOut)
def detail_employee(request, employee_id:int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee



# post
@api.post("employees/")
def create_employee(request, payload:EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {'id': employee.id}



# put setattr????
@api.put("employee/{employee_id}", response=EmployeeOut)
def update_employee(request, payload:EmployeeIn, employee_id:int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.first_name = payload.first_name
    employee.last_name = payload.last_name
    employee.birthdate = payload.birthdate
    employee.department_id = payload.department_id
    employee.save()
    return 200, employee


# delete
@api.delete("employee/{employee_id}")
def delete_employee(request, employee_id:int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return 200