import pandas as pd

def select_one_row_put_in_array(index_value):
    temporary_array = []

    temporary_array.append(single_layer_cover_array[index_value])
    temporary_array.append(double_layer_cover_array[index_value])
    temporary_array.append(single_horti_cultural_array[index_value])
    temporary_array.append(double_horti_cultural_array[index_value])
    temporary_array.append(poli_carbon_single_array[index_value])
    temporary_array.append(poli_carbon_double_array[index_value])
    temporary_array.append(poli_vinyl_colitare_single_array[index_value])
    temporary_array.append(poli_vinyl_colitare_double_array[index_value])

    return temporary_array


def Qserum_list(u_counter, months_counter, light_transmittence_index, u_variable_name):
    Qserum_first = ((serum_surface_area[u_counter] / base_area) * u_variable_name[months_counter] *
                    difference_temperature_array[months_counter] - I_total_sun_lights * light_transmittence[light_transmittence_index] * 0.9352) * base_area
    if difference_temperature_array[months_counter] < 0:
        Qserum_first = 0
#    print(serum_surface_area[u_counter])
    return  Qserum_first


#r is meaning of reading and Don't forget writing file extent and point
average_temperature_excel_data = pd.read_excel (r'power_plant_power_calculation.xlsx', sheet_name='Antalya_Merkez')

months_array = average_temperature_excel_data_months = average_temperature_excel_data["AYLAR"]
outside_temperature_array = average_temperature_excel_data_outside_temperature = average_temperature_excel_data["Dış Ortam Sıcaklığı"]
serum_inside_temperature_array = average_temperature_excel_data_serum_inside_temperature = average_temperature_excel_data["Sera İç sıcaklığı"]
temperature_difference_between_array = average_temperature_excel_data_temperature_difference_between = average_temperature_excel_data["Sıcaklık Farkı"]
single_layer_cover_array = single_layer_cover = average_temperature_excel_data["U (PE-S)"]
double_layer_cover_array = double_layer_cover = average_temperature_excel_data["U (PE-D)"]
single_horti_cultural_array = horti_cultural_single = average_temperature_excel_data["U (HG-S)"]
double_horti_cultural_array = horti_cultural_double = average_temperature_excel_data["U (HG-D)"]
poli_carbon_single_array = poli_carbon_single = average_temperature_excel_data["U (PC-S)"]
poli_carbon_double_array = poli_carbon_double = average_temperature_excel_data["U (PC-D)"]
poli_vinyl_colitare_single_array = poli_vinyl_colitare_single = average_temperature_excel_data["U (PVC-S)"]
poli_vinyl_colitare_double_array = poli_vinyl_colitare_double = average_temperature_excel_data["U (PVC-D)"]
I_total_sun_lights = months_array[15]

base_area = 25000
overall_heat_loss_coefficent = 1
minumum_power_for_the_green_house = 2
power_for_the_green_house = 3

difference_temperature_array = []
serum_surface_area = []
light_transmittence = []

for counter in range(12):
    difference_temperature_array.append(serum_inside_temperature_array[counter] - outside_temperature_array[counter])

maximum_temperature_difference = max(difference_temperature_array)

serum_surface_area = select_one_row_put_in_array(13)
light_transmittence = select_one_row_put_in_array(12)

Qserum_single_layer_cover = []
Qserum_double_layer_cover = []
Qserum_single_horti_cultural = []
Qserum_double_horti_cultural = []
Qserum_poli_carbon_single = []
Qserum_poli_carbon_double = []
Qserum_poli_vinyl_colitare_single = []
Qserum_poli_vinyl_colitare_double = []


for months_counter in range(len(difference_temperature_array)):
    Qserum_single_layer_cover.append(Qserum_list(0, months_counter, 0, single_layer_cover_array))
    Qserum_double_layer_cover.append(Qserum_list(1, months_counter, 1, double_layer_cover_array))
    Qserum_single_horti_cultural.append(Qserum_list(2, months_counter, 2, single_horti_cultural_array))
    Qserum_double_horti_cultural.append(Qserum_list(3, months_counter, 3, double_horti_cultural_array))
    Qserum_poli_carbon_single.append(Qserum_list(4, months_counter, 4, poli_carbon_single_array))
    Qserum_poli_carbon_double.append(Qserum_list(5, months_counter, 5, poli_carbon_double_array))
    Qserum_poli_vinyl_colitare_single.append(Qserum_list(6, months_counter, 6, poli_vinyl_colitare_single_array))
    Qserum_poli_vinyl_colitare_double.append(Qserum_list(7, months_counter, 7, poli_vinyl_colitare_double_array))

#Qsera = ((Aortu / Ataban) * U * (Tic - Tdis) - I * T * 0.9352) * Ataban;
#int Tic=18;


print(Qserum_single_layer_cover
      )


