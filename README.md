# Python Domainrobot (InternetX/AutoDNS) Library

[![Documentation Status](https://app.readthedocs.org/projects/domainrobot-python/badge/?version=latest)](https://domainrobot-python.readthedocs.io/en/latest/)
[![Coverage Status](https://coveralls.io/repos/github/DigitalTolk/domainrobot-python/badge.svg)](https://coveralls.io/github/DigitalTolk/domainrobot-python)

Python client for the [Domainrobot JSON API](https://help.internetx.com/display/APIJSONEN/) (InterNetX/AutoDNS).

All responses return typed model objects with full IDE autocompletion.

## Installation

```bash
pip install domainrobot
```

## Quick start

```python
from domainrobot import Domainrobot

with Domainrobot(username="user", password="pass", context=4) as client:
    # list all domains
    result = client.domain.list()
    for domain in result.data:
        print(domain.name, domain.expire, domain.registryStatus)
```

### Listing all domains

`client.domain.list()` returns a response where each item in `data` is a
[`Domain`](https://domainrobot-python.readthedocs.io/en/latest/api/models.html) model with these attributes:

| Attribute | Type | Description |
|---|---|---|
| `name` | `str` | Domain name, e.g. `"example.com"` |
| `idn` | `str` | Unicode version (punycode) |
| `expire` | `str` | Expiration date |
| `payable` | `str` | Next payable date |
| `registryStatus` | `str` | `"ACTIVE"`, `"HOLD"`, `"LOCK"`, etc. |
| `autoRenewStatus` | `str` | `"TRUE"`, `"FALSE"`, `"ONCE"` |
| `dnssec` | `bool` | DNSSEC enabled |
| `privacy` | `bool` | Privacy service enabled |
| `trustee` | `bool` | Trustee service enabled |
| `domainsafe` | `bool` | DomainSafe enabled |
| `ownerc` | `dict` | Owner contact |
| `adminc` | `dict` | Admin contact |
| `techc` | `dict` | Technical contact |
| `nameServers` | `list[dict]` | Name servers |
| `comment` | `str` | Custom comment field |
| `created` | `str` | Creation date |
| `updated` | `str` | Last update date |
| `extra` | `dict` | Any unknown/new API fields |

```python
result = client.domain.list(
    {"filters": [{"key": "name", "value": "*.com", "operator": "LIKE"}]},
    keys=["status", "expire"],
)
for domain in result.data:
    print(f"{domain.name}  expires={domain.expire}  status={domain.registryStatus}")
```

### Domain operations

```python
# register (async - returns Job)
job_result = client.domain.create({
    "name": "example.com",
    "ownerc": {"id": 1},
    "adminc": {"id": 1},
    "techc": {"id": 1},
})
print(job_result.data[0].status)  # "RUNNING"

# get info (returns Domain)
result = client.domain.info("example.com")
print(result.data[0].authinfo)

# transfer
client.domain.transfer({"name": "example.com", "authinfo": "secret"})

# cancelation
client.domain.cancelation_create("example.com", {"type": "DELETE", "execution": "EXPIRE"})
```

### Contact

```python
# create (returns Contact)
result = client.contact.create({
    "type": "PERSON",
    "fname": "John",
    "lname": "Doe",
    "email": "john@example.com",
    "country": "DE",
    "city": "Munich",
    "pcode": "80333",
    "address": ["Marienplatz 1"],
    "phone": "+49-89-12345",
})
print(result.data[0].id)  # contact ID

# update
client.contact.update(result.data[0].id, {"fname": "Jane"})
```

### Certificate

```python
# prepare order (returns CertificateData)
prep = client.certificate.prepare_order({"plain": "-----BEGIN CERTIFICATE REQUEST-----\n..."})

# order (async - returns Job)
client.certificate.create({
    "product": "BASIC_SSL",
    "csr": "-----BEGIN CERTIFICATE REQUEST-----\n...",
    "adminContact": {"id": 1},
    "technicalContact": {"id": 1},
})

# get info (returns Certificate)
result = client.certificate.info(456)
print(result.data[0].serialNumber)
```

### Zone

```python
# create (returns Zone)
client.zone.create({
    "origin": "example.com",
    "soa": {"email": "admin@example.com", "refresh": 43200, "retry": 7200, "expire": 1209600, "ttl": 86400},
    "main": {"address": "1.2.3.4"},
})

# stream update - add/remove records (returns Zone)
result = client.zone.stream("example.com", {
    "adds": [{"name": "www", "type": "A", "value": "1.2.3.4", "ttl": 3600}],
    "rems": [],
})
print(result.data[0].resourceRecords)
```

### Error handling

```python
from domainrobot import DomainrobotApiError, DomainrobotTransportError

try:
    client.domain.info("nonexistent.example")
except DomainrobotApiError as e:
    print(f"API error {e.status_code}: {e}")
    print(e.messages)
except DomainrobotTransportError as e:
    print(f"Connection error: {e}")
```

### Custom headers

Every method accepts an optional `headers` parameter:

```python
client.domain.info("example.com", headers={"X-Domainrobot-Demo": "true"})
```

## Available services

| Service | Attribute | Response model | Key endpoints |
|---|---|---|---|
| Account | `client.account` | `Account` | info, update |
| BackupMx | `client.backup_mx` | `BackupMx` | create, info, delete, list |
| Certificate | `client.certificate` | `Certificate` / `Job` | create, info, reissue, delete, renew, revoke, list |
| Contact | `client.contact` | `Contact` | create, info, update, delete, list |
| Domain | `client.domain` | `Domain` / `Job` | create, info, update, list, transfer, renew, restore |
| DomainStudio | `client.domain_studio` | `DomainEnvelope` | search |
| Hello | `client.hello` | - | ping |
| Job | `client.job` | `ObjectJob` | info, list, cancel, confirm |
| MailProxy | `client.mail_proxy` | `MailProxy` | create, info, update, delete, list |
| Poll | `client.poll` | `PollMessage` | info, confirm |
| Redirect | `client.redirect` | `Redirect` | create, info, update, delete, list |
| Session | `client.session` | `User` | login, logout |
| SslContact | `client.ssl_contact` | `SslContact` | create, info, update, delete, list |
| Subscription | `client.subscription` | `Subscription` | create, update, delete, list |
| TransferOut | `client.transfer_out` | `TransferOut` | list, answer |
| User | `client.user` | `User` | create, info, update, delete, list |
| Zone | `client.zone` | `Zone` | create, info, update, delete, list, stream, import_zone |

## Documentation

Full API reference: [domainrobot-python.readthedocs.io](https://domainrobot-python.readthedocs.io/en/latest/)

## License

GPL-3.0-or-later
