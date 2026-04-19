from domainrobot.response import DomainrobotResponse


class TestDomainrobotResponse:
    def test_parses_full_body(self):
        body = {
            "stid": "stid-1",
            "ctid": "ctid-1",
            "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
            "data": [{"id": 1}],
            "messages": [{"text": "OK"}],
        }
        resp = DomainrobotResponse(200, body, {"content-type": "application/json"})
        assert resp.status_code == 200
        assert resp.stid == "stid-1"
        assert resp.ctid == "ctid-1"
        assert resp.status == {"code": "S0001", "text": "OK", "type": "SUCCESS"}
        assert resp.data == [{"id": 1}]
        assert resp.messages == [{"text": "OK"}]
        assert resp.headers == {"content-type": "application/json"}

    def test_parses_empty_body(self):
        resp = DomainrobotResponse(204, {}, {})
        assert resp.status_code == 204
        assert resp.stid is None
        assert resp.ctid is None
        assert resp.data is None
        assert resp.messages is None

    def test_repr(self):
        resp = DomainrobotResponse(200, {"stid": "abc"}, {})
        assert repr(resp) == "DomainrobotResponse(status_code=200, stid='abc')"

    def test_repr_no_stid(self):
        resp = DomainrobotResponse(200, {}, {})
        assert repr(resp) == "DomainrobotResponse(status_code=200, stid=None)"
