from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Redirect
from .serializers import RedirectSerializer


# pylint: disable=too-many-ancestors,no-member
class RedirectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer


def redirect_page(_request, code):
    """get redirect's destination and do a 302 redirect"""
    my_redirect = get_object_or_404(Redirect, code=code)
    my_redirect.visits += 1
    my_redirect.save()
    return redirect(my_redirect.destination)
