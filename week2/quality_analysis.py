import matplotlib.pyplot as plt
import numpy as np

# Labels for the 8 characteristics
labels = [
    'Functional Suitability', 'Performance Efficiency', 'Compatibility', 
    'Usability', 'Reliability', 'Security', 'Maintainability', 'Portability'
]

# Weights as defined in the Lab Manual
weights = [0.15, 0.12, 0.10, 0.15, 0.15, 0.15, 0.08, 0.10]

# --- UPDATE THESE ARRAYS WITH YOUR REAL RATINGS ---
APP1_RATINGS = [5, 4, 4, 5, 5, 4, 4, 3] # WhatsApp
APP2_RATINGS = [4, 3, 4, 3, 4, 3, 4, 5] # Messenger

# Calculate Weighted Scores
app1_weighted = sum([rating * weight for rating, weight in zip(APP1_RATINGS, weights)])
app2_weighted = sum([rating * weight for rating, weight in zip(APP2_RATINGS, weights)])

print(f"WhatsApp Weighted Score: {app1_weighted:.2f}")
print(f"Messenger Weighted Score: {app2_weighted:.2f}")

# Radar Chart Setup
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
APP1_RATINGS += APP1_RATINGS[:1]
APP2_RATINGS += APP2_RATINGS[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot App 1
ax.plot(angles, APP1_RATINGS, color='green', linewidth=2, label=f'WhatsApp ({app1_weighted:.2f})')
ax.fill(angles, APP1_RATINGS, color='green', alpha=0.25)

# Plot App 2
ax.plot(angles, APP2_RATINGS, color='blue', linewidth=2, label=f'Messenger ({app2_weighted:.2f})')
ax.fill(angles, APP2_RATINGS, color='blue', alpha=0.25)

ax.set_yticklabels([1, 2, 3, 4, 5])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title('ISO 25010 Quality Profile: WhatsApp vs Facebook Messenger', size=15, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save the plot
plt.savefig('quality_radar_WhatsApp_Messenger.png', bbox_inches='tight')
print("Radar chart saved successfully as quality_radar_WhatsApp_Messenger.png")