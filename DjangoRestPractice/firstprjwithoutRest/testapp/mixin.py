from django.http import HttpResponse


class HttpResponseMixin(object):
    def rendertoHttpResponse(self, json_data):
        return HttpResponse(json_data, content_type='application/json')