def get_client_ip(request):
    """
    Method gets request and use it to get user ip
    :param request: Request from view
    :return: str - ip address of client
    """

    a = request.META.get('HTTP_X_FORWARDED_FOR')
    if a:
        ip = a.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return str(ip)
