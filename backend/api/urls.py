from django.urls import path
from api import views

urlpatterns = [
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("set_csrf_token/", views.set_csrf_token),
    path("is_authenticated/", views.is_authenticated),
    path("get_user_role/", views.get_user_role),

    path('get_buildings_list/', views.get_buildings),
    path('add_building/', views.create_building),
    path('delete_building/<int:building_id>/', views.delete_building),
    
    path('get_entrances_list/', views.get_entrances),
    path('add_entrance/', views.create_entrance),
    path('delete_entrance/<int:entrance_id>/', views.delete_entrance),

    path('get_apartments_list/', views.get_apartments),
    path('add_apartment/', views.create_apartment),
    path('delete_apartment/<int:apartment_id>/', views.delete_apartment),

    path('add_manager/', views.add_manager),
    path('add_guard/', views.add_guard),
    path('add_inhabitant/', views.add_inhabitant),

    path("delete_user/<int:user_id>/", views.delete_user),
    path('get_users_list/', views.get_users),

    path('manager_buildings/', views.get_manager_buildings),
    path('guard_entrances/', views.get_guard_entrances),
    path('inhabitant_apartments/', views.get_inhabitant_apartment),

]
