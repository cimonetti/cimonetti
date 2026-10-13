# Implementation history

The starting material was the five Python notebooks supplied by Vítor Cimonetti. The source of this edition was reconstructed directly from those uploads, discarding the previous refactor.

Names, comments, informal notes, `for` and `while` loops, original function organization, plotting structure and input-loading cells are retained. Source edits are limited to six cells:

- Spectral notebook, cell 5: bound the cumulative-integration loops, correct the frequency index after the loop counter is incremented, reject unusable input and return NaN for descriptors of zero spectral power.
- Filtering notebook, cell 3: apply the same frequency-index/zero-power corrections, check the sampling rate and expected signals, and skip design cutoffs at or above Nyquist.
- Smoothing notebook, cell 4: correct the span label from seconds to a fraction and the saved time-column header from Frame to Tempo. Derivatives and the span sweep remain unchanged.
- Knee notebook, cell 2: keep the per-frame loop, handle zero-length segments and clip the arccos argument to [-1,1].
- Knee notebook, cell 5: allow no valleys and use the supplied `vales_filtrados` argument instead of the global `vales` variable; move the export out of this cell.
- Knee notebook, cell 6: export only after `minimos` and `maximos` have been calculated.

The exercise notebook has unchanged source cells. All notebooks have saved outputs and execution counts cleared, and environment metadata cleaned. Separate synthetic data files make the original loading cells executable without distributing participant recordings. Documentation, examples and tests are separate additions. The exact source changes appear in `docs/correcoes.diff`.

AI assistance was used for these corrections and packaging. Checks made during preparation must not be described as checks independently performed by the account owner. The uploaded originals were not overwritten.
