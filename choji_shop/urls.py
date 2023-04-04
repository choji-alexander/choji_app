from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view),
    path('product_detail/<int:my_id>', views.product_detail_view),
    path('product_addition/', views.product_add_view),
    path('product_detail/<int:my_id>/delete/', views.product_delete_view),
    path('product_detail/<int:my_id>/update/', views.product_update_view),

]
