from __future__ import annotations

import dataclasses
from typing import Any

from ._base import Model


@dataclasses.dataclass
class Domain(Model):
    """A domain object."""

    name: str | None = None
    idn: str | None = None
    ownerc: dict[str, Any] | None = None
    adminc: dict[str, Any] | None = None
    techc: dict[str, Any] | None = None
    zonec: dict[str, Any] | None = None
    nameServers: list[dict[str, Any]] | None = None
    nameServerEntries: list[str] | None = None
    period: dict[str, Any] | None = None
    registryStatus: str | None = None
    registrarStatus: str | None = None
    autoRenewStatus: str | None = None
    cancelationStatus: str | None = None
    dnssec: bool | None = None
    autoDnssec: bool | None = None
    dnssecData: list[dict[str, Any]] | None = None
    privacy: bool | None = None
    trustee: bool | None = None
    domainsafe: bool | None = None
    parking: str | None = None
    authinfo: str | None = None
    authinfoExpire: str | None = None
    expire: str | None = None
    payable: str | None = None
    action: str | None = None
    comment: str | None = None
    priceClass: str | None = None
    priceClassRenew: str | None = None
    nicMemberLabel: str | None = None
    domainCreated: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class DomainRestore(Model):
    """A restorable domain object."""

    name: str | None = None
    idn: str | None = None
    deleted: str | None = None
    restorePhaseEnd: str | None = None
    expire: str | None = None
    registryStatus: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class DomainCancelation(Model):
    """A domain cancelation object."""

    domain: str | None = None
    type: str | None = None
    execution: str | None = None
    registryWhen: str | None = None
    gainingRegistrar: str | None = None
    disconnect: bool | None = None
    notice: str | None = None
    registryStatus: str | None = None
    status: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Contact(Model):
    """A domain contact object."""

    id: int | None = None
    type: str | None = None
    alias: str | None = None
    fname: str | None = None
    lname: str | None = None
    organization: str | None = None
    title: str | None = None
    address: list[str] | None = None
    pcode: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    email: str | None = None
    phone: str | None = None
    fax: str | None = None
    sip: str | None = None
    protection: str | None = None
    domainsafe: bool | None = None
    comment: str | None = None
    verification: str | None = None
    extensions: dict[str, Any] | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Certificate(Model):
    """An SSL certificate object."""

    id: int | None = None
    name: str | None = None
    product: str | None = None
    certificateType: str | None = None
    csr: str | None = None
    server: str | None = None
    serialNumber: str | None = None
    signatureHashAlgorithm: str | None = None
    expire: str | None = None
    payable: str | None = None
    lifetime: dict[str, Any] | None = None
    orderId: str | None = None
    partnerOrderId: str | None = None
    adminContact: dict[str, Any] | None = None
    technicalContact: dict[str, Any] | None = None
    authentication: dict[str, Any] | None = None
    certificationAuthority: list[dict[str, Any]] | None = None
    subjectAlternativeNames: list[dict[str, Any]] | None = None
    histories: list[dict[str, Any]] | None = None
    software: str | None = None
    comment: str | None = None
    certificateTransparency: bool | None = None
    domain: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class CertificateData(Model):
    """Certificate preparation data (from prepareOrder)."""

    plain: str | None = None
    name: str | None = None
    keySize: int | None = None
    countryCode: str | None = None
    state: str | None = None
    city: str | None = None
    organization: str | None = None
    organizationUnit: str | None = None
    email: str | None = None
    product: str | None = None
    authentication: list[dict[str, Any]] | None = None
    algorithm: str | None = None
    signatureHashAlgorithm: str | None = None
    subjectAlternativeNames: list[dict[str, Any]] | None = None
    certificate: dict[str, Any] | None = None


