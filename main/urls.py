from django.urls import path
from main.views import show_main, create_record, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_one, remove_one, delete_record
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-record', create_record, name='create_record'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_one/<int:record_id>/', add_one, name='add_one'),
    path('remove_one/<int:record_id>/', remove_one, name='remove_one'),
    path('delete_record/<int:record_id>/', delete_record, name='delete_record'),
]
