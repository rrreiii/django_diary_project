from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.Index.as_view(), name='index'), #/diary
    path('add/', views.AddView.as_view(), name='add'), #/diary/add
    path('update/<int:pk>', views.update,name='update'), #/diary/update/100
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail')
]
