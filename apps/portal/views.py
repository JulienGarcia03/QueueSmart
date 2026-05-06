from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.operations.models import QueueEntry, Service
from apps.users.models import Notification
class PortalView(LoginRequiredMixin, TemplateView):
    """Customer portal dashboard view."""
    login_url = "login"
    template_name = "pages/portal_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        names = {self.request.user.username}
        full_name = self.request.user.get_full_name().strip()
        if full_name:
            names.add(full_name)

        current_entry = QueueEntry.objects.filter(
            user_name__in=names,
            status=QueueEntry.Status.WAITING,
        ).select_related("queue__service").order_by("joined_at", "id").first()

        notifications = Notification.objects.filter(
            recipient_name__in=names,
        ).order_by("-created_at", "-id")

        context["current_entry"] = current_entry
        context["estimated_wait"] = (
            (current_entry.position - 1) * current_entry.queue.service.expected_duration
            if current_entry
            else None
        )
        context["active_services"] = Service.objects.all()
        context["recent_notifications"] = notifications[:3]
        return context

class ServiceTicketFormView(TemplateView):
    """Service Ticket Form view."""
    template_name = 'pages/service_ticket_form.html'


class ServiceTicketDetailsView(TemplateView):
    """Service Ticket Details view."""
    template_name = 'pages/service_ticket_details.html'

class ServiceTicketCancellationFormView(TemplateView):
    """Service Ticket Cancellation Form view."""
    template_name = 'pages/service_ticket_cancellation_form.html'
