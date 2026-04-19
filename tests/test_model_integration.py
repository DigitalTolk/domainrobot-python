"""Verify that service methods return typed model instances."""

import httpx

from domainrobot.models import (
    Certificate,
    Contact,
    Domain,
    DomainCancelation,
    Job,
    ObjectJob,
    PollMessage,
    SslContact,
    User,
    Zone,
)
from tests.conftest import SUCCESSFUL_RESPONSE


DOMAIN_RESPONSE = {
    "stid": "stid-1",
    "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
    "data": [{"name": "example.com", "registryStatus": "ACTIVE", "expire": "2026-01-01"}],
    "messages": [],
}

CONTACT_RESPONSE = {
    "stid": "stid-1",
    "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
    "data": [{"id": 1, "fname": "John", "lname": "Doe", "type": "PERSON", "country": "DE"}],
    "messages": [],
}

JOB_RESPONSE = {
    "stid": "stid-1",
    "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
    "data": [{"id": 123, "status": "RUNNING", "action": "create"}],
    "messages": [],
}


class TestDomainModels:
    def test_info_returns_domain_model(self, client, mock_api):
        mock_api.get("/domain/example.com").mock(
            return_value=httpx.Response(200, json=DOMAIN_RESPONSE)
        )
        result = client.domain.info("example.com")
        domain = result.data[0]
        assert isinstance(domain, Domain)
        assert domain.name == "example.com"
        assert domain.registryStatus == "ACTIVE"
        assert domain.expire == "2026-01-01"

    def test_list_returns_domain_models(self, client, mock_api):
        mock_api.post("/domain/_search").mock(
            return_value=httpx.Response(200, json=DOMAIN_RESPONSE)
        )
        result = client.domain.list()
        assert all(isinstance(d, Domain) for d in result.data)

    def test_create_returns_job_model(self, client, mock_api):
        mock_api.post("/domain").mock(
            return_value=httpx.Response(200, json=JOB_RESPONSE)
        )
        result = client.domain.create({"name": "example.com"})
        job = result.data[0]
        assert isinstance(job, Job)
        assert job.status == "RUNNING"


class TestContactModels:
    def test_info_returns_contact_model(self, client, mock_api):
        mock_api.get("/contact/1").mock(
            return_value=httpx.Response(200, json=CONTACT_RESPONSE)
        )
        result = client.contact.info(1)
        contact = result.data[0]
        assert isinstance(contact, Contact)
        assert contact.fname == "John"
        assert contact.country == "DE"


class TestCertificateModels:
    def test_info_returns_certificate_model(self, client, mock_api):
        resp = {
            "stid": "stid-1",
            "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
            "data": [{"id": 456, "product": "BASIC_SSL", "name": "example.com"}],
            "messages": [],
        }
        mock_api.get("/certificate/456").mock(
            return_value=httpx.Response(200, json=resp)
        )
        result = client.certificate.info(456)
        cert = result.data[0]
        assert isinstance(cert, Certificate)
        assert cert.product == "BASIC_SSL"


class TestZoneModels:
    def test_info_returns_zone_model(self, client, mock_api):
        resp = {
            "stid": "stid-1",
            "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
            "data": [{
                "origin": "example.com",
                "virtualNameServer": "ns1.autodns.com",
                "resourceRecords": [{"name": "www", "type": "A", "value": "1.2.3.4"}],
            }],
            "messages": [],
        }
        mock_api.get("/zone/example.com/ns1.autodns.com").mock(
            return_value=httpx.Response(200, json=resp)
        )
        result = client.zone.info("example.com", "ns1.autodns.com")
        zone = result.data[0]
        assert isinstance(zone, Zone)
        assert zone.origin == "example.com"
        assert len(zone.resourceRecords) == 1


class TestJobModels:
    def test_info_returns_object_job_model(self, client, mock_api):
        resp = {
            "stid": "stid-1",
            "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
            "data": [{"job": {"id": 1, "status": "SUCCESS"}, "object": {"type": "domain", "value": "example.com"}}],
            "messages": [],
        }
        mock_api.get("/job/1").mock(
            return_value=httpx.Response(200, json=resp)
        )
        result = client.job.info(1)
        oj = result.data[0]
        assert isinstance(oj, ObjectJob)
        assert oj.job["status"] == "SUCCESS"


class TestExtraFields:
    def test_unknown_api_fields_preserved_in_extra(self, client, mock_api):
        resp = {
            "stid": "stid-1",
            "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
            "data": [{"name": "example.com", "brandNewField": "surprise", "anotherOne": 42}],
            "messages": [],
        }
        mock_api.get("/domain/example.com").mock(
            return_value=httpx.Response(200, json=resp)
        )
        result = client.domain.info("example.com")
        domain = result.data[0]
        assert domain.name == "example.com"
        assert domain.extra["brandNewField"] == "surprise"
        assert domain.extra["anotherOne"] == 42


class TestNoModelFallback:
    def test_methods_without_model_return_dicts(self, client, mock_api):
        mock_api.get("/hello").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.hello.ping()
        assert result.data[0] == {"name": "example.com"}
