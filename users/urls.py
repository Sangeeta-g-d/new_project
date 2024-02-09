from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [

     path('index',views.index,name='index'),
     path('login',views.login1,name='login1'),
     path('add_operator',views.add_operator,name='add_operator'),
     path('quality_range',views.quality_range,name='quality_range'),
     path('update_quality/<int:id>',views.update_quality,name='update_quality'),
     path('add_quality',views.add_quality,name='add_quality'),
     path('operator_login',views.operator_login,name='operator_login'),
     path('operators_list',views.operators_list,name='operators_list'),
     path('profile',views.profile,name='profile'),
     path('admin_logout',views.admin_logout,name='admin_logout'),
     path('forgot_password',views.forgot_password,name='forgot_password'),
     path('change_password/<token>',views.change_password,name='change_password'),
     path('operator_logout',views.operator_logout,name='operator_logout'),
     path('delete_operator/<int:pk>/', views.delete_operator, name='delete_operator'),
     path('update_operator/<int:id>', views.update_operator, name='update_operator'),
     path('get_quality_ranges/', views.get_quality_ranges, name='get_quality_ranges'),
     path('update_quote/<int:id>', views.update_quote, name='update_quote'),
     path('operator_dashboard/', views.operator_dashboard, name='operator_dashboard'),
     #path('get_commodities/', views.get_commodities, name='get_commodities'),
     #path('get_agents/', views.get_agents, name='get_agents'),
     path('get_commission_agent/', views.get_commission_agent, name='get_commission_agent'),
     path('get_lot_id/', views.get_lot_id, name='get_lot_id'),
     path('get_details/', views.get_details, name='get_details'),
     path('get_grade_range/', views.get_grade_range, name='get_grade_range'),
     path('applied_tender', views.applied_tender, name='applied_tender'),
     path('operator_tender', views.operator_tender, name='operator_tender'),
     path('submit_row/<int:row_id>/', views.submit_row, name='submit_row'),
     path('submitted_tender', views.submitted_tender, name='submitted_tender'),
     path('run_selenium/',views.run_selenium,name="run_selenium"),
     path('run_selenium_row/',views.run_selenium_row,name="run_selenium_row"),
     #path('check_tender_exists/', views.check_tender_exists, name='check_tender_exists'),
     path('submit_all_rows/',views.submit_all_rows, name='submit_all_rows'),
     path('submit_all_data/',views.submit_all_data, name='submit_all_data')


     ]
