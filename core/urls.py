from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('create/', views.createSurvey, name='survey-create-view'),

    path('', views.listSurvey, name='survey-list-view'),
    path('<int:pk>/', views.viewSurvey, name='survey-detail-view'),
    path('<int:pk>/edit/', views.editSurvey, name='survey-edit-view'),
    path('<int:pk>/delete/', views.deleteSurvey, name='survey-delete-view'),

    path('<int:pk>/edit/field/text/', views.textField, name='add-text-field-view'),
    path('<int:pk>/edit/field/password/', views.passwordField, name='add-password-field-view'),
    path('<int:pk>/edit/field/email/', views.emailField, name='add-email-field-view'),
    path('<int:pk>/edit/field/telephone/', views.telephoneField, name='add-telephone-field-view'),
    path('<int:pk>/edit/field/textarea/', views.textAreaField, name='add-textarea-field-view'),
    path('<int:pk>/edit/field/number/', views.numberField, name='add-number-field-view'),
    path('<int:pk>/edit/field/range/', views.rangeField, name='add-range-field-view'),
    path('<int:pk>/edit/field/checkbox/', views.checkBoxField, name='add-checkbox-field-view'),
    path('<int:pk>/edit/field/radio/', views.radioField, name='add-radio-field-view'),
    path('<int:pk>/edit/field/select/', views.selectField, name='add-select-field-view'),
    path('<int:pk>/edit/field/date/', views.dateField, name='add-date-field-view'),
    path('<int:pk>/edit/field/month/', views.monthField, name='add-month-field-view'),
    path('<int:pk>/edit/field/time/', views.timeField, name='add-time-field-view'),
    path('<int:pk>/edit/field/datetime/', views.dateTimeField, name='add-datetime-field-view'),
]
