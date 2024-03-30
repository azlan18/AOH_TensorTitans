import pickle
from pathlib import path

import streamlit_authenticator as stauth

names = ['Bandhan Sawant', 'Azlan Khawar']
usernames = ['bandhannn','azlan18']
passwords = ['981010AB','887900As']

hashed_password = stauth.Hasher(passwords).generate()
