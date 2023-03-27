class Get_Ip_Address:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                request.id_address = request.META.get('REMOTE_ADDR')
            except:
                request.id_address = None
        response = self.get_response(request)
        return response