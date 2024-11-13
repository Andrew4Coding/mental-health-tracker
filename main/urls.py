from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_mood_entry, name='create_mood_entry'),
    path('edit/<str:id>/', edit_mood, name='edit_mood'),
    path('delete/<str:id>/', delete_mood, name='delete_mood'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-mood-entry-ajax', add_mood_entry_ajax, name='add_mood_entry_ajax'),
    path('create-flutter/', create_mood_flutter, name='create_mood_flutter'),
]