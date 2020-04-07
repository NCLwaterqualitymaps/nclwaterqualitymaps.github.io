# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:28:56 2020

@author: lazen
"""
import csv


csv_path = 'Master_Data.csv'
output_path = 'data/Results_1.js'

template_start = 'var json_Results_1 = { "type": "FeatureCollection",\n "name": "Results_1",\n "crs": { "type": "name",\n "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }\n,"features": [\n'
template_end = ']}'

output = template_start

with open(csv_path, 'r') as csv_file_obj:
    csv_reader = csv.reader(csv_file_obj)
    csv_contents = [row for row in csv_reader]

lats, lons = [], []

for enum, row in enumerate(csv_contents):
    if enum == 0:
        continue
    Sample_ID, lon, lat = row[0], row[6], row[5] #row = column for some reason
    lats.append(lat)
    lons.append(lon)
    print(Sample_ID)
    date = row[1]
    Sampling_date = row[1]
    Sample_description = row[4]
    Sample_type = row[4] # was source
    Sample_type = Sample_type.replace(" ", "").lower() #takes out spaces from sample description
    Location_ID = row[2]
    Contaminants = row[51] # was problem 
    Symptoms = row[53] # was Desc
    Treatments = row[52] # was advice


    feature = "{" + '"type": "Feature", "properties": {{"Sample_ID": "{}", "Sampling_date": "{}", "Sample_description":"{}", "Sample_type":"{}", "Contaminants":"{}", "Treatments":"{}", "Symptoms":"{}" }}, "geometry": {{ "type": "Point", "coordinates": [ {}, {} ] }}\n'.format(Sample_ID, Sampling_date, Sample_description, Sample_type, Contaminants, Treatments, Symptoms, lon, lat) + "}"


    if enum == 1:
        output = output + feature
    else:
        output = output + ',' + feature

maxLat, maxLon = max(lats), max(lons)
minLat, minLon = min(lats), min(lons)

output = output + template_end

with open(output_path, "w") as of:
    of.write(output)


with open('index.html', 'r') as file:
     #read a list of lines into data
    webmap_index = file.read().splitlines()
webmap_index[39] = "        }}).fitBounds([[{},{}],[{},{}]]);".format(minLat, minLon, maxLat, maxLon)
print(minLat, minLon, maxLat, maxLon)
with open('index.html', 'w', newline='\n') as file:
    file.writelines((s + '\n' for s in webmap_index))
