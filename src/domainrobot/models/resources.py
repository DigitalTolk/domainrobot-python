from __future__ import annotations

import dataclasses
import datetime
from typing import Any

from ._base import Model


@dataclasses.dataclass
class Domain(Model):
    """A domain object."""

    #: The name of the domain.
    name: str | None = None
    #: The unicode domain name
    idn: str | None = None
    #: The owner contact.
    ownerc: dict[str, Any] | None = None
    #: The administrative contact.
    adminc: dict[str, Any] | None = None
    #: The technical contact reference.
    techc: dict[str, Any] | None = None
    #: The dns contact.
    zonec: dict[str, Any] | None = None
    #: The nameservers.
    nameServers: list[dict[str, Any]] | None = None
    #: NSentry is only be provided for .DE. If NSentry is used, nameServers is
    #: not allowed.
    nameServerEntries: list[str] | None = None
    #: The period in years, depends on the requested action
    period: dict[str, Any] | None = None
    #: The registry status.
    registryStatus: str | None = None
    #: The registrar status.
    registrarStatus: str | None = None
    #: The autorenew status.
    autoRenewStatus: str | None = None
    #: The cancelation status.
    cancelationStatus: str | None = None
    #: Indicates whether DNSSEC is enabled for the domain or not.
    dnssec: bool | None = None
    #: Enables or disables automatic DNSSEC for certain name servers
    #: (e.g. NodeSecure).
    autoDnssec: bool | None = None
    #: Submits the key material to the registry. If the list is empty, the key
    #: material is deleted at the registry. If the key is omitted during an
    #: update, the data is retained.
    dnssecData: list[dict[str, Any]] | None = None
    #: Enable privacy service for the domain.
    privacy: bool | None = None
    #: Enable trustee service for the domain.
    trustee: bool | None = None
    #: Enable domainsafe.
    domainsafe: bool | None = None
    #: The parking provider.
    parking: str | None = None
    #: The authinfo.
    authinfo: str | None = None
    #: The expire date of the authinfo.
    authinfoExpire: datetime.datetime | None = None
    #: The expire date of the domain.
    expire: datetime.datetime | None = None
    #: The payable date of the domain.
    payable: datetime.datetime | None = None
    #: The last action.
    action: str | None = None
    #: A custom field. Can only be updated via PUT /domain/{name}/_comment.
    #: Requires appropriate ACLs.
    comment: str | None = None
    #: The priceclass for the registration of the domain.
    priceClass: str | None = None
    #: The priceclass for the renew of the domain.
    priceClassRenew: str | None = None
    #: The nic member label.
    nicMemberLabel: str | None = None
    #: The domain creation of the domain at the registry.
    domainCreated: datetime.datetime | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class DomainRestore(Model):
    """A restorable domain object."""

    #: The name of the domain.
    name: str | None = None
    #: The unicode domain name
    idn: str | None = None
    #: The date at deletion of the domain
    deleted: datetime.datetime | None = None
    #: The end of current restore phase
    restorePhaseEnd: datetime.datetime | None = None
    #: The expire date of the domain.
    expire: datetime.datetime | None = None
    #: The registry status.
    registryStatus: str | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class DomainCancelation(Model):
    """A domain cancelation object."""

    #: Domain to be cancelled.
    domain: str | None = None
    #: The cancelation type. TRANSIT is only possible for certain TLDs.
    type: str | None = None
    #: Date and Time at which the domain is to be canceled.
    execution: str | None = None
    #: The date on which the registry should perform the domain cancelation.
    #: Only necessary when ExecutionType equals DATE.
    registryWhen: datetime.datetime | None = None
    #: The registrar to which the domain is to be transferred. Only possible
    #: with preack, for which it is required. accept_all = All registrars are
    #: accepted Designated registrar (e.g. DENIC-104). Ask the registry for
    #: the provider ID of your reseller. The transfer is then only possible to
    #: the selected registrar.
    gainingRegistrar: str | None = None
    #: Specifies whether the domain is disconnected during a transit. Only
    #: possible with transit, for which it is necessary. Default value = false
    disconnect: bool | None = None
    #: Some remarks
    notice: str | None = None
    registryStatus: str | None = None
    #: Status of the cancelation request.
    status: str | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Contact(Model):
    """A domain contact object."""

    #: The unique identifier of the contact
    id: int | None = None
    #: Domain contact type
    type: str | None = None
    #: A string that is either automatically generated when an alias is not
    #: sent or a self-defined string that can be set by the user for the
    #: purpose of identifying the domain contact.
    alias: str | None = None
    #: First name
    fname: str | None = None
    #: Last name
    lname: str | None = None
    #: The name of the organization
    organization: str | None = None
    #: A prefix to a person's name.
    title: str | None = None
    #: Street or post box. Depending on the registry, up to 65,536 characters
    #: may be possible.
    address: list[str] | None = None
    #: The postal code ("zip-code") of the contact. For countries Canada,
    #: Norway, Poland and Spain the format of the postal code is checked for
    #: validity. Canada (ca): Six characters in the following format 'LNL NLN',
    #: where 'L' represents a letter and 'N' represents a number.
    #: Norway (co): Four characters between 0001 and 9990.
    #: Poland (pl): Consists of five digits, with a hyphen ('-') between the
    #: second and third digits. Spain (es): Consisting of exactly five digits.
    #: No letters or special characters, only numbers. Each of the five
    #: positions can be any digit from 0 to 9.
    pcode: str | None = None
    #: The city of the contact
    city: str | None = None
    #: The local country state of the contact
    state: str | None = None
    #: Country (ISO 3166-1 alpha-2). Country Code. Certain strings, such as
    #: "Germany", are mapped to DE.
    country: str | None = None
    #: Email address
    email: str | None = None
    #: The phone number of the contact
    phone: str | None = None
    #: The fax number of the contact
    fax: str | None = None
    #: The sip of the contact
    sip: str | None = None
    #: The protection of the contact
    protection: str | None = None
    #: Indicates whether the domain contact is in the DomainSafe.
    domainsafe: bool | None = None
    #: A freely definable text that can be set for a contact. May only be
    #: composed of ASCII characters.
    comment: str | None = None
    #: The status of domain contact verification.
    verification: str | None = None
    #: Additional data for contacts required by certain TLDs.
    extensions: dict[str, Any] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Certificate(Model):
    """An SSL certificate object."""

    #: The ID of the certificate
    id: int | None = None
    #: The name of the certificate
    name: str | None = None
    #: The ordered product
    product: str | None = None
    #: The type of the certificate
    certificateType: str | None = None
    #: CSR - Key (Certificate Signing Request)
    csr: str | None = None
    #: The certificate
    server: str | None = None
    #: Serial number of the certificate
    serialNumber: str | None = None
    #: The signature hash algorithm which was used
    signatureHashAlgorithm: str | None = None
    #: The notAfter date of the certificate
    expire: datetime.datetime | None = None
    #: The payable date for the certificate. Indicates when a runtime renewal
    #: must take place.
    payable: datetime.datetime | None = None
    #: The certificate term in months
    lifetime: dict[str, Any] | None = None
    #: The unique certificate order number
    orderId: str | None = None
    #: The order number of the related request
    partnerOrderId: str | None = None
    #: The administrative contact
    adminContact: dict[str, Any] | None = None
    #: The technical contact
    technicalContact: dict[str, Any] | None = None
    #: The authentication of the certificate
    authentication: dict[str, Any] | None = None
    #: The certificate authority chain
    certificationAuthority: list[dict[str, Any]] | None = None
    #: Subject Alternative Names (SANs)
    subjectAlternativeNames: list[dict[str, Any]] | None = None
    #: The history of the certificate (old certificate versions)
    histories: list[dict[str, Any]] | None = None
    #: The webserver software in use, relevant values: 'II5' for Mircosoft,
    #: 'APACHE2' for Linux
    software: str | None = None
    #: A custom field. Can only be updated via PUT /certificate/{id}/_comment.
    #: Requires appropriate ACLs.
    comment: str | None = None
    #: Activates the certificate transparency for a certificate. Default is
    #: "True".
    certificateTransparency: bool | None = None
    #: The domain, which the redirect belongs.
    domain: str | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class CertificateData(Model):
    """Certificate preparation data (from prepareOrder)."""

    #: The CSR key as a string.
    plain: str | None = None
    #: The name of the certificate which is contained within the CSR key.
    name: str | None = None
    #: The key length of the CSR key.
    keySize: int | None = None
    #: The country code which is contained within the CSR key.
    countryCode: str | None = None
    #: The state defined in the csr.
    state: str | None = None
    #: The city contained within the CSR key.
    city: str | None = None
    #: The organisation contained within the CSR key.
    organization: str | None = None
    #: The organisation contained within the CSR key.
    organizationUnit: str | None = None
    #: The email address contained within the CSR key.
    email: str | None = None
    #: The SSL product.
    product: str | None = None
    #: The generated authentication data.
    authentication: list[dict[str, Any]] | None = None
    #: The algorithm used in the CSR key.
    algorithm: str | None = None
    #: The hash algorithm which was used for the CSR.
    signatureHashAlgorithm: str | None = None
    #: The SubjectAlternativeNames contained within the CSR key.
    subjectAlternativeNames: list[dict[str, Any]] | None = None
    #: The certificate.
    certificate: dict[str, Any] | None = None


