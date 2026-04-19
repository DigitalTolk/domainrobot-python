# Python Domainrobot (InternetX/AutoDNS) Library

[![Documentation Status](https://app.readthedocs.org/projects/domainrobot-python/badge/?version=latest)](https://domainrobot-python.readthedocs.io/en/latest/)
[![Coverage Status](https://coveralls.io/repos/github/DigitalTolk/domainrobot-python/badge.svg)](https://coveralls.io/github/DigitalTolk/domainrobot-python)

Python client for the [Domainrobot JSON API](https://help.internetx.com/display/APIJSONEN/) (InterNetX/AutoDNS).

## Installation

```bash
pip install domainrobot
```

## Quick start

```python
from domainrobot import Domainrobot

client = Domainrobot(
    username="user",
    password="pass",
    context=4,
)

# ping
client.hello.ping()

# list domains
result = client.domain.list(
    {"filters": [{"key": "name", "value": "*.com", "operator": "LIKE"}]},
    keys=["status", "expire"],
)
for domain in result.data:
    print(domain["name"])

client.close()
```

### Context manager

```python
with Domainrobot(username="user", password="pass", context=4) as client:
    result = client.domain.info("example.com")
    print(result.data)
```

## Common examples

### Domain

```python
# register
client.domain.create({
    "name": "example.com",
    "ownerc": {"id": 1},
    "adminc": {"id": 1},
    "techc": {"id": 1},
})

# transfer
client.domain.transfer({
    "name": "example.com",
    "authinfo": "secret",
})

# create cancelation
client.domain.cancelation_create("example.com", {
    "type": "DELETE",
    "execution": "EXPIRE",
})
```

### Contact

```python
# create
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
contact_id = result.data[0]["id"]

# update
client.contact.update(contact_id, {"fname": "Jane"})
```

### Certificate

```python
# prepare order (check CSR)
client.certificate.prepare_order({"plain": "-----BEGIN CERTIFICATE REQUEST-----\n..."})

# order
client.certificate.create({
    "product": "BASIC_SSL",
    "csr": "-----BEGIN CERTIFICATE REQUEST-----\n...",
    "adminContact": {"id": 1},
    "technicalContact": {"id": 1},
})
```

### Zone

```python
# create
client.zone.create({
    "origin": "example.com",
    "soa": {"email": "admin@example.com", "refresh": 43200, "retry": 7200, "expire": 1209600, "ttl": 86400},
    "main": {"address": "1.2.3.4"},
})

# stream update (add/remove records)
client.zone.stream("example.com", {
    "adds": [{"name": "www", "type": "A", "value": "1.2.3.4", "ttl": 3600}],
    "rems": [],
})
```

### Error handling

```python
from domainrobot import Domainrobot, DomainrobotApiError, DomainrobotTransportError

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

| Service | Attribute | Key endpoints |
|---|---|---|
| Account | `client.account` | info, update |
| BackupMx | `client.backup_mx` | create, info, delete, list |
| Certificate | `client.certificate` | create, info, reissue, delete, renew, revoke, list |
| Contact | `client.contact` | create, info, update, delete, list |
| Domain | `client.domain` | create, info, update, list, transfer, renew, restore |
| DomainStudio | `client.domain_studio` | search |
| Hello | `client.hello` | ping |
| Job | `client.job` | info, list, cancel, confirm |
| MailProxy | `client.mail_proxy` | create, info, update, delete, list |
| Poll | `client.poll` | info, confirm |
| Redirect | `client.redirect` | create, info, update, delete, list |
| Session | `client.session` | login, logout |
| SslContact | `client.ssl_contact` | create, info, update, delete, list |
| Subscription | `client.subscription` | create, update, delete, list |
| TransferOut | `client.transfer_out` | list, answer |
| User | `client.user` | create, info, update, delete, list |
| Zone | `client.zone` | create, info, update, delete, list, stream, import_zone |

## License

GPL-3.0-or-later
