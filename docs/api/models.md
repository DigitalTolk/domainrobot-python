# Models

All service methods return {class}`~domainrobot.response.DomainrobotResponse` where `data` contains typed model instances. Every model extends {class}`~domainrobot.models.Model` and captures unknown API fields in `extra`.

```python
result = client.domain.info("example.com")
domain = result.data[0]

# Typed attributes with IDE autocompletion
print(domain.name)            # "example.com"
print(domain.registryStatus)  # "ACTIVE"
print(domain.expire)          # "2026-01-01T00:00:00.000+0000"

# Unknown/new fields preserved
print(domain.extra)           # {"someFutureField": "value"}
```

## Base

```{eval-rst}
.. automodule:: domainrobot.models._base
   :members:
   :undoc-members:
```

## Resource models

```{eval-rst}
.. automodule:: domainrobot.models.resources
   :members:
   :undoc-members:
```
