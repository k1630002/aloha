from django.conf.urls import url
from views import auth, users, chats

app_name = 'api'
urlpatterns = [
    url(r'^auth/login', auth.login, name='login'),
    url(r'^auth/logout', auth.logout, name='logout'),
    url(r'^auth/register', auth.register, name='register'),
    url(r'^users/', users.list, name='listUsers'),
    url(r'^chats/', chats.chats, name='chats'),
    url(r'^messages/', chats.messages, name='messages'),
]