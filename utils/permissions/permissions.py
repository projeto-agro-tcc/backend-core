from functools import wraps

from rest_framework import status
from utils.exceptions.catalogo_exceptions import CustomValidation


def authenticated_user(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        if request.request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            raise CustomValidation('Not authenticate', 'detail', status_code=status.HTTP_401_UNAUTHORIZED)
    return wrapper_func


def allowed_users_by_group(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.request.user.groups.exists():
                group = request.request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise CustomValidation('Permission Denied', 'detail', status_code=status.HTTP_401_UNAUTHORIZED)
        return wrapper_func
    return decorator
