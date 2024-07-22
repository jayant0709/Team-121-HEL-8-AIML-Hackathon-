from django.urls import path
from . import views

urlpatterns = [
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('home/', views.home, name='home_page'),
    path('thank-you/<int:feedback_id>/', views.thank_you, name='thank_you'),
    path('view-feedback/<int:feedback_id>/', views.view_feedback, name='view_feedback'),
    path('chatbot-api/', views.chatbot_api, name='chatbot_api'),
    path('login/', views.user_login, name='login_page'),
    path('signup/', views.user_signup, name='signup_page'),
    path('', views.user_login, name='home_page'),  # Set login as the default page
    path('start-emotion-detection/', views.start_emotion_detection, name='start_emotion_detection'),
    path('stop-emotion-detection/', views.stop_emotion_detection, name='stop_emotion_detection'),
    path('process_chat_emotions/', views.process_chat_emotions, name='process_chat_emotions'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
