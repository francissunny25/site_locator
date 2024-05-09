import sys

from src.exception import CustomException
from src.logger import logging

import plotly.express as px
import plotly.io as pio

from shapely.geometry import shape, Point

class AreaPlotter:
    def __init__(self):
        pio.renderers.default = 'svg'

    def ica_area_plotter(self, ica_data, ica_geojson):
        try:
            logging.info('Plotting ICA Area Map')
            map = px.choropleth_mapbox(
                ica_data,
                locations='Area',
                hover_data='Systems Engineer',
                geojson=ica_geojson,
                title='ICA MAP',
                color="Area",
                mapbox_style='carto-positron',
                center={'lat':51.5,
                        'lon':0},
                zoom=7,
                opacity=.5
            )
            return map
        except Exception as e:
            raise CustomException(e, sys)
        
    def site_on_ica_map_plotter(self, map, site, site_cordinates):
        try:
            logging.info('Plotting Site location on map')
            area_map = map.add_scattermapbox(
                lat=[site_cordinates[0]],
                lon=[site_cordinates[1]],
                marker_size=12,
                text=site,
                marker_color='rgb(235,0,100)'
            )
            return area_map
        except Exception as e:
            raise CustomException(e, sys)
        
    def get_ica_details(self, ica_geojson, cordinates):
        try:
            for feature in ica_geojson['features']:
                polygon = shape(feature['geometry'])
                if polygon.contains(Point(cordinates[1], cordinates[0])):
                    return feature
        except Exception as e:
            raise CustomException(e, sys)