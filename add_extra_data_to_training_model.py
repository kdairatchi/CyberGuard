import pandas as pd

# Ask for the bot's name
bot_name = input("Please enter the name of the bot you want to add extra data to: ")

# Load the original training data
original_data = pd.read_csv('data.csv')

# Load the extra data
extra_data = pd.read_csv(f'{bot_name}_extra_data.csv')

# Concatenate the original data with the extra data
new_data = pd.concat([original_data, extra_data])

# Save the new data to a new CSV file
new_data.to_csv(f'{bot_name}_new_data.csv', index=False)

print(f"Extra data has been added to the training model for bot '{bot_name}'.")
