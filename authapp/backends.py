from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.hashers import check_password
from authapp.models import CustomUser

class CaseInsensitiveModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(username__iexact=username)
            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            return None
