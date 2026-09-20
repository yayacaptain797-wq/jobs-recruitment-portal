from django.urls import path

from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("job/<int:job_id>/", views.job_detail, name="job_detail"),
    path("job/<int:job_id>/apply/", views.apply_job, name="apply_job"),

    path(
        "application-success/",
        views.application_success,
        name="application_success",
    ),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard",
    ),
]