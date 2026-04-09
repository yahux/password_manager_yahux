import hashlib   # Library to create SHA-1 hashes (required by the HIBP API)
import requests  # Library to handle the internet connection and data retrieval
import secrets   # Library for generating high-security random characters
import string    # Library to access sets of characters like letters and digits

def generate_password(length=20):
    """Generates a cryptographically secure random password."""
    # Define the pool of characters: Letters (upper/lower), Digits, and Symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Securely select random characters and join them into a single string
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

def check_pwned_api(password):
    """Checks if a password has been leaked using k-Anonymity privacy."""
    # Step 1: Hash the password and convert it to uppercase hex
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Step 2: Split the hash into the first 5 chars (prefix) and the rest (tail)
    prefix, tail = sha1_password[:5], sha1_password[5:]
    
    # Step 3: Send only the prefix to the HIBP API (protects your identity)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Could not connect to HIBP API. Status: {response.status_code}")

    # Step 4: Search the results for our specific hash tail
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count) # Found! Return the number of times it was leaked
            
    return 0 # Not found! The password is clean.

def main():
    """Execution starts here."""
    # Print your custom ASCII art using a 'Raw' triple-quoted string
    print(r"""
  _____.___.      .__                                                                .___                                            __                
  \__  |   |____  |  |__  __ _____  ___ ___________    ______ ________  _  _____________  __| _/    ____    ____   ____   ________________ _/  |_  ___________ 
   /   |   \__  \ |  |  \|  |  \  \/  / \____ \__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |    / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
   \____   |/ __ \|  |  Y  \  |  />    <  |  |_> > __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |   / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
   / ______(____  /___|  /____//__/\_ \ |   __(____  /____  >____  >  \/\_/ \____/|__|  \____ |   \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|   
   \/            \/     \/            \/ |__|        \/     \/     \/                          \/  /_____/      \/     \/     \/          \/                  
    """)
    
    # Generate a secure 20-character password
    new_pass = generate_password(20)
    print(f"PASSWORD GENERATED: {new_pass}")
    print("-" * 50)
    print("Checking database for security leaks...")
    
    try:
        # Check the password against Have I Been Pwned
        pwn_count = check_pwned_api(new_pass)
        
        if pwn_count > 0:
            print(f"⚠️  STATUS: BREACHED! This password appeared {pwn_count} times in leaks.")
            print("ADVICE: Run the script again to get a different password.")
        else:
            print("✅ STATUS: SECURE. No matches found in the breach database.")
            
    except Exception as e:
        print(f"❌ ERROR: {e}")

# Boilerplate to ensure the script runs only when executed directly
if __name__ == "__main__":
    main()