@dataclasses.dataclass
class SslContact(Model):
    """An SSL contact object."""

    #: Unique identifier of the object
    id: int | None = None
    #: The first name of the contact
    fname: str | None = None
    #: The last name of the contact
    lname: str | None = None
    #: The name of organisation of the contact.
    organization: str | None = None
    #: The title of the contact
    title: str | None = None
    #: The address of the contact.
    address: list[str] | None = None
    #: The postal code of the contact.
    pcode: str | None = None
    #: The city of the contact
    city: str | None = None
    #: The local country state of the contact
    state: str | None = None
    #: The country of the contact
    country: str | None = None
    #: The email address of the contact.
    email: str | None = None
    #: The phone number of the contact
    phone: str | None = None
    #: The fax number of the contact
    fax: str | None = None
    #: The contact extensions
    extensions: dict[str, Any] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The owner of the object
    owner: dict[str, Any] | None = None
    #: The updating using of the object
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Zone(Model):
    """A DNS zone object."""

    #: Zone name
    origin: str | None = None
    #: Punycode version of the origin.
    idn: str | None = None
    #: The first nameserver managed by the system
    virtualNameServer: str | None = None
    #: Only for ns_action: "primary" and "complete"
    soa: dict[str, Any] | None = None
    #: Main IP address of the zone. Required for ns_action "primary" and
    #: "complete".
    main: dict[str, Any] | None = None
    #: The resource records.
    resourceRecords: list[dict[str, Any]] | None = None
    #: List of hostnames to be used as name severs.
    nameServers: list[dict[str, Any]] | None = None
    #: Name of the nameserver group.
    nameServerGroup: str | None = None
    #: If true dnssec signing for the zone is active.
    dnssec: bool | None = None
    #: Allow zone transfer for the defined zone grants
    allowTransfer: bool | None = None
    #: Denotes of the zone is present in the DomainSafe service.
    domainsafe: bool | None = None
    #: A custom field. Can only be updated via PUT
    #: /zone/{name}/{nameserver}/_comment. Requires appropriate ACLs.
    comment: str | None = None
    #: Additional nameserver check is proceeded.
    action: str | None = None
    #: A list of IP addresses from which a zone transfer (AXFR) by be started
    #: from for this zone.
    grants: list[str] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: Owner of the zone object
    owner: dict[str, Any] | None = None
    #: User who last updated the zone.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Job(Model):
    """An asynchronous job object.

    Many operations (domain create, transfer, certificate order) are
    asynchronous and return a Job instead of the final resource.
    """

    #: The job id.
    id: int | None = None
    #: Defines the status of a job.
    status: str | None = None
    #: Substatus of the job. Substatuses exist depending on the job.
    subStatus: str | None = None
    #: The action, which the job is supposed to do.
    action: str | None = None
    #: The job subtype.
    subType: str | None = None
    #: The date on which the job will be processed by the system.
    execution: datetime.datetime | None = None
    #: The workflow events generated by the job.
    events: list[dict[str, Any]] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class ObjectJob(Model):
    """A job with its related object (from job info/list)."""

    #: The related job.
    job: dict[str, Any] | None = None
    #: The object of the job or notify.
    object: dict[str, Any] | None = None
    #: The overall authentication status for a certificate request.
    authentication: list[dict[str, Any]] | None = None
    #: The niccom logs.
    niccomLogs: list[dict[str, Any]] | None = None


