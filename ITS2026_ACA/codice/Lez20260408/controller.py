from employee_dao import Impiegato, EmployeeDao
import json
dao = EmployeeDao()

print(json.dumps(dao.findImpiegati()))