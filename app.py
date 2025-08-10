import numpy as np
import matplotlib.pyplot as plt
from math import gamma, factorial
import streamlit as st


st.title("Growth Comprassion Visualization")

max_n = st.slider("Select n value", 10, 140, 100)


n = np.linspace(1, max_n, 140)  
n_values = np.arange(1, max_n + 1)  

gamma_vals = np.vectorize(gamma)(n + 1)
factorial_vals = np.array([factorial(i) for i in n_values])
stirling_approx = (n / np.e) ** n

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(n, gamma_vals, '--', label='Γ(n+1)', color='navy', linewidth=2.2)  
ax.plot(n_values, factorial_vals, '-', label='Factorial (n!)', color='red', linewidth=1.5)  
ax.plot(n, stirling_approx, '-', label="Stirling's Approximation", color='gray', linewidth=2.1) 


ax.set_title(f' n={max_n}')
ax.set_xlabel('n')
ax.set_ylabel('Value')
ax.set_yscale('log')  
ax.legend()
ax.grid(True, alpha=0.2)

st.pyplot(fig)
