'''File to avoid annoying renaming of discrepant files like "districts.asc" vs "district.asc" in the pipeline'''

from _configs.country_config import *

############################## Data files ##############################

# /DATA/ 
observed_population_raster_path = f"{data_path}/{country_code}_population_v2_2020.asc"
district_mapping_csv_path = f"{data_path}/{country_code}_mapping.csv"
districts_raster_path = f"{data_path}/{country_code}_districts.asc"
# districts_raster_sequential_path = f"{data_path}/{country_code}_district_seq1.asc"
districts_raster_sequential_path = districts_raster_path
treatment_seeking_raster_path = f"{data_path}/{country_code}_treatmentseeking_2023_v3.asc" 
travel_time_raster_path = f"{data_path}/{country_code}_traveltime.asc"

incidence_data_csv_path = None
pfpr_raster_path = f"{data_path}/{country_code}_pfpr_2to10_{calibration_year}.asc"

seasonality_file_path = f"{template_path}/{country_code}_seasonality.csv"

# District Mapping Columns
ID_COLUMN = "ID"
DISTRICT_COLUMN = "region_name"

# /generated/
initial_population_projected_raster_path = f"{generated_data_path}/{country_code}_population_backwards_projected_{initial_year}_26.97M.asc"
# initial_population_projected_raster_path = f"{generated_data_path}/{country_code}_population_backwards_projected_{initial_year}_unscaled.asc"
projected_population_calibration_year_raster_path = f"{generated_data_path}/{country_code}_population_projected_{calibration_year}.asc"

zero_beta_raster_path = f"{generated_data_path}/{country_code}_beta_zero.asc"

population_per_district_projected_csv_path = f"{generated_data_path}/population_per_district_projected_{calibration_year}.csv"

population_incidence_per_district_csv_path = f"{generated_data_path}/population_incidence_per_district.csv"


# Templates
BETA_RASTER_TEMPLATE = f"{template_path}/{country_code}_beta.template"
ACCESS_RASTER_TEMPLATE = f"{template_path}/{country_code}_treatmentseeking.template"
POPULATION_BIN_RASTER_TEMPLATE = f"{template_path}/{country_code}_initialpopulation_1_location.template"