@dataclasses.dataclass
class PollMessage(Model):
    """A poll message object."""

    #: Message ID. Required for confirming with Poll Confirm.
    id: int | None = None
    #: The server transaction ID.
    stid: str | None = None
    #: The custom transaction ID.
    ctid: str | None = None
    #: The job data. Available if the message is a job message
    job: dict[str, Any] | None = None
    #: The notification data. Available if the message is a notification message
    notify: dict[str, Any] | None = None
    #: System messages.
    messages: list[dict[str, Any]] | None = None
    #: Optional message flags.
    flags: str | None = None
    #: Optional notice.
    notice: str | None = None
    #: "Response" object like "domain". Object type depends on the request.
    object: dict[str, Any] | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None


@dataclasses.dataclass
class User(Model):
    """A user object."""

    #: The user name.
    user: str | None = None
    #: The context. A separated section.
    context: int | None = None
    #: The default email.
    defaultEmail: str | None = None
    #: User status.
    status: int | None = None
    #: User substatus of the User.
    substatus: int | None = None
    #: Authentication type, e.g. password or TOTP.
    authType: str | None = None
    #: The language for the user. The setting affects the user interface
    #: language and system messages. Possible values: de en es.
    language: str | None = None
    #: The user details.
    details: dict[str, Any] | None = None
    #: Defines the type of user lock.
    lock: str | None = None
    #: Parent user.
    parent: dict[str, Any] | None = None
    #: Specifies whether the user is a direct customer of the user.
    #: false = No direct customer true = direct customer
    #: Default value = false
    #: For XML, 0 (false) and 1 (true) can also be used.
    directCustomer: bool | None = None
    #: Customer to which this user belongs.
    customer: dict[str, Any] | None = None
    #: User privileges.
    acls: dict[str, Any] | None = None
    #: User profile.
    profiles: dict[str, Any] | None = None
    #: Different subscriptions of the users.
    subscriptions: list[dict[str, Any]] | None = None
    #: The available name server groups
    nameServerGroups: list[dict[str, Any]] | None = None
    #: The user created date.
    created: datetime.datetime | None = None
    #: The user updated date.
    updated: datetime.datetime | None = None


