# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:54:57 2020

@author: lazen
"""

#Cell 1

import pandas as pd


#Cell 2

#read in excel - Shift+right click the excel file and select 'copy as path'
# Insert below in form = r"file_path"
# Note - Will not read in spreadsheet if open in excel


#input
excel_path = r"Excel_Results\Results_Template.xlsx"

#output
#....................r".folder..\...File_name.csv...."
csv_save_location = r"CSV_Results\csv_results_07042020.csv"



#if multiple sheets in excel file, this will extract relevant sheet
#input name of sheet in form => sheet_name = "Name_of_sheet"
#Note- The results_template sheet is "source"

alldata_excel = pd.read_excel (excel_path, sheet_name = "source")



#Cell 3

#Organise master dataframe (table of data)

#This changes the title
alldata_df = alldata_excel


#Replace spaces in titles with underscores
column_names = alldata_df.columns.str.replace(' ', '_')


#delete first 4 rows so that only site information is included
alldata_df = alldata_excel.iloc[4:,]


#set column titles
alldata_df.columns = column_names

#index dataframe
index_df = pd.DataFrame(alldata_df.Sample_ID)
index_df.reset_index(inplace = True, drop=True)

#Sets Sample ID as the index
alldata_df.set_index("Sample_ID", inplace = True)

#This will show the dataframe below - Jupyter
#alldata_df





#Cell 4

#This cell contains the information used in order to build a function to perform the limit check against your results

#Note - contaminants haven't been included that WHO consider "not to be of health concerns at levels likley to be found"

#This points the function towards the correct column in the dataframe
faecal_result = alldata_df.Faecal_Coliforms
aluminium_result = alldata_df.Aluminium
antimony_result = alldata_df.Antimony
arsenic_result = alldata_df.Arsenic
barium_result = alldata_df.Barium
bromide_result = alldata_df.Bromide
cadmium_result = alldata_df.Cadmium
calcium_result = alldata_df.Calcium
chloride_result = alldata_df.Chloride
chromium_result = alldata_df.Chromium
copper_result = alldata_df.Copper
fluoride_result = alldata_df.Fluoride
iron_result = alldata_df.Iron
lead_result = alldata_df.Lead
manganese_result = alldata_df.Manganese
nickel_result = alldata_df.Nickel
nitrate_result = alldata_df.Nitrate
nitrite_result = alldata_df.Nitrite
sodium_result = alldata_df.Sodium
strontium_result = alldata_df.Strontium
sulphate_result = alldata_df.Sulphate


#Limits according to WHO Guidelines
#Units = mg/l

faecal_limit = 0.0
aluminium_limit = 0.2
antimony_limit = 0.02
arsenic_limit = 0.01
barium_limit = 1.3
bromide_limit = 6
cadmium_limit = 0.003
calcium_limit = 100 #Taste threshold
chloride_limit = 250 #Taste threshold
chromium_limit = 0.05
copper_limit = 2
fluoride_limit = 1.5
iron_limit = 2 #Taste threshold
lead_limit = 0.01
manganese_limit = 0.4
nickel_limit = 0.07
nitrate_limit = 50
nitrite_limit = 3
sodium_limit = 200 #Taste threshold
strontium_limit = 4
sulphate_limit = 500

#   NOTE: There is no WHO guidance regarding; Ammonium, magnesium, phosphate & zinc -
#   the levels likely to be found in drinking water are well below an unsafe amount


# If limit is exceeded then print the following in the results:

faecal_exc = "High faecal coliform count; "
aluminium_exc = "High aluminium level; "
antimony_exc = "High antimony level; "
arsenic_exc = "High arsenic level; "
barium_exc = "High barium level; "
bromide_exc = "High bromide level; "
cadmium_exc = "High cadmium level; "
calcium_exc = "High calcium level; "
chloride_exc = "High chloride level; "
chromium_exc = "High chromium level; "
copper_exc = "High copper level; "
fluoride_exc = "High fluoride level; "
iron_exc = "High iron level; "
lead_exc = "High lead level; "
manganese_exc = "High manganese level; "
nickel_exc = "High nickel level; "
nitrate_exc = "High nitrate level; "
nitrite_exc = "High nitrite level' "
sodium_exc = "High sodium level; "
strontium_exc = "High strontium level; "
sulphate_exc = "High sulphate level; "


# These are the treatment methods that will be shown in final results

faecal_treatment = "Faecal treatment - Heat water to a rolling boil and then allow to cool naturally, chemical disinfection, coagulation, distillation, reverse osmosis, slow sand filtration or solar disinfection; "
aluminium_treatment = "Aluminium can be treated at home by point of use reverse osmosis and distillation; " #http://www.purewateroccasional.net/wtialuminum.html
antimony_treatment = "Antimony is not reduced from water by conventional treatment processes - must be controlled at the source, i.e old plumbing fittings may cause contamination; "
arsenic_treatment = "Arsenic can be reduced using coagulation, ion exchange or reverse osmosis; "
barium_treatment = "Barium can be reduced with the using ion exchange or lime softening; "
bromide_treatment = "Bromide can be reduced using granular activated carbon or reverse osmosis; "
cadmium_treatment = "Cadmium can be reduced using coagulation/filtration, lime softening and point of use reverse osmosis; "   #https://www.freedrinkingwater.com/water-contamination/cadmium-contaminants-removal-water-page2.htm
calcium_treatment = "Calcium can be reduced using a water softener or point of use reverse osmosis; " #https://www.kent.co.in/blog/remove-calcium-and-magnesium-in-hard-water-with-water-softener/
chloride_treatment = "Chloride can be reduced using reverse osmosis, distillation or ion exchange; "
chromium_treatment = "Chromium can be reduced using coagulation; "
copper_treatment = "Copper can be reduced by removing the source of the contamination; "
fluoride_treatment = "Fluoride can be reduced using activated alumina and other coagulants; "
iron_treatment = "Iron can be reduced by using aeration or ion exchange; "
lead_treatment = "Lead is incredibly difficult to remove so alternative water should be found; "
manganese_treatment = "Manganese levels can be reduced using aeration or ion exchange; "
nickel_treatment = "Nickel can be reduced through coagulation or ion exchange; "
nitrate_treatment = "Nitrate can be reduced through ion exchange; "
nitrite_treatment = "Nitrite can be reduced through ion exchange; "
sodium_treatment = "Sodium can be reduced through distillaton, ion exchange and reverse osmosis; "
strontium_treatment = "Strontium can be reduced through ion exchange; "
sulphate_treatment = "Sulphate can be reduced through ion exchange ; "

# These are the symptoms that will be printed in the final results

faecal_sym = "Faecal contamination can include vomiting and diarrhoea. Pathogens such as E coli, hepatitis and salmonella can cause severe health effects ; "
aluminium_sym = "High Aluminium levels can lead to vomiting, diarrohea, skin rashes and skin ulcers; "
antimony_sym = "High Antimony levels can lead to sustained vomiting, andominal cramps and diarrhoea; "
arsenic_sym = "Arsenic is highly toxic and long-term exposure can cause hard patches on palms and soles of feet, skin lesions and cancer; "
barium_sym = "High Barium Levels can lead to hypertension, cardia arrhythmia, convulsions and paralysis; "
bromide_sym = "High Bromide levels can cause vomiting, abdominal pain, coma and paralysis; "
cadmium_sym = "High Cadmium levels can lead to kidney dysfunction and osteoporosis (weak/fragile bones); "
calcium_sym = "High Calcium levels may cause taste to be affected; "
chloride_sym = "High Chloride levels may cause taste to be affected; "
chromium_sym = "High Chromium levels can cause gastrointestinal disorders, haemorrhagic diathesis, convulsions and death; "  #http://www.filterwater.com/t-chromium.aspx
copper_sym = "High Copper levels can cause headaches, vomiting and diarrhoea; "
fluoride_sym = "High fluoride levels can lead to dental and skeletal fluorosis; "
iron_sym = "High iron levels may cause taste to be affected; "
lead_sym = "High lead levels can lead to hypertension, impaired fertility, adverse pregnancy outcomes and death ; "
manganese_sym = "High manganese levels may cause taste to be affected; "
nickel_sym = "High Nickel levels may cause vomiting, diarrhoea, lassitude and headaches; "
nitrate_sym = "High Nitrate levels can lead to cyanosis, asphyxia and blue-baby syndrome in infants; "
nitrite_sym = "High Nitrite levels can lead to cyanosis, asphyxia and blue-baby syndrome in infants; "
sodium_sym = "High Sodium levels may cause taste to be affected; "
strontium_sym = "High Strontium levels can cause bone and dental disorders; "
sulphate_sym = "High Sulphate levels can cause laxative effexts; "


# Cell 5

# This is the function to check the limits

def limit_check(result, limit, exceedence, treatment, symptoms):
    exceeds = []
    treatments = []
    symp = []
    num_sites = len(alldata_df)

    for i in range(num_sites):
        if result[i] > limit:
            exceeded = exceedence

        else:
            exceeded = ""

        exceeds.append(exceeded)

        if exceeds[i] == exceedence:
            treat = treatment

        else:
            treat = ""

        treatments.append(treat)

        if treatments[i] == treatment:
            symptom = symptoms

        else:
            symptom = ""

        symp.append(symptom)

        exceeds_df = pd.DataFrame(exceeds)
        symptoms_df = pd.DataFrame(symp)
        treatments_df = pd.DataFrame(treatments)

        results_df = pd.concat([index_df.Sample_ID, exceeds_df, symptoms_df, treatments_df], axis=1, )
        results_df.columns = ["Sample_ID", "Contaminants", "Treatments", "Symptoms"]
        results_df.set_index("Sample_ID", inplace=True)

    return results_df



#Cell 6

#The function is then used to perform the limit checks, each line of code here represents a different contaminant

faecal_limit_check = limit_check(faecal_result, faecal_limit, faecal_exc, faecal_sym, faecal_treatment )
aluminium_limit_check = limit_check(aluminium_result, aluminium_limit, aluminium_exc, aluminium_sym, aluminium_treatment )
antimony_limit_check = limit_check(antimony_result, antimony_limit, antimony_exc, antimony_sym, antimony_treatment )
arsenic_limit_check = limit_check(arsenic_result, arsenic_limit, arsenic_exc, arsenic_sym, arsenic_treatment )
barium_limit_check = limit_check(barium_result, barium_limit, barium_exc, barium_sym, barium_treatment )
bromide_limit_check = limit_check(bromide_result, bromide_limit, bromide_exc, bromide_sym, bromide_treatment )
cadmium_limit_check = limit_check(cadmium_result, cadmium_limit, cadmium_exc, cadmium_sym, cadmium_treatment )
calcium_limit_check = limit_check(calcium_result, calcium_limit, calcium_exc, calcium_sym, calcium_treatment )
chloride_limit_check = limit_check(chloride_result, chloride_limit, chloride_exc, chloride_sym, chloride_treatment )
chromium_limit_check = limit_check(chromium_result, chromium_limit, chromium_exc, chromium_sym, chromium_treatment )
copper_limit_check = limit_check(copper_result, copper_limit, copper_exc, copper_sym, copper_treatment )
fluoride_limit_check = limit_check(fluoride_result, fluoride_limit, fluoride_exc, fluoride_sym, fluoride_treatment )
iron_limit_check = limit_check(iron_result, iron_limit, iron_exc, iron_sym, iron_treatment )
lead_limit_check = limit_check(lead_result, lead_limit, lead_exc, lead_sym, lead_treatment )
manganese_limit_check = limit_check(manganese_result, manganese_limit, manganese_exc, manganese_sym, manganese_treatment )
nickel_limit_check = limit_check(nickel_result, nickel_limit, nickel_exc, nickel_sym, nickel_treatment )
nitrate_limit_check = limit_check(nitrate_result, nitrate_limit, nitrate_exc, nitrate_sym, nitrate_treatment )
nitrite_limit_check = limit_check(nitrite_result, nitrite_limit, nitrite_exc, nitrite_sym, nitrite_treatment )
sodium_limit_check = limit_check(sodium_result, sodium_limit, sodium_exc, sodium_sym, sodium_treatment )
strontium_limit_check = limit_check(strontium_result, strontium_limit, strontium_exc, strontium_sym, strontium_treatment )
sulphate_limit_check = limit_check(sulphate_result, sulphate_limit, sulphate_exc, sulphate_sym, sulphate_treatment )




#Cell 7

# This code takes the individual limit checks above and merges all in to one dataframe

all_limits_df = faecal_limit_check + aluminium_limit_check + antimony_limit_check + arsenic_limit_check + barium_limit_check + bromide_limit_check + cadmium_limit_check + calcium_limit_check + chloride_limit_check + chromium_limit_check + copper_limit_check + fluoride_limit_check + iron_limit_check + lead_limit_check + manganese_limit_check + nickel_limit_check + nitrate_limit_check + nitrite_limit_check + sodium_limit_check + strontium_limit_check + sulphate_limit_check

# Cell 8

# Where the water is found to not be contaminated there will be a blank space in the table
# This code will fill the blanks in contaminants column

amount = len(all_limits_df)
fill_blanks = []

for i in range(amount):

    blanksi = all_limits_df.Contaminants[i]

    if blanksi == "":

        result = "Water considered safe on date of sample"

    else:
        result = all_limits_df.Contaminants[i]

    fill_blanks.append(result)

contaminants_fill_df = pd.DataFrame(fill_blanks)

contaminants_fill_df.columns = ["Contaminants"]
contaminants_fill_df["Sample_ID"] = index_df.Sample_ID
contaminants_fill_df.set_index("Sample_ID", inplace=True)

contaminants_fill_df
all_limits_df.drop(["Contaminants"], axis=1)

all_limits_df["Contaminants"] = contaminants_fill_df.Contaminants





#Cell 9

# This code will add on the extra columns generated by the limit check to the original results dataframe
# Merge limits with original data

all_results_df = pd.concat([alldata_df, all_limits_df],axis=1, join="outer")








#cell 10

headings_with_units = (['Sampling_date', 'Location_ID', 'Sample_description',
       'Sample_type', 'Latitude', 'Longitude', 'Sea_Level_(mAOD)',
       'Depth_below_ground_(m)', 'Faecal_Coliforms_(count/100ml)', 'Aluminium_(mg/l)', 'Ammonium_(mg/l)',
       'Antimony_(mg/l)', 'Arsenic_(mg/l)', 'Barium_(mg/l)', 'Bromide_(mg/l)', 'Cadmium_(mg/l)', 'Calcium_(mg/l)',
       'Chloride_(mg/l)', 'Chromium_(mg/l)', 'Copper_(mg/l)', 'Fluoride_(mg/l)', 'Iron_(mg/l)', 'Lead_(mg/l)',
       'Magnesium_(mg/l)', 'Manganese_(mg/l)', 'Nickel_(mg/l)', 'Nitrate_(mg/l)', 'Nitrate.1_(mg/l)', 'Nitrite_(mg/l)',
       'Nitrite.1_(mg/l)', 'Phosphate_(mg/l)', 'Potassium_(mg/l)', 'Silicon_(mg/l)', 'Sodium_(mg/l)', 'Strontium_(mg/l)',
       'Sulphate_(mg/l)', 'Zinc_(mg/l)', 'UV_abs_200_(cm-1)', 'UV_abs_210_(cm-1)', 'UV_abs_220_(cm-1)',
       'UV_abs_230_(cm-1)', 'UV_abs_254_(cm-1)', 'UV_abs_260_(cm-1)', 'UV_abs_280_(cm-1)', 'UV_abs_300_(cm-1)',
       'Total_Coliforms_(total_count)', 'Putative_Pathogens_-_Human__E.coli(total_count)',
       'Putative_Pathogens_-_Total__E.coli_(total_count)',
       'Putative_Pathogens_-_Total__Coliform(total_count)', 'Total_Bacteria_(total_count)',
       'Contaminants', 'Treatments', 'Symptoms'])


#This sets the new headings and then replaces underscores with spaces
all_results_df.columns = headings_with_units



#cell 10

headings_with_units = (['Sampling_date', 'Location_ID', 'Sample_description',
       'Sample_type', 'Latitude', 'Longitude', 'Sea_Level_(mAOD)',
       'Depth_below_ground_(m)', 'Faecal_Coliforms_(count/100ml)', 'Aluminium_(mg/l)', 'Ammonium_(mg/l)',
       'Antimony_(mg/l)', 'Arsenic_(mg/l)', 'Barium_(mg/l)', 'Bromide_(mg/l)', 'Cadmium_(mg/l)', 'Calcium_(mg/l)',
       'Chloride_(mg/l)', 'Chromium_(mg/l)', 'Copper_(mg/l)', 'Fluoride_(mg/l)', 'Iron_(mg/l)', 'Lead_(mg/l)',
       'Magnesium_(mg/l)', 'Manganese_(mg/l)', 'Nickel_(mg/l)', 'Nitrate_(mg/l)', 'Nitrate.1_(mg/l)', 'Nitrite_(mg/l)',
       'Nitrite.1_(mg/l)', 'Phosphate_(mg/l)', 'Potassium_(mg/l)', 'Silicon_(mg/l)', 'Sodium_(mg/l)', 'Strontium_(mg/l)',
       'Sulphate_(mg/l)', 'Zinc_(mg/l)', 'UV_abs_200_(cm-1)', 'UV_abs_210_(cm-1)', 'UV_abs_220_(cm-1)',
       'UV_abs_230_(cm-1)', 'UV_abs_254_(cm-1)', 'UV_abs_260_(cm-1)', 'UV_abs_280_(cm-1)', 'UV_abs_300_(cm-1)',
       'Total_Coliforms_(total_count)', 'Putative_Pathogens_-_Human__E.coli(total_count)',
       'Putative_Pathogens_-_Total__E.coli_(total_count)',
       'Putative_Pathogens_-_Total__Coliform(total_count)', 'Total_Bacteria_(total_count)',
       'Contaminants', 'Treatments', 'Symptoms'])


#This sets the new headings and then replaces underscores with spaces
all_results_df.columns = headings_with_units




#Cell 11

# export csv to a folder

all_results_df.to_csv(csv_save_location)


#Cell 12

#This is the final results table that has been exported to csv - Jupyter

#all_results_df