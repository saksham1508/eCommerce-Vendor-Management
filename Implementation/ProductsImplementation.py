from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        # check if the vendor is logged in, then add the product and return True else Return False
        if (username in VendorSessionModel.vendor_session_db):
            self.product_db[product_name] = {"product_name": product_name,
                                             "product_type": product_type,
                                             "available_quantity": available_quantity,
                                             "unit_price": unit_price
                                             }
            return True
        else:
            return False

    def search_product_by_name(self, product_name):

        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product
        if(product_name in ProductsImplementation.product_db[product_name]):
            return product_name
        else:
            return False


    def get_all_products(self):

        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products
        if (username not in VendorSessionModel.vendor_session_db):
            return false

        elif(username in VendorSessionModel.vendor_session_db):
            return self.product_db