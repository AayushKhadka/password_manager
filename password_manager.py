import json

# Try to load existing passwords from file
# If file doesn't exist yet, start with empty dictionary
try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
    print("Loaded existing passwords!")
except:
    passwords = {}
    print("Starting fresh!")

# Add a new password
passwords["instagram.com"] = {
    "username": "ayush01",
    "password": "ayush123"
}

# Save to file
with open("passwords.json", "w") as file:
    json.dump(passwords, file)

print("Saved! Passwords:", passwords)