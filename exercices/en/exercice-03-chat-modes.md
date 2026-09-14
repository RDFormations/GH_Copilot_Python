# Exercices — Chat and interaction modes

> **Context** — A date calculation module contains a bug. Tests fail: deadline is sometimes before createdAt.

## Exercice — Ask then Edit on an SLA bug

**Prerequisites :** module 3 read; Copilot Chat ready.

### Instructions

1. Create `src/utils/date_utils.py` avec l échantillon buggy :

```py
from datetime import datetime, timedelta

SLA_HOURS = {"low": 72, "normal": 48, "critical": 4}

def calculate_sla_deadline(created_at: datetime, priority: str) -> datetime:
    hours = SLA_HOURS[priority]
    return created_at - timedelta(hours=hours)  # BUG
```

2. **Ask** — select the function, ask: "Why can deadline be before createdAt?" Note the faulty line.
3. **Ask** — ask for the minimal fix without applying the patch.
4. **Edit** — request: "Add SLA hours to createdAt, do not subtract." Accept diff after review.
5. Verify: createdAt = 2026-01-10T10:00:00Z, normal priority (48 h) → deadline ≈ +48 h.
6. **Bonus** — use `/tests` to generate two test cases.

**Success criteria :** correct Ask diagnosis; Edit fix with addition; manual test OK.

> **Solution** : [Accéder à la correction](../correction/en/correction-03-chat-modes.md)
