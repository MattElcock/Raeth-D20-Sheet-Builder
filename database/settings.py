import firebase_admin
import logging
from firebase_admin import credentials

def login_to_firebase():
    """A funtion which attempts to login to the Firebase console, enabling
    SDK functions.

    :returns:
        Boolean - True if login successful, False otherwise.
    """
    try:
        cred = credentials.Certificate("firebase_creds.json")
        firebase_admin.initialize_app(cred)
    except FileNotFoundError:
        logging.critical("Cannot connect to Firebase; could not find credentials.")
        return False
    except:
        logging.critical("There was an unknown error connecting to Firebase")
        return False
    else:
        logging.info("🔑 Successfully logged into Firebase")
        return True