from __future__ import annotations

from ._base import BaseService


class CertificateService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/certificate", json=body, headers=headers)

    def info(self, certificate_id: int, *, headers: dict | None = None):
        return self._request(
            "GET", f"/certificate/{certificate_id}", headers=headers
        )

    def reissue(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/certificate/{certificate_id}", json=body, headers=headers
        )

    def delete(self, certificate_id: int, *, headers: dict | None = None):
        return self._request(
            "DELETE", f"/certificate/{certificate_id}", headers=headers
        )

    def renew(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT",
            f"/certificate/{certificate_id}/_renew",
            json=body,
            headers=headers,
        )

    def revoke(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "POST",
            f"/certificate/{certificate_id}/_revoke",
            json=body,
            headers=headers,
        )

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/certificate/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def prepare_order(self, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", "/certificate/_prepareOrder", json=body, headers=headers
        )

    def create_realtime(self, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", "/certificate/_realtime", json=body, headers=headers
        )

    def comment_update(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT",
            f"/certificate/{certificate_id}/_comment",
            json=body,
            headers=headers,
        )

    def install_check(self, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", "/certificate/_installcheck", json=body, headers=headers
        )

    def check_vmc_data(self, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", "/certificate/_checkVmcData", json=body, headers=headers
        )

    def site_seal(self, certificate_id: int, *, headers: dict | None = None):
        return self._request(
            "GET", f"/certificate/{certificate_id}/_siteseal", headers=headers
        )
