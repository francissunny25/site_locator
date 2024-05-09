import sys

from src.exception import CustomException
from src.logger import logging

from geopy.geocoders import ArcGIS
from OSGridConverter import latlong2grid

class GetSiteGridDetails:
    def __init__(self):
        self.nom = ArcGIS()

    def get_cordinates(self, postcode):
        try:
            logging.info('Retrieving Site Cordinates')
            latitude, longitude = self.nom.geocode(postcode)[1]
            return latitude, longitude
        except Exception as e:
            raise CustomException(e,sys)

    def get_grid_details(self, postcode):
        try:
            logging.info('Retrieving Site Grid Reference')
            latitude, longitude = self.get_cordinates(postcode)
            grid_reference = latlong2grid(latitude, longitude)
            return grid_reference
        except Exception as e:
            raise CustomException(e, sys)