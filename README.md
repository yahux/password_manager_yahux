_____.___.      .__                                                                       .___                                            __                
\__  |   |____  |  |__  __ _____  ___ ___________    ______ ________  _  _____________  __| _/    ____   ____   ____   ________________ _/  |_  ___________ 
 /   |   \__  \ |  |  \|  |  \  \/  / \____ \__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |    / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
 \____   |/ __ \|   Y  \  |  />    <  |  |_> > __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |   / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 / ______(____  /___|  /____//__/\_ \ |   __(____  /____  >____  >  \/\_/ \____/|__|  \____ |   \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|   
 \/           \/     \/            \/ |__|       \/     \/     \/                          \/  /_____/      \/     \/     \/           \/                   

A Python-based security tool that generates cryptographically secure passwords and checks them against the **Have I Been Pwned** database using **k-Anonymity**.

## 🚀 Features

- **Secure Generation:** Uses the `secrets` module for high-entropy randomness.

- **Privacy First:** Implements k-Anonymity; your password is never sent over the internet.

(🛡️ How k-Anonymity Works: This script hashes your password locally. 
It only sends the first 5 characters of the SHA-1 hash to the API. 
The API returns a list of matching suffixes, and the script identifies matches locally. 
Your plain-text password and full hash never leave your machine.)

- **API Integration:** Connects to the Have I Been Pwned (HIBP) REST API.


## 🛠️ Windows Installation

1. Clone the repo:

   ```bash

   git clone https://github.com/yahux/password_manager_yahux.git](https://github.com/yahux/password_manager_yahux.git)

*** Make sure you are in the script file directory ***

# Install dependencies

This is very important for the script to work. 

(** python -m pip install -r requirements.txt **)

if not working try (** py -m pip install -r requirements.txt **)

2. Run the code using:


Python password_manager_yahux.py 


## 🛠️ Linux Installation (Ubuntu/Debian/Kali)

1. Clone the repo:

git clone (https://github.com/yahux/password_manager_yahux.git)

*** Make sure you are in the script file directory ***

cd password_manager_yahux

# Install dependencies

This is very important for the script to work. 

(** sudo apt install python3-pip **)

(** pip3 install -r requirements.txt **)

If you get a "Permissions" error, try: (** pip3 install -r requirements.txt --user **)

2. Run the code using:


Python password_manager_yahux.py 


**linux chmod**

chmod +x password_manager_yahux.py && ./password_manager_yahux.py

