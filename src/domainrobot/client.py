from __future__ import annotations

from typing import Any

from ._http import HttpClient
from .services.account import AccountService
from .services.backup_mx import BackupMxService
from .services.certificate import CertificateService
from .services.contact import ContactService
from .services.domain import DomainService
from .services.domain_studio import DomainStudioService
from .services.hello import HelloService
from .services.job import JobService
from .services.mail_proxy import MailProxyService
from .services.poll import PollService
from .services.redirect import RedirectService
from .services.session import SessionService
from .services.ssl_contact import SslContactService
from .services.subscription import SubscriptionService
from .services.transfer_out import TransferOutService
from .services.user import UserService
from .services.zone import ZoneService

DEFAULT_BASE_URL = "https://api.autodns.com/v1"


class Domainrobot:
    """Main client for the Domainrobot JSON API.

    Usage::

        client = Domainrobot(username="user", password="pass", context=4)
        result = client.domain.info("example.com")
        print(result.data)
    """

    def __init__(
        self,
        username: str,
        password: str,
        *,
        context: int | None = None,
        base_url: str = DEFAULT_BASE_URL,
        default_headers: dict[str, str] | None = None,
        timeout: float = 30.0,
    ) -> None:
        self._http = HttpClient(
            base_url=base_url,
            username=username,
            password=password,
            context=context,
            default_headers=default_headers,
            timeout=timeout,
        )

        self.account = AccountService(self._http)
        self.backup_mx = BackupMxService(self._http)
        self.certificate = CertificateService(self._http)
        self.contact = ContactService(self._http)
        self.domain = DomainService(self._http)
        self.domain_studio = DomainStudioService(self._http)
        self.hello = HelloService(self._http)
        self.job = JobService(self._http)
        self.mail_proxy = MailProxyService(self._http)
        self.poll = PollService(self._http)
        self.redirect = RedirectService(self._http)
        self.session = SessionService(self._http)
        self.ssl_contact = SslContactService(self._http)
        self.subscription = SubscriptionService(self._http)
        self.transfer_out = TransferOutService(self._http)
        self.user = UserService(self._http)
        self.zone = ZoneService(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> Domainrobot:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
