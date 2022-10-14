from django.urls import path
from . import views

# urlpatterns = [
#     path('orders/', views.model_list('Order')),
#     path('models/', views.model_list('CarModel')),
#     path('colors/', views.model_list('Color')),
#     path('brands/', views.model_list('CarBrand')),
#
#
#     path('orders/<int:pk>/', views.model_detail('Order')),
#     path('models/<int:pk>/', views.model_detail('CarModel')),
#     path('colors/<int:pk>/', views.model_detail('Color')),
#     path('brands/<int:pk>/', views.model_detail('CarBrand')),
#
# ]

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('models/', views.CarModelList.as_view()),
    path('colors/', views.ColorList.as_view()),
    path('brands/', views.CarBrandList.as_view()),


    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    path('models/<int:pk>/', views.CarModelDetail.as_view()),
    path('colors/<int:pk>/', views.ColorDetail.as_view()),
    path('brands/<int:pk>/', views.CarBrandDetail.as_view()),

    path('colors-quantity/', views.ColorQuantity.as_view()),
    path('brands-quantity/', views.BrandsQuantity.as_view()),

]
