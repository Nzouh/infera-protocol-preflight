# Infera protocol preflight

A small, dependency-free gate for instrument-ready experiment plans. It checks instrument availability, cumulative reagent inventory, and per-step temperature limits, then writes an inspectable JSON verdict. It complements orchestration; it does not generate protocols or control hardware.

```bash
python audit.py example.json -o report.json
python -m unittest -v
```

The included sample intentionally exits `2` because it contains review cases. Inputs are synthetic. A useful next step would be validating vendor-specific schemas and unit conversions.
