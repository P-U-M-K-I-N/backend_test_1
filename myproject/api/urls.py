from django.urls import path, include
from . import views

# Path CRUD
urlpatterns = [
    path('todo-create/', views.todoCreate, name='create-data'),
    path('todo-read/', views.todoRead, name='read-all-data'),
    path('todo-updates/<str:pk>', views.todoUpdate, name='update-data'),
    path('todo-delete/<str:pk>', views.todoDelete, name='delete-data'),
]