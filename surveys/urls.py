from django.urls import path
from . import views


urlpatterns =[
    path('survey-workspace/', views.SurveysAPIVIEW.as_view()),
    path('generate-workspace-form/', views.generate_block_at_start),
    
    path('survey-blocks/<str:id>/', views.get_survey_details),
    path('block-actions/', views.SurveyBlocks.as_view()),
    path('change-block-to-preferred/<str:survey_id>/', views.change_block_to_preferred)
]
