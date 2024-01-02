from django.urls import path
from books_app.views import Home_View,Books_Apiview,GenerateVideoAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('', Home_View.as_view(),name="home"),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name="obtain_token"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),


    path('api/books/',Books_Apiview.as_view(),name="books"),
    path('api/books/<int:pk>/',Books_Apiview.as_view(),name="books"),

    path('api/generate/',GenerateVideoAPIView.as_view(),name="generate_video")

]