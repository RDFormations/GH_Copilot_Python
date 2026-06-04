#!/usr/bin/env bash
gen_50_args_line() {
  python3 - <<'PY'
import random
print(" ".join(map(str, random.sample(range(1, 100_001), 50))))
PY
}
