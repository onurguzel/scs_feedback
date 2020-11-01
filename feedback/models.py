from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ("Feedback", "Request", "User")


class User(models.Model):
    team_id = models.CharField(_("Team Id"), max_length=50)
    user_id = models.CharField(_("User Id"), max_length=50)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Request(models.Model):
    sender = models.ForeignKey(
        User,
        related_name="requests",
        on_delete=models.CASCADE,
        verbose_name=_("Request by"),
    )
    recipients = models.ManyToManyField(
        User, related_name="received_requests", verbose_name=_("Requested from")
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Request")
        verbose_name_plural = _("Requests")

    def __str__(self):
        return f"FeedbackRequest #{self.id}"


class Feedback(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Author"),
        related_name="sent_feedbacks",
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Recipient"),
        related_name="received_feedbacks",
    )
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        verbose_name=_("Feedback Request"),
        related_name="feedbacks",
        blank=True,
        null=True,
    )
    start_doing = models.TextField(_("Start doing"))
    continue_doing = models.TextField(_("Continue doing"))
    stop_doing = models.TextField(_("Stop doing"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")