from rest_framework.views import APIView, Response, Request, status
from rest_framework.pagination import PageNumberPagination
from .models import Room
from .serializers import RoomSerializer

class GeneralRoomview(APIView):
    def get(self, request: Request) -> Response:
        rooms = Room.objects.all()
        result_page = self.paginate_queryset(rooms, request, view=self)
        serializer = RoomSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
    
    # def post(self, request: Request) -> Response:
    #     serializer = RoomSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status.HTTP_201_CREATED)
    
class SpecificRoomView(APIView):
    def get(self, request: Request, room_id: int) -> Response:
        ...
    
    def post(self, request: Request, room_id: int) -> Response:
        ...
    
    def patch(self, request: Request, room_id: int) -> Response:
        ...
    
    def delete(self, request: Request, room_id: int) -> Response:
        ... 
