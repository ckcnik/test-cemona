from django.conf.urls import include, url
from django.contrib import admin
# from .views import set_session
from .api_views import ModemViewSet


modem_list = ModemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
modem_detail = ModemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# item_list = ItemViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# item_detail = ItemViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

urlpatterns = [
    # url(r'^stat/$', ModemViewSet.as_view(), name='population'),
    # категории
    url(r'^modem/$', modem_list, name='modems'),
    url(r'^modem/(?P<pk>[0-9]+)/$', modem_detail, name='modem-detail'),
    # url(r'^api/category/(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),
    # товары
    # url(r'^api/item/$', item_list, name='items'),
    # url(r'^api/item/(?P<pk>[0-9]+)/$', item_detail, name='item_detail'),
    # Аутентификация
    # url(r'^set-session/$', set_session, name='set-session'),
    # url(r'^api/login/$', AuthView.as_view(), name='login'),
    # url(r'^api/logout/$', LogoutView.as_view(), name='logout'),
]
