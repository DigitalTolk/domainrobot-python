import datetime

from domainrobot.models import (
    Account,
    BackupMx,
    Certificate,
    CertificateData,
    Contact,
    Domain,
    DomainCancelation,
    DomainEnvelope,
    DomainRestore,
    Job,
    MailProxy,
    Model,
    ObjectJob,
    PollMessage,
    Redirect,
    Subscription,
    SslContact,
    TransferOut,
    User,
    Zone,
)


class TestModelFromDict:
    def test_known_fields_set_as_attributes(self):
        d = Domain.from_dict({"name": "example.com", "registryStatus": "ACTIVE"})
        assert d.name == "example.com"
        assert d.registryStatus == "ACTIVE"

    def test_unknown_fields_go_to_extra(self):
        d = Domain.from_dict({"name": "example.com", "someFutureField": 42})
        assert d.name == "example.com"
        assert d.extra == {"someFutureField": 42}

    def test_missing_fields_default_to_none(self):
        d = Domain.from_dict({"name": "example.com"})
        assert d.expire is None
        assert d.ownerc is None
        assert d.dnssec is None

    def test_empty_dict_all_none(self):
        d = Domain.from_dict({})
        assert d.name is None
        assert d.extra == {}

    def test_extra_not_in_repr(self):
        d = Domain.from_dict({"name": "example.com", "unknown": "val"})
        r = repr(d)
        assert "unknown" not in r
        assert "example.com" in r


class TestAllModelsFromDict:
    """Ensure every model can round-trip from_dict without error."""

    def test_account(self):
        a = Account.from_dict({"currentAccountBalance": 100.0, "currency": "EUR"})
        assert a.currentAccountBalance == 100.0
        assert a.currency == "EUR"

    def test_backup_mx(self):
        b = BackupMx.from_dict({"domain": "example.com"})
        assert b.domain == "example.com"

    def test_certificate(self):
        c = Certificate.from_dict({"id": 1, "product": "BASIC_SSL", "name": "example.com"})
        assert c.id == 1
        assert c.product == "BASIC_SSL"

    def test_certificate_data(self):
        c = CertificateData.from_dict({"plain": "CSR...", "keySize": 2048})
        assert c.keySize == 2048

    def test_contact(self):
        c = Contact.from_dict({"id": 1, "fname": "John", "lname": "Doe", "type": "PERSON"})
        assert c.fname == "John"
        assert c.type == "PERSON"

    def test_domain(self):
        d = Domain.from_dict({"name": "example.com", "expire": "2026-01-01"})
        assert d.name == "example.com"

    def test_domain_cancelation(self):
        dc = DomainCancelation.from_dict({"domain": "example.com", "type": "DELETE"})
        assert dc.type == "DELETE"

    def test_domain_envelope(self):
        de = DomainEnvelope.from_dict({"domain": "example.com", "tld": "com", "source": "INITIAL"})
        assert de.tld == "com"

    def test_domain_restore(self):
        dr = DomainRestore.from_dict({"name": "example.com", "deleted": "2025-01-01"})
        assert dr.deleted == "2025-01-01"

    def test_job(self):
        j = Job.from_dict({"id": 123, "status": "RUNNING", "action": "create"})
        assert j.status == "RUNNING"

    def test_mail_proxy(self):
        m = MailProxy.from_dict({"domain": "example.com", "target": "mail.example.com"})
        assert m.target == "mail.example.com"

    def test_object_job(self):
        oj = ObjectJob.from_dict({"job": {"id": 1}, "object": {"type": "domain"}})
        assert oj.job == {"id": 1}

    def test_poll_message(self):
        p = PollMessage.from_dict({"id": 999, "stid": "stid-1"})
        assert p.id == 999

    def test_redirect(self):
        r = Redirect.from_dict({"source": "www.example.com", "target": "example.com", "mode": "HTTP"})
        assert r.mode == "HTTP"

    def test_ssl_contact(self):
        s = SslContact.from_dict({"id": 1, "fname": "John", "email": "j@example.com"})
        assert s.email == "j@example.com"

    def test_subscription(self):
        s = Subscription.from_dict({"id": 42, "status": "ACTIVE", "articleLabel": "backup_mx"})
        assert s.articleLabel == "backup_mx"

    def test_transfer_out(self):
        t = TransferOut.from_dict({"domain": "example.com", "gainingRegistrar": "REG-X"})
        assert t.gainingRegistrar == "REG-X"

    def test_user(self):
        u = User.from_dict({"user": "admin", "context": 4, "authType": "PASSWORD"})
        assert u.user == "admin"
        assert u.context == 4

    def test_zone(self):
        z = Zone.from_dict({
            "origin": "example.com",
            "virtualNameServer": "ns1.autodns.com",
            "resourceRecords": [{"name": "www", "type": "A", "value": "1.2.3.4"}],
        })
        assert z.origin == "example.com"
        assert z.resourceRecords is not None
        assert len(z.resourceRecords) == 1


class TestDatetimeParsing:
    def test_iso_datetime_with_timezone(self):
        d = Domain.from_dict({"created": "2024-01-15T10:30:00.000+0000"})
        assert isinstance(d.created, datetime.datetime)
        assert d.created.year == 2024
        assert d.created.month == 1
        assert d.created.day == 15

    def test_iso_datetime_without_millis(self):
        d = Domain.from_dict({"expire": "2026-06-15T00:00:00+0000"})
        assert isinstance(d.expire, datetime.datetime)
        assert d.expire.year == 2026

    def test_iso_datetime_without_timezone(self):
        d = Domain.from_dict({"updated": "2024-06-15T12:00:00"})
        assert isinstance(d.updated, datetime.datetime)
        assert d.updated.hour == 12

    def test_none_stays_none(self):
        d = Domain.from_dict({"expire": None})
        assert d.expire is None

    def test_missing_stays_none(self):
        d = Domain.from_dict({})
        assert d.created is None

    def test_non_datetime_fields_unaffected(self):
        d = Domain.from_dict({"name": "example.com", "dnssec": True})
        assert d.name == "example.com"
        assert d.dnssec is True

    def test_multiple_datetime_fields(self):
        d = Domain.from_dict({
            "created": "2024-01-01T00:00:00.000+0000",
            "updated": "2024-06-15T00:00:00.000+0000",
            "expire": "2026-01-01T00:00:00.000+0000",
            "domainCreated": "2024-01-01T00:00:00.000+0000",
        })
        assert isinstance(d.created, datetime.datetime)
        assert isinstance(d.updated, datetime.datetime)
        assert isinstance(d.expire, datetime.datetime)
        assert isinstance(d.domainCreated, datetime.datetime)

    def test_transfer_out_dates(self):
        t = TransferOut.from_dict({
            "start": "2024-06-01T00:00:00.000+0000",
            "end": "2024-06-10T00:00:00.000+0000",
        })
        assert isinstance(t.start, datetime.datetime)
        assert isinstance(t.end, datetime.datetime)

    def test_job_execution_datetime(self):
        j = Job.from_dict({"execution": "2024-01-01T00:00:01.000+0000"})
        assert isinstance(j.execution, datetime.datetime)


class TestModelInheritance:
    def test_all_models_extend_model(self):
        for cls in [
            Account, BackupMx, Certificate, CertificateData, Contact, Domain,
            DomainCancelation, DomainEnvelope, DomainRestore, Job, MailProxy,
            ObjectJob, PollMessage, Redirect, Subscription, SslContact,
            TransferOut, User, Zone,
        ]:
            assert issubclass(cls, Model)
