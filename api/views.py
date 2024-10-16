import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.generate_text import generate_text
from rest_framework.decorators import api_view
from django.http import StreamingHttpResponse

@api_view(['POST'])
def text_gen(request):
    text_input = request.data.get('text_input')

    # Check if text input is provided
    if not text_input:
        return StreamingHttpResponse("Error: input cannot be empty", status=400)

    # Generator function for streaming tokens
    def stream_response():
        for token in generate_text(text_input):  
            yield token

    return StreamingHttpResponse(stream_response(), content_type="application/json")