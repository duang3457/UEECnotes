# 中间件，暂时未导入到setting.py中
class GetUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)

        response = self.get_response(request)

        self.process_response(request, response)

        return response

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass