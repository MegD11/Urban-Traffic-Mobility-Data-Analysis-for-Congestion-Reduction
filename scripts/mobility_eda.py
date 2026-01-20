import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and prepare data
file_path = "../data/Exp_3_VBOX_Data.xlsx"
sheets = ['7', '8', '9']
df = pd.concat([pd.read_excel(file_path, sheet_name=s) for s in sheets])

df = df[['Speed (kmph)', 'Time']].dropna()
df['Time'] = df['Time'].astype(int)

# Group by time and calculate average speed
avg_speed = df.groupby('Time')['Speed (kmph)'].mean().reset_index()

# Plot average speed trend
plt.figure(figsize=(9,5))
sns.lineplot(data=avg_speed, x='Time', y='Speed (kmph)')
plt.xlabel("Time")
plt.ylabel("Average Speed (kmph)")
plt.title("Average Vehicle Speed Over Time")
plt.tight_layout()

# Save plot
plt.savefig("../visuals/average_speed_by_time.png")
plt.show()
