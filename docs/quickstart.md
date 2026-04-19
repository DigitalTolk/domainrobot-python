# Quick start

## Installation

```bash
pip install domainrobot
```

## Basic usage

```python
from domainrobot import Domainrobot

with Domainrobot(username="user", password="pass", context=4) as client:
    # list all domains
    result = client.domain.list()
    for domain in result.data:
        print(domain.name, domain.expire, domain.registryStatus)
```

Every service method returns a `DomainrobotResponse` where `data` is a list of
typed model objects. The model attributes match the API field names and provide
full IDE autocompletion.

## Listing all domains

```python
result = client.domain.list()

for domain in result.data:
    # Domain model attributes (all optional, None if not returned by API):
    #
    # domain.name             - domain name, e.g. "example.com"
    # domain.idn              - unicode version (punycode)
    # domain.expire           - expiration date
    # domain.payable          - next payable date
    # domain.registryStatus   - "ACTIVE", "HOLD", "LOCK", etc.
    # domain.autoRenewStatus  - "TRUE", "FALSE", "ONCE"
    # domain.cancelationStatus- cancelation status if any
    # domain.action           - last action, e.g. "CREATE", "UPDATE"
    # domain.authinfo         - transfer auth code
    # domain.dnssec           - DNSSEC enabled (bool)
    # domain.privacy          - privacy service enabled (bool)
    # domain.trustee          - trustee service enabled (bool)
    # domain.domainsafe       - DomainSafe enabled (bool)
    # domain.comment          - custom comment
    # domain.ownerc           - owner contact (dict)
    # domain.adminc           - admin contact (dict)
    # domain.techc            - technical contact (dict)
    # domain.zonec            - zone contact (dict)
    # domain.nameServers      - list of name servers (list[dict])
    # domain.period           - registration period (dict)
    # domain.created          - creation date
    # domain.updated          - last update date
    # domain.owner            - owning user (dict)
    # domain.extra            - any unknown/new API fields (dict)

    print(f"{domain.name:30s}  {domain.expire}  {domain.registryStatus}")
```

You can filter and sort with query parameters:

```python
result = client.domain.list(
    {
        "filters": [{"key": "name", "value": "*.com", "operator": "LIKE"}],
        "orders": [{"key": "expire", "type": "ASC"}],
    },
    keys=["status", "expire"],
)
```

## Error handling

```python
from domainrobot import Domainrobot, DomainrobotApiError, DomainrobotTransportError

try:
    client.domain.info("nonexistent.example")
except DomainrobotApiError as e:
    print(f"API error {e.status_code}: {e}")
    print(e.messages)       # list of error message dicts
    print(e.response_body)  # full response body
except DomainrobotTransportError as e:
    print(f"Connection error: {e}")
    print(e.original)       # underlying httpx exception
```

## Custom headers

Every method accepts an optional `headers` parameter:

```python
client.domain.info("example.com", headers={"X-Domainrobot-Demo": "true"})
```
