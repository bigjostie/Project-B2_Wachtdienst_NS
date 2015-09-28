__author__ = 'Team Cor'

import requests
import codecs

auth_details = ("joshua.rijnders@student.hu.nl", "eHuZFsYeUUKORRWvuUjXdgiuCoUY09R6XuhTBuOp0ZwYiV-fIYACdw")
response = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=auth_details)

def xml(response):
    """
    :param response: het ophalen van de api gegevens (URL)
    :return: Het schrijven naar /gegevens/stations.xml. Dit voor een lokale kopie van alle stations en geo locaties.
    """
    bestand = codecs.open("gegevens/stations.xml", "w", "utf-8")
    bestand.write(response.text)
    bestand.close()

xml(response)

"""
Er moet nog een functie gescreven worden dat de locaties nu automatisch naar de database/csv bestand gaan en hierin worden opgeslagen.
"""