@dataclasses.dataclass
class TransferOut(Model):
    """A transfer-out request object."""

    #: The domain name.
    domain: str | None = None
    #: The gaining registrar.
    gainingRegistrar: str | None = None
    #: The loosing registrar.
    loosingRegistrar: str | None = None
    #: Date on which the transfer started.
    start: datetime.datetime | None = None
    #: Date on which the transfer reminder mail is sent.
    reminder: datetime.datetime | None = None
    #: Date of the automatic ACK on which the transfer is confirmed.
    autoAck: datetime.datetime | None = None
    #: Date of the automatic NACK on which the transfer is rejected.
    autoNack: datetime.datetime | None = None
    #: Date on which the transfer process ends.
    end: datetime.datetime | None = None
    #: Automatic response to the transfer request.
    #: false = not active true = active
    #: Default value = false
    #: For XML, 0 (false) and 1 (true) can also be used.
    autoAnswer: bool | None = None
    #: Receiver of the reminder email.
    recipient: str | None = None
    #: The type of the transfer.
    type: str | None = None
    #: Reason for rejection. Only for type "nack", mandatory here.
    nackReason: int | None = None
    #: The ctid.
    transaction: str | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Account(Model):
    """A customer account object."""

    #: The current account balance
    currentAccountBalance: float | None = None
    #: The current total, the amount of all finished and unfinished
    #: transactions.
    runningTotal: float | None = None
    #: The credit limit of the account.
    creditLimit: float | None = None
    #: Currency in which the account is held.
    currency: str | None = None
    #: The minimum account balance at which a notification should be sent.
    minRunningTotalNotification: float | None = None
    #: Email address for notification. A notification is sent when the minimum
    #: account balance has been reached (minRunningTotalNotification).
    minRunningTotalNotificationEmail: str | None = None
    #: The customer object.
    customer: dict[str, Any] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: The date of the last update.
    updated: datetime.datetime | None = None


