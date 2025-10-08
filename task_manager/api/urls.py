from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from accounts.views import *
from rest_framework.routers import DefaultRouter
from tasks.views import *
from rest_framework_simplejwt.authentication import JWTAuthentication  # JWT Auth
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



router = DefaultRouter()
router.register('tasks',TaskViewset,basename='task')


schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API documentation for the Task Manager project",
        contact=openapi.Contact(email="vineet@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
    authentication_classes=[],
)


urlpatterns = [
    
    path('',include(router.urls)),
    path('register/',RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]