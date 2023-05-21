from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TextSummarizerSerializer
from .services.summary import Summary


class TextSummarizerView(APIView):
    def post(self, request):
        serializer = TextSummarizerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            instance = Summary()
            summarized_text = instance.get_text_summary(
                data["text"], data["summary_length"]
            )

            return Response(
                data={"summary": summarized_text}, status=status.HTTP_200_OK
            )
