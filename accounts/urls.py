from django.urls import path
from accounts.views import ProfileView, ProfileEditView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]
