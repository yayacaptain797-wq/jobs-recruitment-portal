from django.shortcuts import render, get_object_or_404, redirect

from .models import Job, Application
from .forms import ApplicationForm


def home(request):

    jobs = Job.objects.filter(is_active=True).order_by("-created_at")

    query = request.GET.get("q")
    job_type = request.GET.get("job_type")

    if query:
        jobs = jobs.filter(
            title__icontains=query
        ) | jobs.filter(
            company__icontains=query
        ) | jobs.filter(
            location__icontains=query
        ) | jobs.filter(
            job_type__icontains=query
        )

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    return render(request, "jobs/home.html", {
        "jobs": jobs,
        "query": query,
        "job_type": job_type,
        "job_types": Job.JOB_TYPES,
    })


def job_detail(request, job_id):

    job = get_object_or_404(Job, id=job_id, is_active=True)

    return render(request, "jobs/job_detail.html", {"job": job})


def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id, is_active=True)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()

            return redirect("application_success")

    else:
        form = ApplicationForm()

    return render(
        request,
        "jobs/apply.html",
        {
            "job": job,
            "form": form,
        },
    )


def application_success(request):

    return render(request, "jobs/success.html")
def admin_dashboard(request):

    total_jobs = Job.objects.count()
    active_jobs = Job.objects.filter(is_active=True).count()
    inactive_jobs = Job.objects.filter(is_active=False).count()
    total_applications = Application.objects.count()

    query = request.GET.get("q", "").strip()

    recent_applications = Application.objects.select_related(
        "job"
    ).order_by("-applied_at")

    if query:
        recent_applications = recent_applications.filter(
            full_name__icontains=query
        ) | recent_applications.filter(
            email__icontains=query
        ) | recent_applications.filter(
            job__title__icontains=query
        )

    recent_applications = recent_applications[:5]

    return render(
        request,
        "jobs/admin_dashboard.html",
        {
            "total_jobs": total_jobs,
            "active_jobs": active_jobs,
            "inactive_jobs": inactive_jobs,
            "total_applications": total_applications,
            "recent_applications": recent_applications,
            "query": query,
        },
    )