import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.signal import find_peaks
import numpy as np
import wave
import math

click_rec = wave.open('MaBo_2.wav', 'r')

#Extract Raw Audio from Wav File
signal = click_rec.readframes(-1)
signal = np.frombuffer(signal, dtype='int16')
fs = click_rec.getframerate()


plt.figure(1)
plt.title('Signal Wave of the tone')
plt.xlabel('Number of sample')
plt.ylabel('Amplitude')
#plt.plot(abs(signal))
# plt.show()

# Calculate energy of the signal  https://stackoverflow.com/questions/29429733/cant-find-the-right-energy-using-scipy-signal-welch
signalabs=abs(signal)

i = 0
sum_x = 0

while i < len(signalabs)-100:
    sum_x = 0
    j = 0
    while j < 100:
        sum_x = sum_x + signalabs[i+j]
        j += 1
    
    signalabs[i] = sum_x/100
    i=i+1 

# Plot the graph with signal energy
plt.figure(1)
plt.title('Energy')
plt.xlabel('Number of sample')
plt.ylabel('Amplitude')
plt.plot(signalabs)
plt.plot()
plt.show()

"# thesis" 
