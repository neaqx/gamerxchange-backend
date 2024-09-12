from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def route_route(request):
    return Response({
        'message': 'Welcome to GamerXchange API'
    })