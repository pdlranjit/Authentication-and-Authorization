from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.BookList,name='booklist')
    # path('',views.Newlist,name='newlist')
    path('',views.tasklist,name='name_tasks'),
    path('<int:pk>/',views.Taskdetail,name='task_detail'),
    path('<int:pk>/delete/',views.TaskDelete,name='task_delete')
]
