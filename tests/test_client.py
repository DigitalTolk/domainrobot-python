from domainrobot import Domainrobot
from domainrobot.services.certificate import CertificateService
from domainrobot.services.contact import ContactService
from domainrobot.services.domain import DomainService
from domainrobot.services.domain_studio import DomainStudioService
from domainrobot.services.hello import HelloService
from domainrobot.services.job import JobService
from domainrobot.services.poll import PollService
from domainrobot.services.ssl_contact import SslContactService
from domainrobot.services.transfer_out import TransferOutService
from domainrobot.services.user import UserService
from domainrobot.services.zone import ZoneService
from tests.conftest import BASE_URL


class TestDomainrobotInit:
    def test_services_are_attached(self):
        c = Domainrobot(username="u", password="p", base_url=BASE_URL)
        assert isinstance(c.domain, DomainService)
        assert isinstance(c.contact, ContactService)
        assert isinstance(c.zone, ZoneService)
        assert isinstance(c.certificate, CertificateService)
        assert isinstance(c.ssl_contact, SslContactService)
        assert isinstance(c.poll, PollService)
        assert isinstance(c.transfer_out, TransferOutService)
        assert isinstance(c.job, JobService)
        assert isinstance(c.user, UserService)
        assert isinstance(c.domain_studio, DomainStudioService)
        assert isinstance(c.hello, HelloService)
        c.close()

    def test_context_manager(self):
        with Domainrobot(username="u", password="p", base_url=BASE_URL) as c:
            assert isinstance(c, Domainrobot)
        # After __exit__, client should be closed (no error is sufficient)

    def test_close_is_idempotent(self):
        c = Domainrobot(username="u", password="p", base_url=BASE_URL)
        c.close()
        c.close()  # should not raise
