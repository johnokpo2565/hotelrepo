from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import Http404

class CustomUserManager(BaseUserManager):

    def get_object_by_public_id(self, public_id):
        
        try:
            instance = self.get(public_id=public_id)
            return instance
        except ObjectDoesNotExist:
            raise Http404("User does not exist")
        except (ValidationError, ValueError, TypeError):
            raise Http404("Invalid user")
        
    
    def create_user(self, email, first_name, last_name, password=None, **extrafields):
        
        if email is None:
            raise ValueError('email is required')
        if first_name is None:
            raise ValueError('first name is required')
        if last_name is None:
            raise ValueError('last name is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extrafields)
        user.set_password(password)
        user.save(using=self._db)

    
    def create_superuser(self, email, first_name, last_name, password=None, **extrafields):
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_active", True)
        return self.create_user(email=email, first_name=first_name, last_name=last_name, 
                         password=password,
                                 **extrafields)

       