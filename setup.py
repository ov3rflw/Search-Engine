'''
SETUP FOR SEARCH ENGINE BETA
'''
import subprocess, sys

def installation():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    USER = input('Install "SecLists" ? (Y/N): ').lower()
    if USER == 'y': 
        process = subprocess.Popen(["git", "clone", "https://github.com/danielmiessler/SecLists.git"])
    else: 
        print('Installation finish')

installation() 