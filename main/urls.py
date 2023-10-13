from django.urls import path
from main.views import show_main, create_record, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, delete_record, edit_record, add_record_ajax, get_record_json
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
    path('edit-record/<int:id>', edit_record, name='edit_record'),
    path('delete/<int:id>', delete_record, name='delete_record'),
    # path('photo/<str:nama_file_photo>', get_photo, name='get_photo'),
    path('create-record-ajax/', add_record_ajax, name='add_record_ajax'),
    path('get-record/', get_record_json, name='get_record_json'),
]
