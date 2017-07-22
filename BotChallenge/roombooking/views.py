from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from roombooking.serializers import RoomSerializer
from roombooking.models import Room


# Create your views here.
@csrf_exempt
def web_hook(request):
    if request.method == 'GET':
        snippets = Room.objects.all()
        serializer = RoomSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)