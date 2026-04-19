import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestCertificateService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/certificate").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.create({"product": "SSL123"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/certificate/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.info(1)
        assert result.status_code == 200
        assert route.called

    def test_reissue(self, client, mock_api):
        route = mock_api.put("/certificate/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.reissue(1, {"csr": "..."})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/certificate/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.delete(1)
        assert result.status_code == 200
        assert route.called

    def test_renew(self, client, mock_api):
        route = mock_api.put("/certificate/1/_renew").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.renew(1, {"csr": "..."})
        assert result.status_code == 200
        assert route.called

    def test_revoke(self, client, mock_api):
        route = mock_api.post("/certificate/1/_revoke").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.revoke(1, {"serialNumber": "abc"})
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/certificate/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.list()
        assert result.status_code == 200
        assert route.called

    def test_prepare_order(self, client, mock_api):
        route = mock_api.post("/certificate/_prepareOrder").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.prepare_order({"plain": "CSR..."})
        assert result.status_code == 200
        assert route.called

    def test_create_realtime(self, client, mock_api):
        route = mock_api.post("/certificate/_realtime").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.create_realtime({"product": "SSL"})
        assert result.status_code == 200
        assert route.called

    def test_comment_update(self, client, mock_api):
        route = mock_api.put("/certificate/1/_comment").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.comment_update(1, {"comment": "test"})
        assert result.status_code == 200
        assert route.called

    def test_install_check(self, client, mock_api):
        route = mock_api.post("/certificate/_installcheck").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.install_check({"hostname": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_check_vmc_data(self, client, mock_api):
        route = mock_api.post("/certificate/_checkVmcData").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.check_vmc_data({"name": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_site_seal(self, client, mock_api):
        route = mock_api.get("/certificate/1/_siteseal").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.certificate.site_seal(1)
        assert result.status_code == 200
        assert route.called
