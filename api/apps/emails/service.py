import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.utils.html import format_html
from dynaconf import settings


class EmailService:
    def __init__(self):
        self.environment = settings.ENVIRONMENT
        self.email_test_mode = settings.EMAIL_TEST_MODE
        self.test_email_recipient = settings.TEST_EMAIL_RECIPIENT
        self.smtp_host = settings.EMAIL_HOST
        self.smtp_port = settings.EMAIL_PORT
        self.smtp_user = settings.EMAIL_HOST_USER
        self.smtp_password = settings.EMAIL_HOST_PASSWORD
        self.email_sender = settings.EMAIL_HOST_SENDER
        self.email_use_tls = settings.EMAIL_USE_TLS

    def send_emails(self, email_data_list):
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            if self.email_use_tls:
                server.starttls()
            server.login(self.smtp_user, self.smtp_password)

            for email_data in email_data_list:
                subject = self._prepare_subject(email_data['subject'])
                original_recipients = self._get_original_recipients(email_data['recipients'])
                recipients = self._get_recipients(original_recipients)
                body = self._prepare_body(email_data.get('body', ''), original_recipients)

                self._send_email(server, subject, body, recipients)

    def _prepare_subject(self, subject: str) -> str:
        if self.environment in ['local', 'dev', 'test']:
            return f"[{self.environment.upper()}] {subject}"
        return subject

    def _get_original_recipients(self, recipients: str) -> list:
        return [email.strip() for email in recipients.split(',')]

    def _get_recipients(self, original_recipients: list) -> list:
        if self.email_test_mode:
            return [self.test_email_recipient]
        return original_recipients

    def _prepare_body(self, body: str, original_recipients: list) -> str:
        if self.email_test_mode:
            original_recipients_str = ', '.join(original_recipients)
            test_note = format_html(
                '<p style="color:red;"><strong>Envio de Teste:</strong> Este email seria enviado para: {}</p>',
                original_recipients_str
            )
            return f"{body}\n{test_note}"
        return body

    def _send_email(self, server, subject: str, body: str, recipients: list):
        msg = self._create_message(subject, body, recipients)
        server.sendmail(self.email_sender, recipients, msg.as_string())

    def _create_message(self, subject: str, body: str, recipients: list) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        return msg
