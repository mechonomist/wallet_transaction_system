from django.contrib import admin
from django.urls import path
from wallet_app import views as wallet_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet/', wallet_views.WalletView.as_view()),
    path('wallet/<str:pk>', wallet_views.WalletView.as_view()),
]
