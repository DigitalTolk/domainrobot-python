# Quick start

## Installation

```bash
pip install domainrobot
```

## Basic usage

```python
from domainrobot import Domainrobot

with Domainrobot(username="user", password="pass", context=4) as client:
    result = client.domain.info("example.com")
    print(result.data)
```

## Error handling

```python
from domainrobot import Domainrobot, DomainrobotApiError, DomainrobotTransportError

try:
    client.domain.info("nonexistent.example")
except DomainrobotApiError as e:
    print(f"API error {e.status_code}: {e}")
except DomainrobotTransportError as e:
    print(f"Connection error: {e}")
```
