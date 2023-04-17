from rest_framework.views import APIView
from django.http import JsonResponse
from ..comment import Comment
from ..serializations import CommentSerializer


# Create your views here.
class SampleSerializationApiView(APIView):
    def get(self, request):
        comment = Comment("truongtronghai@gmail.com", "Focus on goal, not obstacles")
        return JsonResponse({"result": CommentSerializer(comment).data})
