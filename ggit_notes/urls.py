from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import note_detail, note_list

urlpatterns = [
    path('', note_list, name='note-list'),
    path('<int:note_id>/', note_detail, name='note-detail')
]
