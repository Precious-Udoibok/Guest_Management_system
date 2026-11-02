import logging
import httpx


from app.core.config import settings

logger = logging.getLogger(__name__)


class EmailDeliveryError(RuntimeError):
    """Raised when an email cannot be delivered."""


def send_email_to_user(to_email: str, subject: str, body: str):
    if not settings.EMAILS_ENABLED:
        raise EmailDeliveryError("email delivery is not configured")

    try:
        response = httpx.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "api-key": settings.BREVO_API_KEY,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json={
                "sender": {
                    "name": settings.EMAILS_FROM_NAME,
                    "email": settings.EMAILS_FROM_EMAIL,
                },
                "to": [{"email": to_email}],
                "subject": subject,
                "textContent": body,
            },
            timeout=10,
        )
        response.raise_for_status()
        logger.info("Email sent successfully")

    except Exception as exc:
        logger.exception("Failed to send email to %s", to_email)
        raise EmailDeliveryError("Email delivery failed") from exc
