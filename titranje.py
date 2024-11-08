import Gušenotitranje as harm
import matplotlib.pyplot as plt
import numpy as np

My_oscillator=harm.HarmonicOscillator(5,0.1,0,0.5,0.12,0.03)
My_oscillator.oscillate1(7,0.01)
My_oscillator.oscillate2(7,0.01)
My_oscillator.plot_trajectory()
My_oscillator.reset()
