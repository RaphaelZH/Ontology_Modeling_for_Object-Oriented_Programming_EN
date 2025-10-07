import neurokit2 as nk
import matplotlib.pyplot as plt

# Simulate an ECG signal
# duration: length of the signal in seconds
# sampling_rate: number of samples per second
# heart_rate: average heart rate in beats per minute
# noise: amount of noise to add (0 to 1)
simulated_ecg = nk.ecg_simulate(duration=10, sampling_rate=250, heart_rate=70, noise=0.05)

# Visualize the simulated signal
#plt.figure(figsize=(10, 4))
#plt.plot(simulated_ecg)
#plt.title("Simulated ECG Signal")
#plt.xlabel("Sample Number")
#plt.ylabel("Amplitude")
#plt.show()

print(simulated_ecg)
print(len(simulated_ecg))