import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Transfer function coefficients
numerator = [10]

# Define the two polynomials as lists of coefficients
poly1 = [1, 100]
poly2 = [0.25, 0.4, 1]

# Multiply the two polynomials using numpy.polymul
denominator = np.polymul(poly1, poly2)

# Create the transfer function
transfer_function = ctrl.TransferFunction(numerator, denominator)

# Bode plot
plt.figure()
mag, phase, omega = ctrl.bode_plot(transfer_function, dB=True)

# Gain and phase margins
gm, pm, wg, wp = ctrl.margin(transfer_function)
print(f"Gain margin: {gm:.4f} at frequency {wg:.4f} rad/s")
print(f"Phase margin: {pm:.4f} at frequency {wp:.4f} rad/s")

plt.show()
