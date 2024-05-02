from src.logger import logging

from src.components.config_reader import ConfigReader
from src.components.get_site_details import GetSiteGridDetails

if __name__ == "__main__":
    logging.info('Collecting data from the user')
    config_reader = ConfigReader()
    site_postcode = config_reader.read_config()['postcode']
    logging.info(f'Site Postcode: {site_postcode}')
    logging.info(f'Retrieving Sites Grid Reference details')
    site_grid_details = GetSiteGridDetails()
    grid_reference = site_grid_details.get_grid_details(site_postcode)
    logging.info(f'Grid Reference: {grid_reference}')
    logging.info(f'Grid Eastling: {grid_reference.E}')
    logging.info(f'Grid Northling: {grid_reference.N}')