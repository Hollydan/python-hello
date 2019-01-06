
from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.do_map), 
    path('who/', views.who),
    # str int slug uuid path
    path('who1/<str:name>/<str:age>/', views.who1),
    path('home/<str:new_type>', views.home)
]
