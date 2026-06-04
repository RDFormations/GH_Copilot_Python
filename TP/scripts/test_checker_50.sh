#!/usr/bin/env bash
# Lance push_swap | checker avec 50 valeurs aléatoires.
# Usage : ./scripts/test_checker_50.sh [nombre_de_tests]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TP_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
# shellcheck source=gen_50_args.sh
source "$SCRIPT_DIR/gen_50_args.sh"

cd "$TP_DIR"

PUSH_SWAP="${PUSH_SWAP:-python3 src/push_swap.py}"
CHECKER="${CHECKER:-python3 checker.py}"
RUNS="${1:-${RUNS:-1}}"

if ! [[ "$RUNS" =~ ^[1-9][0-9]*$ ]]; then
  echo "Usage: $0 [nombre_de_tests]" >&2
  exit 1
fi

echo "=== push_swap | checker — $RUNS test(s) à 50 valeurs ==="
echo "push_swap : $PUSH_SWAP"
echo "checker   : $CHECKER"
echo

ok=0
fail=0

for ((i = 1; i <= RUNS; i++)); do
  args="$(gen_50_args_line)"
  # shellcheck disable=SC2086
  if ! result="$($PUSH_SWAP $args 2>/dev/null | $CHECKER $args 2>/dev/null | tr -d '\r')"; then
    echo "Test $i/$RUNS : FAIL (push_swap ou checker en erreur)"
    fail=$((fail + 1))
    continue
  fi
  if [[ "$result" != "OK" ]]; then
    echo "Test $i/$RUNS : FAIL ($result)"
    fail=$((fail + 1))
  else
    echo "Test $i/$RUNS : OK"
    ok=$((ok + 1))
  fi
done

echo
echo "Résultat : $ok OK, $fail FAIL sur $RUNS test(s)"
[[ "$fail" -eq 0 ]]
