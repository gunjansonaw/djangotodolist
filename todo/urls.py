from django.urls import path
from  .import views
urlpatterns = [
    path('',views.todo_list,name="todo_list"),
    path('create',views.create_todo,name="create-todo"),
    path('complete/<int:todo_id>',views.complete_todo,name="complete-todo"),
    path('delete/<int:todo_id>',views.delete_todo,name="delete_todo"),
]

