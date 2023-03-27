from django.urls import path,include
from vehicle import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.Home.as_view()),name="home"),
    path('login/',views.Login.as_view(),name="login"),
    path('register/',views.Register.as_view(),name="Register"),
    path('logout/',views.Logout.as_view(),name="logout"),


    path('add-vehicle/',views.Add_Vehicle.as_view(),name="add_vehicle"),
    path('edit-vehicle/',views.Edit_vehicle.as_view(),name="edit_vehicle"),

    path('get-vehicle-details/<int:id>/',login_required(views.get_vehicle_details.as_view()),name="get_vehicle_details"),
    path('delete-vehicle/<int:id>/',views.Delete_Vehicle.as_view(),name="delete_Vehicle")

    
]