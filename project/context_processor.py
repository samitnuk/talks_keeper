def tk_processor(request):
    PORTAL_URL = request.scheme + '://' + request.get_host()
    return {'PORTAL_URL': PORTAL_URL}
