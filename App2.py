import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

def highlight_state_on_map(india_map, state, drought_probability):
    # Use the state coordinates for highlighting
    # You may need to replace these coordinates with the actual coordinates of the states
    state_coordinates = {
        'Andaman': [11.7401, 92.6586], 'Andhra Pradesh': [15.9129, 79.7400], 'Arunachal Pradesh': [27.1004, 93.6166], 'Assam': [26.2006, 92.9376], 'Bihar': [25.0961, 85.3131], 'Chandigarh': [30.7333, 76.7794], 'Chhattisgarh': [21.2787, 81.8661], 'Dadra and Nagar Haveli and Daman and Diu': [20.1809, 73.0169], 'Delhi': [28.7041, 77.1025], 'Goa': [15.2993, 74.1240], 'Gujarat': [22.2587, 71.1924], 'Haryana': [29.0588, 76.0856], 'Himachal Pradesh': [31.1048, 77.1734], 'Jammu and Kashmir': [33.7782, 76.5762], 'Jharkhand': [23.6102, 85.2799], 'Karnataka': [15.3173, 75.7139], 'Kerala': [10.8505, 76.2711], 'Ladakh': [34.1526, 77.5771], 'Lakshadweep': [10.5667, 72.6417], 'Madhya Pradesh': [22.9734, 78.6569], 'Maharashtra': [19.7515, 75.7139], 'Manipur': [24.6637, 93.9063], 'Meghalaya': [25.4670, 91.3662], 'Mizoram': [23.1645, 92.9376], 'Nagaland': [26.1584, 94.5624], 'Odisha': [20.9517, 85.0985], 'Puducherry': [11.9416, 79.8083], 'Punjab': [31.1471, 75.3412], 'Rajasthan': [27.0238, 74.2179], 'Sikkim': [27.5330, 88.5122], 'Tamil Nadu': [11.1271, 78.6569], 'Telangana': [18.1124, 79.0193], 'Tripura': [23.9408, 91.9882], 'Uttar Pradesh': [26.8467, 80.9462], 'Uttarakhand': [30.0668, 79.0193], 'West Bengal': [22.9868, 87.8550]
    }

    # Get the coordinates for the selected state
    state_coords = state_coordinates.get(state)

    # Choose the color based on drought probability
    color = 'green' if drought_probability == 0 else 'red'

    # Create a marker for the selected state and add it to the map
    if state_coords:
        folium.Marker(location=state_coords, popup=f"{state}: Drought Probability - {drought_probability}",
                      icon=folium.Icon(color=color)).add_to(india_map)

def main():
    st.title("Map of India")

    # Coordinates for the center of India
    india_center = [20.5937, 78.9629]

    # Create a Folium map centered on India
    india_map = folium.Map(location=india_center, zoom_start=5)

    # Display the map
    folium_static(india_map)

    # Dropdown menu for Years
    years_range = ["2026-2030", "2031-2035", "2036-2040", "2041-2045", "2046-2050",
                   "2051-2055", "2056-2060", "2061-2065", "2066-2070", "2071-2075",
                   "2076-2080", "2081-2085", "2086-2090", "2091-2095", "2096-2100"]
    selected_year = st.selectbox("Select Year Range", years_range)

    # Dropdown menu for State/Union Territory
    states_UT = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
                 "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Goa",
                 "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Lakshadweep",
                 "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
                 "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                 "Uttarakhand", "West Bengal"]
    selected_state_UT = st.selectbox("Select State/Union Territory", states_UT)

    # Button for prediction
    if st.button("Predict"):
        # Read the CSV file for the selected state
        csv_filename = r"C:\Users\Aditi Bhargav\OneDrive\vs code\FrostHacks\Drought hoga ya nahi\{}.csv".format(selected_state_UT)
        try:
            df = pd.read_csv(csv_filename)
            print("Columns in the CSV file:", df.columns)
        except FileNotFoundError:
            st.error(f"CSV file '{csv_filename}' not found for {selected_state_UT}")
            return

        # Extract Drought Probability for the selected year range
        # For demonstration purposes, assuming the column names are 'Range', 'Prediction'
        try:
            selected_df = df[df['Range'] == selected_year]
            drought_probability = selected_df['Drought Probability'].mean()
        except KeyError:
            st.error("Column 'Range' or 'Prediction' not found in the CSV file.")
            return

        # Highlight the selected state on the map
        highlight_state_on_map(india_map, selected_state_UT, drought_probability)
        # Display the updated map
        folium_static(india_map)

if __name__ == "__main__":
    main()
