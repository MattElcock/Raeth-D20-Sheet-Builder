from firebase_admin import auth
import collections


class User:
    def __init__(self, user=None):

        if user is None:
            return

        if not isinstance(user, collections.Mapping):
            raise TypeError("You must supply user information within a dict.")

        self.set_email(user.get("email"))
        self.set_email_verified(user.get("email_verified"))
        self.set_phone_number(user.get("phone_number"))
        self.set_password(user.get("password"))
        self.set_display_name(user.get("display_name"))
        self.set_photo_url(user.get("photo_url"))
        self.disable_user()
        self._logged_in = False

    def __getattr__(self, item):
        return None

    def get_email(self):
        return self._email

    def get_email_verified(self):
        return self._email_verified

    def get_phone_number(self):
        return self._phone_number

    def get_display_name(self):
        return self._display_name

    def get_photo_url(self):
        return self._photo_url

    def is_disabled(self):
        return self._disabled

    def set_email(self, email):
        self._email = email
        return email

    def set_email_verified(self, email_verified):
        self._email_verified = email_verified
        return email_verified

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
        return phone_number

    def set_password(self, password):
        self._password = password
        return True

    def set_photo_url(self, photo_url):
        self._photo_url = photo_url
        return photo_url

    def set_display_name(self, display_name):
        self._display_name = display_name
        return display_name

    def disable_user(self):
        self._disabled = True
        return self._disabled

    def enable_user(self):
        self._disabled = False
        return self._disabled

    def create_in_firebase(self):

        try:
            auth.create_user(
                email=self._email,
                email_verified=self._email_verified,
                phone_number=self._phone_number,
                password=self._password,
                display_name=self._display_name,
                photo_url=self._photo_url,
                disabled=self._disabled)

        except ValueError as e:
            return None, str(e)

        except:
            print("Something went wrong")
