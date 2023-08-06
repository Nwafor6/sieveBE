import pandas as pd
import seaborn as sns
import numpy as np
from scipy import interpolate
import math


# Function to read the seive data via a function
def read_excel_data(file_path):
    try:
        # Read the Excel file using pandas read_excel function
        data = pd.read_excel(file_path)
        # for index, row in data.iterrows():
        #     print(row[1] > 5, "printtinh ")
        return data
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

def perform_analysis(data):
    df = read_excel_data(data)
    if df is not None :
        total_max_rtained=0
        initial_weight=300
        correct_weight=[]
        percentage_wt_retained=[]
        sieve_count=0
        for index, row in df.iterrows():
            total_max_rtained +=row[1]
            sieve_count +=1
        correct_value=(initial_weight-total_max_rtained)/sieve_count
        for index, row in df.iterrows():
            correct_weight.append(row[1]+correct_value)
        total=sum(correct_weight)
        percentage_wt_retained=[(i/initial_weight)*100 for i in correct_weight]
        df["correct_weight"]=correct_weight
        df["%wt retained"]=percentage_wt_retained
        cummulate_per_wt_retained=[]
        per_wt_store=[]
        for wt in percentage_wt_retained:
            per_wt_store.append(wt)
            cummulate_per_wt_retained.append(round(sum(per_wt_store), 3))
        df["cumm_%wt_retained"]=cummulate_per_wt_retained
        
        percentage_passing=[(100-i) for i in cummulate_per_wt_retained]
        df["%passing"]=percentage_passing

        p_s = df["Seive size (mm)"]
        c_p = df["%passing"]
        c_f = [pct / 100.0 for pct in c_p]
        sorted_data = sorted(zip(p_s, c_f), key=lambda x: x[0])
        sorted_p_s, sorted_c_f = zip(*sorted_data)

        cdf = np.array(sorted_c_f)

        interpolator = interpolate.interp1d(cdf, sorted_p_s)

        D10 = interpolator(0.1).round(4)
        D30 = interpolator(0.3).round(4)
        D60 = interpolator(0.6).round(4)
        CU = (D60/D10).round(4)
        CC = ((D30*D30) / (D60 * D10)).round(4)

        # print(D10, D30, D60, "Diamter values")
        # gravel_percentage = 100.0 - D60
        # sand_percentage = D60 - D10
        # silt_percentage = D10
        # clay_percentage = 100.0 - (gravel_percentage + sand_percentage + silt_percentage)
        # Calculate gravel, sand, and silt-clay percentages
        # gravel_percentage = df[df["Seive size (mm)"] > 2]["%passing"].iloc[-1]
        # sand_percentage = df[(df["Seive size (mm)"] >= 0.0625) & (df["Seive size (mm)"] <= 2)]["%passing"].iloc[-1]
        # silt_clay_percentage = df[df["Seive size (mm)"] < 0.0625]["%passing"].iloc[-1]

        # Add the percentages to the dictionary
        gravel_percentage=100-df[df["Seive size (mm)"] == 4.750]["%passing"].iloc[-1]
        sand_percentage=100-df[df["Seive size (mm)"] == 0.0750]["%passing"].iloc[-1]
        silt_clay_percentage=round(df[df["Seive size (mm)"] == 0.0750]["%passing"].iloc[-1], 3)

        # ... (your existing code)

        print("Gravel %:", gravel_percentage)
        print("Sand %:", sand_percentage)
        print("Silt_clay%:", silt_clay_percentage)
        # print("Clay %:", clay_percentage)
        df.to_excel(f'media/glory.xlsx', index=False)
        # link_to_file=f'http://127.0.0.1:8000/media/{owner_name}.xlsx'
        # dic={"link":link_to_file, "df_eive":df["Seive size (mm)"], "df_passing":df["%passing"]}
        # return dic
    return df

perform_analysis("sieve_.xlsx")


# import matplotlib.pyplot as plt

# Sample data
# x_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
# y_values = [10, 20, 30, 40, 50, 60, 70]

# # Create a pandas DataFrame from the data
# data = pd.DataFrame({'x': x_values, 'y': y_values})

# # Plot the graph with x-axis in log10 scale
# plt.figure(figsize=(8, 6))
# plt.plot(data['x'], data['y'])
# plt.xscale('log')  # Set x-axis to log10 scale
# plt.xlabel('X Values (log scale)')
# plt.ylabel('Y Values')
# plt.title('Graph with X-axis in log10 scale')
# plt.grid(True)
# plt.show()

    
    