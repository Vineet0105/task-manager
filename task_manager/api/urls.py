from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from accounts.views import *
from rest_framework.routers import DefaultRouter
from tasks.views import *

router = DefaultRouter()
router.register('tasks',TaskViewset,basename='task')


urlpatterns = [
    
    path('',include(router.urls)),
    path('register/',RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]