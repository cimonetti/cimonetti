"""Regression checks for the corrected original notebook functions."""
from pathlib import Path
import json, unittest
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import detrend
from scipy import signal

plt.show = lambda: plt.close('all')
ROOT = Path(__file__).resolve().parents[1]

def function_cell(prefix, cell):
    path = next((ROOT/'notebooks').glob(prefix+'*.ipynb'))
    notebook = json.loads(path.read_text())
    namespace = {'np': np, 'plt': plt, 'detrend': detrend, 'signal': signal}
    exec(''.join(notebook['cells'][cell]['source']), namespace)
    return namespace

class Corrections(unittest.TestCase):
    def test_original_spectral_frequency_and_constant(self):
        function = function_cell('Análise', 5)['analiseespectral']
        data = np.sin(2*np.pi*np.arange(1000)/10)
        _, median, dominant, f95 = function(data)
        self.assertAlmostEqual(dominant, 1)
        self.assertAlmostEqual(median, 1)
        self.assertGreaterEqual(f95, median)
        values = function(np.ones(100))
        self.assertEqual(values[0], 0)
        self.assertTrue(np.isnan(values[1:]).all())

    def test_original_force_spectrum_constant_and_nyquist_guard(self):
        namespace = function_cell('FIltragem', 3)
        responses = iter(['10', 's'])
        namespace['input'] = lambda prompt: next(responses)
        function = namespace['analiseespectral_residual']
        data = np.column_stack((np.arange(200)/10, np.ones((200,3))))
        result = function(data)
        for values in result.values():
            self.assertEqual(values['forca_total'], 0)
            self.assertTrue(np.isnan(values['freqMediana']))

    def test_knee_loop_geometry_and_zero_length(self):
        function = function_cell('Calculo', 2)['calculaAngulo_joelho']
        data=np.array([[0,0,1,0,0,0,0,0,-1,0], [1,0,1,0,0,0,0,1,0,0], [2,0,0,0,0,0,0,0,-1,0]])
        _, angle = function(data)
        np.testing.assert_allclose(angle[:2], [180,90])
        self.assertTrue(np.isnan(angle[2]))

    def test_cycles_use_argument_and_empty_valleys(self):
        namespace = function_cell('Calculo', 5)
        self.assertEqual(namespace['calcula_ciclos']([3,7,10]), [(3,7),(7,10)])
        peaks, valleys = namespace['detect_picos_vales']([1,2,3,4])
        self.assertEqual(peaks, [])
        self.assertEqual(valleys, [])

if __name__ == '__main__': unittest.main()
