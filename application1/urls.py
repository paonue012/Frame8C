from django.urls import path
from application1.views import (
    ruta_nueva_view,
    about_view,
    home_view,
    contact_view,
    add_student,
    update_student,
    delete_student,
    all_students,
    book_view
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', LoginView.as_view(template_name="base.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', home_view, name='home_view'),
    path('ruta-nueva/', ruta_nueva_view, name='ruta_nueva'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
    path('add-student/', add_student, name='add_student'),
    path('update-student/<int:student_id>/', update_student, name='update_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'),
    path('all-students/', all_students, name='all_students'),
    path('book/', book_view, name='book_view'),
]

