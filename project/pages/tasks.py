from project.celery import app
from .models import Page


@app.task()
def increase_page_counters(page_id):
    """Increase page and blocks counters."""
    page = Page.objects.filter(id=page_id).first()
    if page:
        page.increase_counters()
