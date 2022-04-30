from datetime import date
from ninja import Schema

class EmployeeIn(Schema):
    first_name : str
    last_name : str 
    birthdate : date = None
    department_id : int = None

class EmployeeOut(Schema):
    id : int
    first_name : str
    last_name : str 
    birthdate : date = None
    department_id : int = None
