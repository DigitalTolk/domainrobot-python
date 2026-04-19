from __future__ import annotations

from ..models.resources import Certificate, CertificateData, Job
from ._base import BaseService


class CertificateService(BaseService):
    """SSL certificate operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Order a new certificate. Async operation.

        :param body: Certificate data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request("POST", "/certificate", json=body, headers=headers, model=Job)

    def info(self, certificate_id: int, *, headers: dict | None = None):
        """Inquire data for a certificate.

        :param certificate_id: Certificate ID.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Certificate` data.
        """
        return self._request(
            "GET", f"/certificate/{certificate_id}", headers=headers, model=Certificate
        )

    def reissue(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        """Reissue a certificate. Async operation.

        :param certificate_id: Certificate ID.
        :param body: Certificate data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/certificate/{certificate_id}", json=body, headers=headers, model=Job
        )

    def delete(self, certificate_id: int, *, headers: dict | None = None):
        """Delete a certificate. Async operation.

        :param certificate_id: Certificate ID.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "DELETE", f"/certificate/{certificate_id}", headers=headers, model=Job
        )

    def renew(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        """Renew a certificate. Async operation.

        :param certificate_id: Certificate ID.
        :param body: Certificate data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT",
            f"/certificate/{certificate_id}/_renew",
            json=body,
            headers=headers,
            model=Job,
        )

    def revoke(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        """Revoke a certificate by serial number.

        :param certificate_id: Certificate ID.
        :param body: Revocation data including serial number.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "POST",
            f"/certificate/{certificate_id}/_revoke",
            json=body,
            headers=headers,
            model=Job,
        )

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List certificates.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.Certificate`.
        """
        return self._request(
            "POST",
            "/certificate/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=Certificate,
        )

    def prepare_order(self, body: dict, *, headers: dict | None = None):
        """Prepare a certificate order (check CSR and generate auth data).

        :param body: Certificate data including the CSR.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.CertificateData` data.
        """
        return self._request(
            "POST", "/certificate/_prepareOrder", json=body, headers=headers, model=CertificateData
        )

    def create_realtime(self, body: dict, *, headers: dict | None = None):
        """Order or renew a certificate in realtime.

        :param body: Certificate data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Certificate` data.
        """
        return self._request(
            "POST", "/certificate/_realtime", json=body, headers=headers, model=Certificate
        )

    def comment_update(
        self, certificate_id: int, body: dict, *, headers: dict | None = None
    ):
        """Update the comment for a certificate.

        :param certificate_id: Certificate ID.
        :param body: Comment data.
        :param headers: Optional extra HTTP headers.
        """
        return self._request(
            "PUT",
            f"/certificate/{certificate_id}/_comment",
            json=body,
            headers=headers,
        )

    def install_check(self, body: dict, *, headers: dict | None = None):
        """Check an installed certificate on a server.

        :param body: Request data including hostname.
        :param headers: Optional extra HTTP headers.
        """
        return self._request(
            "POST", "/certificate/_installcheck", json=body, headers=headers
        )

    def check_vmc_data(self, body: dict, *, headers: dict | None = None):
        """Check data against VMC certificate requirements.

        :param body: VMC check data.
        :param headers: Optional extra HTTP headers.
        """
        return self._request(
            "POST", "/certificate/_checkVmcData", json=body, headers=headers
        )

    def site_seal(self, certificate_id: int, *, headers: dict | None = None):
        """Fetch site seal information for a certificate.

        :param certificate_id: Certificate ID.
        :param headers: Optional extra HTTP headers.
        """
        return self._request(
            "GET", f"/certificate/{certificate_id}/_siteseal", headers=headers
        )
