# asteroids
Boot.dev's Course: 6. Build Asteroids

# Prestep to setting up environment
Any dependencies need to be listed in a requirements.txt

# Steps to create environment in WSL:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Steps to create environment in VSCode:
CTRL+SHIFT+P
Python: Create Environment <enter>
Venv: Create Environment <enter>
Python 3.x 64-bit (Microsoft Store)
Check the box for the requirements.txt

# Make sure that your virtual environment is activated when running the game or using the bootdev CLI:
source venv/bin/activate

# To run the game from WSL:
python3 main.py

# to run the game from VSCode:
Open main.py
Hit F5
If it asks you for a debugger, select the option 'Python File'