@dataclasses.dataclass
class BackupMx(Model):
    """A BackupMX record object."""

    #: Domain name for which the BackupMX Record is to be created.
    domain: str | None = None
    #: IDN version of the domain name written in Punycode.
    idn: str | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class MailProxy(Model):
    """A mail proxy object."""

    #: Domain name for which the BackupMX Record is to be created.
    domain: str | None = None
    #: IDN version of the domain name written in Punycode.
    idn: str | None = None
    #: Mail server to which the MailProxy should forward the emails. Note that
    #: the MX record of your mail server must be removed from the zone.
    target: str | None = None
    #: Email address of the administrator to whom notifications are sent to.
    admin: str | None = None
    #: Security settings for handling infected mails.
    protection: str | None = None
    #: If greylisting is activated, the first email from an unknown sender is
    #: rejected at first. Mails from this sender will only be accepted after a
    #: further delayed delivery attempt.
    greylisting: str | None = None
    #: Defines whether to check for viruses and how to deal with detected
    #: viruses.
    virus: str | None = None
    #: Defines whether files should be checked and how banned files should be
    #: avoided.
    bannedFiles: str | None = None
    #: Defines whether headers are to be checked and how banned headers are to
    #: be handled.
    header: str | None = None
    #: The spam policy options.
    spam: dict[str, Any] | None = None
    #: Define email addresses whose mails should be trusted and never marked
    #: as spam.
    whitelist: dict[str, Any] | None = None
    #: Specification of email addresses whose mails are always to be marked
    #: as spam.
    blacklist: dict[str, Any] | None = None
    #: Definition of administrative addresses that should never be ignored by
    #: spam filters. An example of this is the "Hostmaster" addresses, e.g.
    #: hostmaster@example.com.
    excludelist: dict[str, Any] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Redirect(Model):
    """A redirect object."""

    #: Domain that is to be redirected, e.g. test.example.com.
    source: str | None = None
    #: The URL of the target domain. Enter the domain without "https://".
    target: str | None = None
    #: The type of redirect.
    type: str | None = None
    #: The redirect mode of domain and email forwarding.
    mode: str | None = None
    #: Domain that is to be redirected, e.g. example.com.
    domain: str | None = None
    #: Only for the 'frame' mode. Page title to be displayed in the browser
    #: title bar.
    title: str | None = None
    #: Backup destinations for the redirects. If the first destination cannot
    #: be reached, the domain is automatically redirected to the substitute
    #: destination (domain redirection, frame redirect).
    backups: list[str] | None = None
    #: The IDN version of the domain name. Domains can be entered with or
    #: without "www".
    sourceIdn: str | None = None
    #: The Punycode syntax (IDN) version of the target domain URL. Enter the
    #: domain without "https://".
    targetIdn: str | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class Subscription(Model):
    """A subscription contract object."""

    #: The unique identifier of the periodic
    id: int | None = None
    #: Billing status of the subscription.
    status: str | None = None
    #: Name of the subscription or the contract number.
    object: str | None = None
    #: The human readable name of the subscription, e.g. the name of a package
    description: str | None = None
    #: The article label of the subscription, e.g. backup_mx
    articleLabel: str | None = None
    #: The article type label of the subscription, e.g. domain
    articleTypeLabel: str | None = None
    #: The period used by the subscription, e.g. 1 month
    period: dict[str, Any] | None = None
    #: The expiration date of the subscription.
    expire: datetime.datetime | None = None
    #: The date then the event should be billed.
    payable: datetime.datetime | None = None
    #: The cancelation date of the subscription.
    cancelation: datetime.datetime | None = None
    #: The canceled date.
    canceled: datetime.datetime | None = None
    #: cancelationTerm of the subscription..
    cancelationTerm: dict[str, Any] | None = None
    #: The businessCase of the subscription, e.g. create
    businessCase: str | None = None
    #: The items of the subscription
    item: list[dict[str, Any]] | None = None
    #: Date of creation.
    created: datetime.datetime | None = None
    #: Date of the last update.
    updated: datetime.datetime | None = None
    #: The object owner.
    owner: dict[str, Any] | None = None
    #: User who performed the last update.
    updater: dict[str, Any] | None = None


@dataclasses.dataclass
class DomainEnvelope(Model):
    """A DomainStudio search result."""

    #: The domain
    domain: str | None = None
    #: The unicode domain name
    idn: str | None = None
    #: The tld for the given domain name
    tld: str | None = None
    #: The subTld for the given domain name
    subTld: str | None = None
    #: Source
    source: str | None = None
    #: Source
    services: dict[str, Any] | None = None
    #: Defines if the user already owns this domain.
    portfolio: bool | None = None
