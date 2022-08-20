from django.urls import path, include
from crud.api.views import data_view, update_data_view, send_data_view, data_delete

app_name = 'account'

urlpatterns = [
    path('create/', send_data_view),
    path('read/', data_view),
    path('update/<int:pk>', update_data_view),
    path('delete/<int:pk>', data_delete)
]



