from rest_framework.routers import SimpleRouter
from api.viewsets.userviewset import UserViewSet, RegisterViewSet, LoginViewSet

route = SimpleRouter()
route.register('users', UserViewSet, basename="Users")
route.register('auth/register', RegisterViewSet, basename="register", )
route.register('auth/login', LoginViewSet, basename="login")

urlpatterns = route.urls

