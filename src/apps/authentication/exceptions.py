from rest_framework.exceptions import APIException


class DuplicateUsernameException(APIException):
    status_code = 400
    default_code = 'duplicate_username'
    default_detail = 'User with this username already exist'
