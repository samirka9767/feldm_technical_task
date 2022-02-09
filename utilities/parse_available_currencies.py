import os
from xml.etree import ElementTree as ET

file_name = "eurofxref-hist-90d.xml"
full_file = os.path.abspath(os.path.join('currency_data', file_name))

tree = ET.parse(full_file)
root = tree.getroot()


def find_usd_rate(time):
    for child in root[2]:
        if child.attrib['time'] == time:
            return child[0].attrib['rate']
    return -1
