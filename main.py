from src.logger import logging

from src.components.config_helper import Config
from src.components.get_site_details import GetSiteGridDetails
from src.components.area_plotter import AreaPlotter

if __name__ == "__main__":
    config_object = Config()
    site_grid_details = GetSiteGridDetails()
    area_plotter = AreaPlotter()

    logging.info('Collecting data from the user')
    site_postcode = config_object.read_config('config.json')['postcode']
    site_name = config_object.read_config('config.json')['sitename']
    logging.info(f'Site Postcode: {site_postcode}')

    logging.info('Retrieving Sites Grid Reference details')
    grid_reference = site_grid_details.get_grid_details(site_postcode)
    logging.info(f'Grid Reference: {grid_reference}')
    logging.info(f'Grid Eastling: {grid_reference.E}')
    logging.info(f'Grid Northling: {grid_reference.N}')

    logging.info('Retrieving Site Cordinate details')
    site_cordinates = site_grid_details.get_cordinates(site_postcode)

    logging.info('Reading Map configs')
    ica_regions = config_object.read_config('uk.geojson')
    logging.info('Reading ICA Data')
    ica_data = config_object.read_csv('area_ica.csv')

    logging.info('Plotting ICA Areas')
    ica_area_map = area_plotter.ica_area_plotter(ica_data, ica_regions)

    logging.info('Plotting Site on ICA Map')
    #TODO save the image as jpg
    area_plotter.site_on_ica_map_plotter(ica_area_map, site_name, site_cordinates)

    logging.info('Retrieving ICA Area and ICA Engineer details from map')
    ica_details = area_plotter.get_ica_details(ica_regions, site_cordinates)
    
    ica_info = {'Area': ica_details['properties']['area'],
                'Area Engineer': ica_details['properties']['area_ica']}
    
    logging.info('Storing the result')
    config_object.write_json(ica_info, 'ica_details.json')