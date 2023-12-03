import matplotlib.pyplot as plt
z = 3 + 2j  
plt.figure(figsize=(6, 6))
plt.scatter(z.real, z.imag, color='red', label='Complex Number')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Plot of a Complex Number')
plt.legend()
plt.grid(True)
plt.show()
