import pandas as pd
import xlsxwriter


def select_one_row_put_in_array(index_value):
    temporary_array = []

    temporary_array.append(single_layer_poly_ethylene_array[index_value])
    temporary_array.append(double_layer_poly_ethylene_array[index_value])
    temporary_array.append(single_layer_horti_cultural_array[index_value])
    temporary_array.append(double_layer_horti_cultural_array[index_value])
    temporary_array.append(single_layer_poly_carbonate_array[index_value])
    temporary_array.append(double_layer_poly_carbonate_array[index_value])
    temporary_array.append(single_layer_poly_vinyl_chloride_array[index_value])
    temporary_array.append(double_layer_poly_vinyl_chloride_array[index_value])
    temporary_array.append(day_time_array[index_value])
    temporary_array.append(i_coefficient_array[index_value])
    return temporary_array


# Qsera = ((Aortu / Ataban) * U * (Tic - Tdis) - I * T * 0.9352) * Ataban
def Qgreenhouse_list(u_counter, months_counter, light_transmittence_index, u_variable_name):
    calculated_Q_value = ((greenhouse_surface_area[u_counter] / base_area) * u_variable_name[months_counter] *
                          difference_temperature_array[months_counter] - i_coefficient_array[
                              months_counter] * I_total_sun_lights * light_transmittence[
                              light_transmittence_index] * day_time_array[months_counter] / 24 * 0.9352) * base_area
    if difference_temperature_array[months_counter] < 0:
        calculated_Q_value = 0

    return calculated_Q_value


def write_string_instead_of_0(U_arrays, text_i_will_add_instead):
    for counter_in_array in range(len(U_arrays)):
        if U_arrays[counter_in_array] == 0:
            U_arrays[counter_in_array] = text_i_will_add_instead
    return U_arrays


sheet_name_power_plant_district = ['Antalya_Merkez', 'Serik', 'Kaş']
# r means reading, and don't forget writing file extention(xlsx) and adding a point in front of it.
read_excel_data = pd.read_excel(r'power_plant_power_calculation.xlsx', sheet_name=sheet_name_power_plant_district[0])
# read_excel_data reads from power_plant_power_calculation.xlsx
# sheet_name=sheet_name_power_plant_district[0] => it is reading values from sheet 0(Antalya_Merkez). Change it to have
# Q values for different districts.

months_array = read_excel_data_months = \
    read_excel_data["AYLAR"]
outside_temperature_array = read_excel_data_outside_temperature = \
    read_excel_data["Dış Ortam Sıcaklığı"]
greenhouse_inside_temperature_array = read_excel_data_greenhouse_inside_temperature = \
    read_excel_data["Sera İç sıcaklığı"]
temperature_difference_between_array = read_excel_data_temperature_difference_between = \
    read_excel_data["Sıcaklık Farkı"]
single_layer_poly_ethylene_array = single_layer_poly_ethylene_cover = read_excel_data["U (PE-S)"]
double_layer_poly_ethylene_array = double_layer_poly_ethylene_cover = read_excel_data["U (PE-D)"]
single_layer_horti_cultural_array = horti_cultural_single = read_excel_data["U (HG-S)"]
double_layer_horti_cultural_array = horti_cultural_double = read_excel_data["U (HG-D)"]
single_layer_poly_carbonate_array = single_layer_poly_carbonate = read_excel_data["U (PC-S)"]
double_layer_poly_carbonate_array = double_layer_poly_carbonate = read_excel_data["U (PC-D)"]
single_layer_poly_vinyl_chloride_array = single_layer_poly_vinyl_chloride = read_excel_data["U (PVC-S)"]
double_layer_poly_vinyl_chloride_array = double_layer_poly_vinyl_chloride = read_excel_data["U (PVC-D)"]
day_time_array = day_time = read_excel_data["Güneşlenme Süresi"]
i_coefficient_array = i_coefficient = read_excel_data["i Katsayısı"]
I_total_sun_lights = months_array[15]


base_area = 25000
difference_temperature_array = []
greenhouse_surface_area = []
light_transmittence = []
cover_material_name = ["(PE-S)", "(PE-D)", "(HG-S)", "(HG-D)", "(PC-S)", "(PC-D)", "(PVC-S)", "(PVC-S)", "(PVC-D)"]

for counter in range(12):
    difference_temperature_array.append(
        greenhouse_inside_temperature_array[counter] - outside_temperature_array[counter])
maximum_temperature_difference = max(difference_temperature_array)

greenhouse_surface_area = select_one_row_put_in_array(13)
light_transmittence = select_one_row_put_in_array(12)

Qgreenhouse_single_layer_poly_ethylene_cover = []
Qgreenhouse_double_layer_poly_ethylene_cover = []
Qgreenhouse_single_layer_horti_cultural_cover = []
Qgreenhouse_double_layer_horti_cultural_cover = []
Qgreenhouse_single_layer_poly_carbonate_cover = []
Qgreenhouse_double_layer_poly_carbonate_cover = []
Qgreenhouse_single_layer_poly_vinyl_chloride_cover = []
Qgreenhouse_double_layer_poly_vinyl_chloride_cover = []

