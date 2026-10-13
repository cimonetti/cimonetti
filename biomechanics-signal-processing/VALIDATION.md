# Validation during portfolio preparation

Revised on 12 October 2026, local Brazil date, with Python 3.12, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8, pandas 2.2.3 and scikit-misc 0.5.3.

Four regression tests passed for the retained notebook functions: known spectral frequency and constant-signal handling; constant force spectra and cutoff/Nyquist handling; straight/right-angle/zero-length geometry using the original per-frame loop; cycle arguments without reliance on globals and an empty-valley case.

All five notebooks' calculation and plotting cells ran sequentially in a fresh Python process per notebook, using the supplied synthetic files. The original `!pip install scikit-misc` line was not run by that runner; its installed dependency was imported successfully. The full original LOESS span sweep and original finite-difference derivatives were executed. Notebook JSON was validated separately.

```bash
python -m unittest discover -s tests -v
```

Interactive Jupyter/kernel behavior was not verified: the environment restricts kernel sockets. The source-cell check establishes code execution with installed dependencies, not browser behavior. No patient data or experimental ground truth were used. These checks were made during preparation with AI assistance, not independently by the account owner.
