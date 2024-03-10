from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary
        if (username in self.login_data):
            if (self.login_data[username] == password):
                return True
            else:
                return False

    def logout(self, username):

         # Add your code here to log out the current vendor
        if (username in VendorSessionModel.vendor_session_db):

            del VendorSessionModel.vendor_session_db[username]
        return True



