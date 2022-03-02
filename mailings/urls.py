from django.urls import path

from .api import ClientCreateView
from .api import ClientGetView
from .api import ClientDeleteView
from .api import ClientsListView
from .api import ClientUpdateView
from .api import MailingCreateView
from .api import MailingGetView
from .api import MailingDeleteView
from .api import MailingsListView
from .api import MailingUpdateView


urlpatterns = [
    path('client/add/', ClientCreateView.as_view()),
    path('client/get/<int:pk>', ClientGetView.as_view()),
    path('client/delete/<int:pk>', ClientDeleteView.as_view()),
    path('clients/', ClientsListView.as_view()),
    path('client/update/<int:pk>', ClientUpdateView.as_view()),
    path('mailing/add/', MailingCreateView.as_view()),
    path('mailing/get/<int:pk>', MailingGetView.as_view()),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view()),
    path('mailings/', MailingsListView.as_view()),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view()),    
]
