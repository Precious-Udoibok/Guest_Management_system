import logging
import smtplib
from email.message import EmailMessage
from email.utils import formataddr

from app.core.config import settings

logger = logging.getLogger(__name__)


class EmailDeliveryError(RuntimeError):
    """Raised when an email cannot be delivered."""


def send_email_to_user(to_email: str, subject: str, body: str):
    if not settings.EMAILS_ENABLED:
        raise EmailDeliveryError("email delivery is not configured")

    server = None
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = formataddr((settings.EMAILS_FROM_NAME, settings.SMTP_USER))
        msg["To"] = to_email
        msg.set_content(body)

        server = smtplib.SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT)
        if settings.SMTP_TLS:
            server.starttls()  # secure the connection
        server.login(user=settings.SMTP_USER, password=settings.SMTP_PASSWORD)  # login
        server.send_message(from_addr=settings.SMTP_USER, to_addrs=to_email, msg=msg)
        logger.info("Email sent successfully")

    except Exception as exc:
        logger.exception("Failed to send email to %s", to_email)
        raise EmailDeliveryError("email delivery failed") from exc

    finally:
        if server is not None:
            try:
                server.quit()
            except Exception:
                logger.exception("Failed to close the email server connection")
            else:
                logger.info("Connection closed")
