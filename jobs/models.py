from django.db import models


class Job(models.Model):

    JOB_TYPES = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Contract", "Contract"),
        ("Internship", "Internship"),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.CharField(max_length=100, blank=True)
    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPES
    )
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.company}"


class Application(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(
        max_length=300,
        blank=True
    )
    cover_letter = models.TextField()

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"