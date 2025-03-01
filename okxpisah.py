import json
import os
import subprocess

# Path to the wallets.json file
WALLETS_FILE = "wallets.json"

# Function to insert a 4-space line break every 1,000 items
def format_data(items):
    formatted_data = []
    for i, item in enumerate(items, 1):
        formatted_data.append(item)
        if i % 1000 == 0:
            formatted_data.append("    ")  # Add 4-space line break
    return "\n".join(formatted_data)

# Read data from wallets.json
try:
    with open(WALLETS_FILE, 'r') as f:
        wallets = json.load(f)
except FileNotFoundError:
    print(f"Error: {WALLETS_FILE} not found. Please ensure the file exists.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: {WALLETS_FILE} is not a valid JSON file.")
    exit(1)

# Extract private keys and mnemonics
private_keys = [wallet['privateKey'] for wallet in wallets]
mnemonics = [wallet['mnemonic'] for wallet in wallets]

# Format private keys and mnemonics
formatted_private_keys = format_data(private_keys)
formatted_mnemonics = format_data(mnemonics)

# Write private keys to privatekey.txt
with open('privatekey.txt', 'w') as f:
    f.write(formatted_private_keys)

# Write mnemonics to mnemonic.txt
with open('mnemonic.txt', 'w') as f:
    f.write(formatted_mnemonics)

# Send a Mac OS notification
notification_title = "Script Completed"
notification_message = "Private keys and mnemonics have been extracted to privatekey.txt and mnemonic.txt."
subprocess.run([
    'osascript', '-e',
    f'display notification "{notification_message}" with title "{notification_title}"'
])

print("Private keys and mnemonics have been extracted to privatekey.txt and mnemonic.txt respectively.")