import pandas as pd
import numpy as np

# Ask for the bot's name
bot_name = input("Please enter the name of the bot you want to add extra data to: ")

# Create a new dataframe with extra data
extra_data = pd.DataFrame({
    'IP Address': np.random.choice(['192.168.1.1', '192.168.1.2', '192.168.1.3'], size=100),
    'Port': np.random.choice([22, 80, 443], size=100),
    'Protocol': np.random.choice(['TCP', 'UDP', 'ICMP'], size=100),
    'Vulnerability': np.random.choice([0, 1], size=100)
})

# Save the extra data to a new CSV file
extra_data.to_csv(f'{bot_name}_extra_data.csv', index=False)

print(f"Extra data has been created and saved for bot '{bot_name}'.")