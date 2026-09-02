from email.message import EmailMessage
import smtplib
import logging
from email.utils import formataddr

from app.core.config import settings

logger = logging.getLogger(__name__)


def send_email_to_user(to_email: str, subject: str, body: str):
    if not settings.EMAILS_ENABLED:
        raise RuntimeError("no provided configuration for email variables")

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

    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        raise

    finally:
        if server is not None:
            server.quit()
            logger.info("Connection closed")
