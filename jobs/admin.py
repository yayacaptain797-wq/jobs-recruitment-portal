from django.contrib import admin
from django.utils.html import format_html

from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "location",
        "job_type",
        "application_deadline",
        "is_active",
    )

    list_filter = (
        "job_type",
        "is_active",
        "application_deadline",
    )

    search_fields = (
        "title",
        "company",
        "location",
        "description",
        "requirements",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "phone",
        "address",
        "job",
        "applied_at",
    )

    list_filter = (
        "job",
        "applied_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "address",
        "job__title",
        "job__company",
    )

    ordering = (
        "-applied_at",
    )
def admin_dashboard(request):

    total_jobs = Job.objects.count()
    active_jobs = Job.objects.filter(is_active=True).count()
    total_applications = Application.objects.count()

    recent_applications = Application.objects.select_related(
        "job"
    ).order_by("-applied_at")[:5]

    return render(
        request,
        "jobs/admin_dashboard.html",
        {
            "total_jobs": total_jobs,
            "active_jobs": active_jobs,
            "total_applications": total_applications,
            "recent_applications": recent_applications,
        },
    )