@dataclasses.dataclass
class SslContact(Model):
    """An SSL contact object."""

    id: int | None = None
    fname: str | None = None
    lname: str | None = None
    organization: str | None = None
    title: str | None = None
    address: list[str] | None = None
    pcode: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    email: str | None = None
    phone: str | None = None
    fax: str | None = None
    extensions: dict[str, Any] | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Zone(Model):
    """A DNS zone object."""

    origin: str | None = None
    idn: str | None = None
    virtualNameServer: str | None = None
    soa: dict[str, Any] | None = None
    main: dict[str, Any] | None = None
    resourceRecords: list[dict[str, Any]] | None = None
    nameServers: list[dict[str, Any]] | None = None
    nameServerGroup: str | None = None
    dnssec: bool | None = None
    allowTransfer: bool | None = None
    domainsafe: bool | None = None
    comment: str | None = None
    action: str | None = None
    grants: list[str] | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Job(Model):
    """An asynchronous job object."""

    id: int | None = None
    status: str | None = None
    subStatus: str | None = None
    action: str | None = None
    subType: str | None = None
    execution: str | None = None
    events: list[dict[str, Any]] | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class ObjectJob(Model):
    """A job with its related object (from job info/list)."""

    job: dict[str, Any] | None = None
    object: dict[str, Any] | None = None
    authentication: list[dict[str, Any]] | None = None
    niccomLogs: list[dict[str, Any]] | None = None


@dataclasses.dataclass
class PollMessage(Model):
    """A poll message object."""

    id: int | None = None
    stid: str | None = None
    ctid: str | None = None
    job: dict[str, Any] | None = None
    notify: dict[str, Any] | None = None
    messages: list[dict[str, Any]] | None = None
    flags: str | None = None
    notice: str | None = None
    object: dict[str, Any] | None = None
    owner: dict[str, Any] | None = None
    created: str | None = None


@dataclasses.dataclass
class User(Model):
    """A user object."""

    user: str | None = None
    context: int | None = None
    defaultEmail: str | None = None
    status: int | None = None
    substatus: int | None = None
    authType: str | None = None
    language: str | None = None
    details: dict[str, Any] | None = None
    lock: str | None = None
    parent: dict[str, Any] | None = None
    directCustomer: bool | None = None
    customer: dict[str, Any] | None = None
    acls: dict[str, Any] | None = None
    profiles: dict[str, Any] | None = None
    subscriptions: list[dict[str, Any]] | None = None
    nameServerGroups: list[dict[str, Any]] | None = None
    created: str | None = None
    updated: str | None = None


@dataclasses.dataclass
class TransferOut(Model):
    """A transfer-out request object."""

    domain: str | None = None
    gainingRegistrar: str | None = None
    loosingRegistrar: str | None = None
    start: str | None = None
    reminder: str | None = None
    autoAck: str | None = None
    autoNack: str | None = None
    end: str | None = None
    autoAnswer: bool | None = None
    recipient: str | None = None
    type: str | None = None
    nackReason: int | None = None
    transaction: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Account(Model):
    """A customer account object."""

    currentAccountBalance: float | None = None
    runningTotal: float | None = None
    creditLimit: float | None = None
    currency: str | None = None
    minRunningTotalNotification: float | None = None
    minRunningTotalNotificationEmail: str | None = None
    customer: dict[str, Any] | None = None
    created: str | None = None
    updated: str | None = None


@dataclasses.dataclass
class BackupMx(Model):
    """A BackupMX record object."""

    domain: str | None = None
    idn: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class MailProxy(Model):
    """A mail proxy object."""

    domain: str | None = None
    idn: str | None = None
    target: str | None = None
    admin: str | None = None
    protection: str | None = None
    greylisting: str | None = None
    virus: str | None = None
    bannedFiles: str | None = None
    header: str | None = None
    spam: dict[str, Any] | None = None
    whitelist: dict[str, Any] | None = None
    blacklist: dict[str, Any] | None = None
    excludelist: dict[str, Any] | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Redirect(Model):
    """A redirect object."""

    source: str | None = None
    target: str | None = None
    type: str | None = None
    mode: str | None = None
    domain: str | None = None
    title: str | None = None
    backups: list[str] | None = None
    sourceIdn: str | None = None
    targetIdn: str | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Subscription(Model):
    """A subscription contract object."""

    id: int | None = None
    status: str | None = None
    object: str | None = None
    description: str | None = None
    articleLabel: str | None = None
    articleTypeLabel: str | None = None
    period: dict[str, Any] | None = None
    expire: str | None = None
    payable: str | None = None
    cancelation: str | None = None
    canceled: str | None = None
    cancelationTerm: dict[str, Any] | None = None
    businessCase: str | None = None
    item: list[dict[str, Any]] | None = None
    created: str | None = None
    updated: str | None = None
    owner: dict[str, Any] | None = None
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class DomainEnvelope(Model):
    """A DomainStudio search result."""

    domain: str | None = None
    idn: str | None = None
    tld: str | None = None
    subTld: str | None = None
    source: str | None = None
    services: dict[str, Any] | None = None
    portfolio: bool | None = None
