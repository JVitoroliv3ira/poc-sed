from typing import List

from apps.emails.service import EmailService


def send_emails(emails: List[dict]) -> None:
    print(f'Enviando {len(emails)} e-mails...')
    EmailService().send_emails(emails)
    print('E-mails enviados com sucesso.')
