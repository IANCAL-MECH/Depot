import pandas as pd
import xlsxwriter


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
    calculated_Q_value = ((serum_surface_area[u_counter] / base_area) * u_variable_name[months_counter] *
                    difference_temperature_array[months_counter] - I_total_sun_lights * light_transmittence[
                        light_transmittence_index] * 0.9352) * base_area
    if difference_temperature_array[months_counter] < 0:
        calculated_Q_value = 0

    return calculated_Q_value


def find_index_temperature_bigger_than_27(outside_temperature_array):
    index_bigger_than_27 = []
    for counter_in_array in range(len(outside_temperature_array)):
        if outside_temperature_array[counter_in_array] >= 27:
            index_bigger_than_27.append(counter_in_array)

    return index_bigger_than_27

def write_string_intead_of_0(U_arrays, what_you_wanna_write):
    for counter_in_array in range(len(U_arrays)):
        if U_arrays[counter_in_array] == 0:
            U_arrays[counter_in_array] = what_you_wanna_write

    return U_arrays


sheet_name_power_plant_district = ['Antalya_Merkez', 'Serik', 'Kaş']
# r is meaning of reading and Don't forget writing file extent(xlsx) and point
average_temperature_excel_data = pd.read_excel(r'power_plant_power_calculation.xlsx',
                                               sheet_name=sheet_name_power_plant_district[0])

months_array = average_temperature_excel_data_months = average_temperature_excel_data["AYLAR"]
outside_temperature_array = average_temperature_excel_data_outside_temperature = average_temperature_excel_data[
    "Dış Ortam Sıcaklığı"]
serum_inside_temperature_array = average_temperature_excel_data_serum_inside_temperature = \
average_temperature_excel_data["Sera İç sıcaklığı"]
temperature_difference_between_array = average_temperature_excel_data_temperature_difference_between = \
average_temperature_excel_data["Sıcaklık Farkı"]
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
difference_temperature_array = []
serum_surface_area = []
light_transmittence = []
u_genre_name = ["U (PE-S)", "U (PE-D)", "U (HG-S)", "U (HG-D)", "U (PC-S)", "U (PC-D)", "U (PVC-S)", "U (PVC-S)", "U (PVC-D)"]


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

Qserum_single_layer_cover = write_string_intead_of_0(Qserum_single_layer_cover, "ne yazılacaktı unuttum ya")
Qserum_double_layer_cover = write_string_intead_of_0(Qserum_double_layer_cover, "ne yazılacaktı unuttum ya")
Qserum_single_horti_cultural = write_string_intead_of_0(Qserum_single_horti_cultural, "ne yazılacaktı unuttum ya")
Qserum_double_horti_cultural = write_string_intead_of_0(Qserum_double_horti_cultural, "ne yazılacaktı unuttum ya")
Qserum_poli_carbon_single = write_string_intead_of_0(Qserum_poli_carbon_single, "ne yazılacaktı unuttum ya")
Qserum_poli_carbon_double = write_string_intead_of_0(Qserum_poli_carbon_double, "ne yazılacaktı unuttum ya")
Qserum_poli_vinyl_colitare_single = write_string_intead_of_0(Qserum_poli_vinyl_colitare_single,
                                                             "ne yazılacaktı unuttum ya")
Qserum_poli_vinyl_colitare_double = write_string_intead_of_0(Qserum_poli_vinyl_colitare_double,
                                                             "ne yazılacaktı unuttum ya")

# Qsera = ((Aortu / Ataban) * U * (Tic - Tdis) - I * T * 0.9352) * Ataban;
#print(find_index_temperature_bigger_than_27())

workbook_calculated_Q_values = xlsxwriter.Workbook('power_plant_power_calculated_Q_values.xlsx')

worksheet = workbook_calculated_Q_values.add_worksheet()

for u_name_counter in range(1, 9):
    worksheet.write(0, u_name_counter, u_genre_name[u_name_counter])

for months_row in range(12):
    worksheet.write(months_row + 1, 0, months_array[months_row])
    worksheet.write(months_row + 1, 1, Qserum_single_layer_cover[months_row])
    worksheet.write(months_row + 1, 2, Qserum_double_layer_cover[months_row])
    worksheet.write(months_row + 1, 3, Qserum_single_horti_cultural[months_row])
    worksheet.write(months_row + 1, 4, Qserum_double_horti_cultural[months_row])
    worksheet.write(months_row + 1, 5, Qserum_poli_carbon_single[months_row])
    worksheet.write(months_row + 1, 6, Qserum_poli_carbon_double[months_row])
    worksheet.write(months_row + 1, 7, Qserum_poli_vinyl_colitare_single[months_row])
    worksheet.write(months_row + 1, 8, Qserum_poli_vinyl_colitare_double[months_row])

workbook_calculated_Q_values.close()
