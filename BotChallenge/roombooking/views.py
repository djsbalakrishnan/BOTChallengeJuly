import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from roombooking.serializers import RoomSerializer
from roombooking.models import Room


# Create your views here.
@csrf_exempt
def web_hook(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.body
        json_data = json.loads(data.decode('utf-8'))
        result = json_data["result"]["parameters"]

        return JsonResponse({
            "displayText": "enter the end time",
            "source": "agent",
        })



