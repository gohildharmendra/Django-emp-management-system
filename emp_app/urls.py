from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.all_emp, name='index'),
    path('all-emp',views.all_emp, name='all_emp'),
    path('add-emp',views.add_emp, name='add_emp'),
    path('delete-emp/<int:emp_id>',views.delete_emp, name='delete_emp'),
    path('update-emp/<int:emp_id>',views.update_emp, name='update_emp'),
    path('filter-emp',views.filter_emp, name='filter_emp'),
    
]
