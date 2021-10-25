from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data
        response.data = {}
        errors = []
        for field, value in data.items():
            errors.append("{} : {}".format(field, " ".join(value)))

        response.data['errors'] = errors

        response.data['exception'] = str(exc)

    return response