from myapp import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.login, name='login'), #login
    path('logout/', views.logout, name='logout'), #logout
    # supplier
    path('add_supplier/', views.add_supplier, name="add_supplier"),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('delete_supplier/', views.delete_supplier, name="delete_supplier"),
    # yard
    path('yards/', views.yards, name="yards"), # yards
    path('add_yard/', views.add_yard, name="add_yard"), # add new yard
    # metal
    path('add_metal/', views.add_metal, name="add_metal"),
    path('metals/', views.metals, name="metals"),
    path('delete_metal/', views.delete_metal, name="delete_metal"),
    # cost
    path('add_cost/', views.add_cost, name="add_cost"),
    path('costs/', views.costs, name="costs"),
    path('delete_cost/', views.delete_cost, name="delete_cost"),
    # grade
    path('add_grade/', views.add_grade, name="add_grade"),
    path('grades/', views.grades, name="grades"),
    path('gradenewvalue/', views.gradenewvalue, name="gradenewvalue"),
    path('delete_grade/', views.delete_grade, name="delete_grade"),
    
    path('delete_metal_grade/', views.delete_metal_grade, name="delete_metal_grade"),
    path('delete_metal_overhead/', views.delete_metal_overhead, name="delete_metal_overhead"),
    path('update_metal_grade/', views.update_metal_grade, name="update_metal_grade"),
    path('update_overhead_grade/', views.update_overhead_grade, name="update_overhead_grade"),
    # qualitys
    path('add_quality/', views.add_quality, name="add_quality"),
    path('qualitys/', views.qualitys, name="qualitys"),
    path('delete_quality/', views.delete_quality, name="delete_quality"),
    # actual
    path('add_actual/', views.add_actual, name="add_actual"),
    path('actuals/', views.actuals, name="actuals"),
    path('delete_actual/', views.delete_actual, name="delete_actual"),
    # add_calculation
    path('add_calculation/', views.add_calculation, name="add_calculation"),
    path('calculations/', views.calculations, name="calculations"),
    
    # ajax
    path('ajax/fatch_yard_quality_ajax/', views.fatch_yard_quality_ajax, name="fatch_yard_quality_ajax"),
    path('ajax/fatch_cost/', views.fatch_cost_ajax, name="fatch_cost_ajax"),
    path('ajax/fatch_Supplier/', views.fatch_Supplier_ajax, name="fatch_Supplier_ajax"),
    path('ajax/fatch_grade/', views.fatch_grade_ajax, name="fatch_grade_ajax"),
    path('ajax/fatch_quality_ajax/', views.fatch_quality_ajax, name="fatch_quality_ajax"),
    # ajax Calcu
    path('ajax/fatch_grade_calculator/', views.fatch_grade_calculator, name='fatch_grade_calculator'),
]