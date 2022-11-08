from emp_api.viewsets import EmployeeViews
from rest_framework import routers

router=routers.DefaultRouter() 
router.register('employee',EmployeeViews)

#PUT POST GET DELETE
