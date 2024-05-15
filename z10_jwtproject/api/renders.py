from rest_framework import renderers
import json
"""
in frontend error cant  identify with correct error mess through seriaizer.error,
so to customize the error message we need to create a custom renderer.
its not complusary to customize the error mess
"""
class UserRender(renderers.JSONRenderer):
    charset ='utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        "in serializer.error 'ErrorDetail', string is present"
        response=''
        if 'ErrorDetail' in str(data):
            response= json.dumps({'error':data})
        else:
            response=json.dumps(data)
        return response