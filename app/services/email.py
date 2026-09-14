import logging
import resend

from app.core.config import settings

logger = logging.getLogger(__name__)


class EmailDeliveryError(RuntimeError):
    """Raised when an email cannot be delivered."""


def send_email_to_user(to_email: str, subject: str, body: str):
    if not settings.EMAILS_ENABLED:
        raise EmailDeliveryError("email delivery is not configured")

    try:
        resend.api_key = settings.RESEND_API_KEY

        resend.Emails.send(
            {
                "from": settings.EMAILS_FROM_EMAIL,
                "to": [to_email],
                "subject": subject,
                "text": body,
            }
        )

        logger.info("Email sent successfully to %s", to_email)

    except Exception as exc:
        logger.exception("Failed to send email to %s", to_email)
        raise EmailDeliveryError("Email delivery failed") from exc
