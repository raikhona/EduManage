from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('adminsignup', views.admin_signup),
    path('studentsignup', views.student_signup,name='studentsignup'),
    path('teachersignup', views.teacher_signup),

    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='school/teacherlogin.html')),
    path('logout', LogoutView.as_view(template_name='school/index.html'), name='logout'),

    path('adminclick', views.adminclick),
    path('teacherclick', views.teacherclick),
    path('studentclick', views.studentclick),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('accounts/profile/', views.afterlogin_view, name='unnamed_bag'),

    path('admin-teacher', views.admin_teacher_view, name='admin-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view, name='admin-add-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view, name='admin-view-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view, name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view, name='approve-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view, name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>', views.delete_teacher_from_school_view, name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>', views.update_teacher_view, name='update-teacher'),

    path('admin-student', views.admin_student_view, name='admin-student'),
    path('admin-add-student', views.admin_add_student_view, name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view, name='admin-view-student'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view, name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view, name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view, name='admin-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view, name='approve-student'),

    path('teacher-dashboard', views.teacher_dashboard_view, name='teacher-dashboard'),
    path('teacher-notice', views.teacher_notice_view, name='teacher-notice'),
    path('student-dashboard', views.student_dashboard_view, name='student-dashboard'),
]
