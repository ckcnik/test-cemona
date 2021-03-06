from rest_framework import generics, viewsets, pagination, views
from cemona.models import Modem
from rest_framework.response import Response
from rest_framework import status
# from .serializers import ModemSerializer
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate
# from django.contrib.auth import login
# from django.contrib.sessions.models import Session
# from django.core.urlresolvers import reverse
from rest_framework.decorators import api_view
from .serializers import ModemSerializer, ProbeSerializer
from django.utils.translation import ugettext_lazy as _
from cemona.models import Probe


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


# class PopulationList(generics.ListAPIView):
#     """
#     API endpoint that represents a list of population cities.
#     """
#     queryset = Population.objects.all()
#     serializer_class = PopulationSerializer


class ModemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of modems.
    """
    queryset = Modem.objects.all()
    serializer_class = ModemSerializer
    pagination_class = StandardResultsSetPagination


# class ItemViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that represents a list of items.
#     """
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     pagination_class = StandardResultsSetPagination
#
#
# class AuthView(views.APIView):
#     """
#     Метод авторизации, возвращает редирект с параметром сессии
#     """
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#         login(request, user)
#         redirect_url = ''
#         if user:
#             redirect_url = '{0}?session={1}'.format(request.build_absolute_uri(reverse('set-session')),
#                                                     request.session.session_key)
#         content = {
#             'redirect_url': redirect_url
#         }
#         return Response(content)
#
#
# class LogoutView(views.APIView):
#     """
#     Метод авторизации, возвращает редирект с параметром сессии
#     """
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         session_key = request.POST.get('session')
#
#         try:
#             Session.objects.get(session_key=session_key).delete()
#             status = 'Ok'
#         except Session.DoesNotExist:
#             status = 'error'
#         content = {
#             'status': status
#         }
#         return Response(content)


@api_view(['POST'])
def register_probe(request):
    """
    Gate for registering Probe and other devices (ethernet, wifi, modems)
    :param request:
    :return:
    """
    serial_number = request.data['sn']

    try:
        probe = Probe.objects.get(sn=serial_number)
    except Probe.DoesNotExist:
        probe = None

    # md = []
    # for modem in request.data['modems']:
    #     try:
    #         inst_modem = Modem.objects.get(imei=modem['imei'])
    #     except Modem.DoesNotExist:
    #         inst_modem = None
    #     md.append( inst_modem)
    serializer = ProbeSerializer(probe, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": _("Error probe registering!"), 'more': serializer.errors})
