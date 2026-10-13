# Validation during portfolio preparation

Checked on 12 October 2026 with Python 3.12, NumPy 2.3.5, Matplotlib 3.10.8 and Streamlit 1.65.0.

- Three automated tests passed: all 22 extracted curves against an independently defined column/block/sign layout with unequal right/left cycle counts; consistent exclusion across all segments and rejection of removing all cycles of a side; mean and sample SD against known values.
- The included command-line example generated right and left PNG/SVG figures, a comparison figure and numerical output arrays.
- Streamlit AppTest initialized the app without exceptions and displayed its four tabs and synthetic reference selector. This is an initialization check; file-upload and mouse interactions were not exercised.
- The comparison PNG used in the README was visually inspected.

```bash
python -m unittest discover -s tests -v
python marcha.py
```

MATLAB was unavailable. The MATLAB importer and demo have not been executed, and Python checks do not demonstrate MATLAB compatibility. No patient data were processed in these public examples, and the synthetic reference has no normative or clinical interpretation.

These checks were performed while preparing the portfolio with AI assistance, not independently by the account owner.