for months_counter in range(len(difference_temperature_array)):
    Qgreenhouse_single_layer_poly_ethylene_cover.append(
        Qgreenhouse_list(0, months_counter, 0, single_layer_poly_ethylene_array))
    Qgreenhouse_double_layer_poly_ethylene_cover.append(
        Qgreenhouse_list(1, months_counter, 1, double_layer_poly_ethylene_array))
    Qgreenhouse_single_layer_horti_cultural_cover.append(
        Qgreenhouse_list(2, months_counter, 2, single_layer_horti_cultural_array))
    Qgreenhouse_double_layer_horti_cultural_cover.append(
        Qgreenhouse_list(3, months_counter, 3, double_layer_horti_cultural_array))
    Qgreenhouse_single_layer_poly_carbonate_cover.append(
        Qgreenhouse_list(4, months_counter, 4, single_layer_poly_carbonate_array))
    Qgreenhouse_double_layer_poly_carbonate_cover.append(
        Qgreenhouse_list(5, months_counter, 5, double_layer_poly_carbonate_array))
    Qgreenhouse_single_layer_poly_vinyl_chloride_cover.append(
        Qgreenhouse_list(6, months_counter, 6, single_layer_poly_vinyl_chloride_array))
    Qgreenhouse_double_layer_poly_vinyl_chloride_cover.append(
        Qgreenhouse_list(7, months_counter, 7, double_layer_poly_vinyl_chloride_array))

Qgreenhouse_single_layer_poly_ethylene_cover = write_string_instead_of_0(Qgreenhouse_single_layer_poly_ethylene_cover,
                                                                         "Isıtma yapılmayacaktır.")
Qgreenhouse_double_layer_poly_ethylene_cover = write_string_instead_of_0(Qgreenhouse_double_layer_poly_ethylene_cover,
                                                                         "Isıtma yapılmayacaktır.")
Qgreenhouse_single_layer_horti_cultural_cover = write_string_instead_of_0(Qgreenhouse_single_layer_horti_cultural_cover,
                                                                          "Isıtma yapılmayacaktır.")
Qgreenhouse_double_layer_horti_cultural_cover = write_string_instead_of_0(Qgreenhouse_double_layer_horti_cultural_cover,
                                                                          "Isıtma yapılmayacaktır.")
Qgreenhouse_single_layer_poly_carbonate_cover = write_string_instead_of_0(Qgreenhouse_single_layer_poly_carbonate_cover,
                                                                          "Isıtma yapılmayacaktır.")
Qgreenhouse_double_layer_poly_carbonate_cover = write_string_instead_of_0(Qgreenhouse_double_layer_poly_carbonate_cover,
                                                                          "Isıtma yapılmayacaktır.")
Qgreenhouse_single_layer_poly_vinyl_chloride_cover = write_string_instead_of_0(
    Qgreenhouse_single_layer_poly_vinyl_chloride_cover, "Isıtma yapılmayacaktır.")
Qgreenhouse_double_layer_poly_vinyl_chloride_cover = write_string_instead_of_0(
    Qgreenhouse_double_layer_poly_vinyl_chloride_cover, "Isıtma yapılmayacaktır.")

# Qsera = ((Aortu / Ataban) * U * (Tic - Tdis) - I * T * 0.9352) * Ataban;
print(Qgreenhouse_single_layer_poly_ethylene_cover)

workbook_calculated_Q_values = xlsxwriter.Workbook('power_plant_power_calculated_Q_values_Antalya_Merkez.xlsx')

worksheet = workbook_calculated_Q_values.add_worksheet()

for counter in range(len(outside_temperature_array)):
    if outside_temperature_array[counter] > 27:
        worksheet.write(counter, 9, "Aktif havalandırma yapılmalıdır.")

for u_name_counter in range(1, 9):
    worksheet.write(0, u_name_counter, cover_material_name[u_name_counter])

for months_row in range(12):
    worksheet.write(months_row + 1, 0, months_array[months_row])
    worksheet.write(months_row + 1, 1, Qgreenhouse_single_layer_poly_ethylene_cover[months_row])
    worksheet.write(months_row + 1, 2, Qgreenhouse_double_layer_poly_ethylene_cover[months_row])
    worksheet.write(months_row + 1, 3, Qgreenhouse_single_layer_horti_cultural_cover[months_row])
    worksheet.write(months_row + 1, 4, Qgreenhouse_double_layer_horti_cultural_cover[months_row])
    worksheet.write(months_row + 1, 5, Qgreenhouse_single_layer_poly_carbonate_cover[months_row])
    worksheet.write(months_row + 1, 6, Qgreenhouse_double_layer_poly_carbonate_cover[months_row])
    worksheet.write(months_row + 1, 7, Qgreenhouse_single_layer_poly_vinyl_chloride_cover[months_row])
    worksheet.write(months_row + 1, 8, Qgreenhouse_double_layer_poly_vinyl_chloride_cover[months_row])

workbook_calculated_Q_values.close()
