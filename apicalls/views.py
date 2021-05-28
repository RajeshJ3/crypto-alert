from rest_framework import views, permissions, status, response
import requests


class APICall(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        query_params = request.query_params

        method = query_params.get("method", None)
        url = query_params.get("url", None)

        if method == 'post' or method == 'POST':
            resp = requests.post(url=url)
        else:
            resp = requests.get(url=url)

        return response.Response(resp.json(), status.HTTP_200_OK)
