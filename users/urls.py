from django.urls import path,include
from django.contrib import auth
from . import views

urlpatterns = [
    path('',views.welcome_faculty,name='teacher-home'),
    path('<int:pk>/profile', views.teacher_profile, name='teacher-profile'),
    path('create/',views.TeacherCreate.as_view(),name='teacher-create'),
    path('<int:pk>/update/',views.TeacherUpdateView.as_view(),name='teacher-update'),
]

urlpatterns += [
    path('<int:pk>/achivements/', include('achivements.urls'))
]