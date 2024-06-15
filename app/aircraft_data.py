# imports
import json

from datetime import datetime, timedelta, timezone
from langchain_community.document_loaders import WikipediaLoader

class AircraftContent:
    def __init__(self, image_path, aircraft_data, callsign):
        self.image_path = image_path
        self.aircraft_data = aircraft_data
        self.callsign = callsign

class AircraftData:

    def __init__(self):
        return

    def invoke(self):
        print('Starting...')
        aircraft_content = self._generate_aircraft_content()

        return aircraft_content
    
    def _generate_aircraft_image(self, aircraft_type):
        image_path = ""

        return image_path

    def _generate_data(self, aircraft_type):
        docs = WikipediaLoader(query=aircraft_type, load_max_docs=1).load()

        return docs
    
    def _generate_aircraft_content(self, aircraft_type):

        CONFIG_PATH = "app/document_sources/aircraft_mock_data.json"
        aircraft = []

        with open(CONFIG_PATH, 'r') as file:
            config_data = json.load(file)
            aircraft = config_data.get('aircraft', [])


        aircraft_content = []
        for craft in aircraft:
            aircraft_type = craft['type']
            callsign = craft['callsign']
            image_path = self._generate_aircraft_image(aircraft_type)
            aircraft_data = self._generate_aircraft_image(aircraft_type)

            aircraft_content.append(AircraftContent(callsign=callsign, image_path=image_path, aircraft_data=aircraft_data))
            
        return aircraft_content
    
    