import streamlit as st
import pandas as pd
import pydeck as pdk

# App Title 
st.title("Los Angeles Bunkdowns")

# Load the Dataset
data = pd.read_csv("CrimeData.csv", skipinitialspace=True)
data.columns = data.columns.str.strip()

# Ensure LAT and LON are numeric, and remove invalid rows
data["LAT"] = pd.to_numeric(data["LAT"], errors="coerce")
data["LON"] = pd.to_numeric(data["LON"], errors="coerce")
data = data.dropna(subset=["LAT", "LON"])

# Check if "Danger Level" exists; if not, handle missing Danger Level
if "Danger Level" not in data.columns:
    st.error("Error: The 'Danger Level' column is missing from the dataset.")
else:
    # Filter rows with valid Danger Levels
    data = data[data["Danger Level"].notna()]

    # Map Danger Levels to Colors
    def map_color(danger_level):
        if danger_level == "Very High Danger":
            return (255, 0, 0)  # Red
        elif danger_level == "High Danger":
            return (255, 165, 0)  # Orange
        elif danger_level == "Medium Danger":
            return (255, 255, 0)  # Yellow
        elif danger_level == "Low Danger":
            return (0, 255, 0)  # Green
        return (0, 0, 255)  # Default Blue for unexpected Danger Levels

    data["Color"] = data["Danger Level"].apply(map_color)

    # Dropdown to Select Area
    options = data["AREA NAME"].unique()
    selected_area = st.selectbox("Choose your area", options)

    # Legend Data with Emojis
    legend_data = [
        {"Danger Level": "Very High Danger", "Color": "🔴 Red"},
        {"Danger Level": "High Danger", "Color": "🟠 Orange"},
        {"Danger Level": "Medium Danger", "Color": "🟡 Yellow"},
        {"Danger Level": "Low Danger", "Color": "🟢 Green"},
        {"Danger Level": "Your selection", "Color": "🔵Blue"},
    ]
    legend_df = pd.DataFrame(legend_data)

    # Highlight selected Danger Level in Legend
    selected_data = data[data["AREA NAME"] == selected_area]
    if not selected_data.empty:
        selected_danger_level = selected_data["Danger Level"].iloc[0]
        legend_df["Danger Level"] = legend_df["Danger Level"].apply(
            lambda x: f"{x}" if x == selected_danger_level else x
        )
        st.write(f"The selected area '{selected_area}' has the Danger Level: {selected_danger_level}.")
    else:
        st.warning(f"No data found for the selected area: {selected_area}")

    # Display Legend Table
    st.table(legend_df)

    # Button to Submit and Display Map
    if st.button("Submit"):
        if not selected_data.empty:
            # Create Pydeck View State
            view_state = pdk.ViewState(
                latitude=selected_data["LAT"].mean(),
                longitude=selected_data["LON"].mean(),
                zoom=12,
                pitch=0
            )

            # Highlight Selected Area
            selected_layer = pdk.Layer(
                "ScatterplotLayer",
                data=selected_data,
                get_position=["LON", "LAT"],
                get_color=[0, 0, 255],  # Blue for Selected Area
                get_radius=300,
                pickable=True,
            )

            # Plot All Areas
            all_layer = pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position=["LON", "LAT"],
                get_color="Color",
                get_radius=200,
                pickable=True,
            )

            deck = pdk.Deck(layers=[all_layer, selected_layer], initial_view_state=view_state)
            st.pydeck_chart(deck)
    else:
        # Default Map Showing All Areas
        view_state = pdk.ViewState(
            latitude=data["LAT"].mean(),
            longitude=data["LON"].mean(),
            zoom=10,
            pitch=0
        )

        all_layer = pdk.Layer(
            "ScatterplotLayer",
            data=data,
            get_position=["LON", "LAT"],
            get_color="Color",
            get_radius=200,
            pickable=True,
        )

        deck = pdk.Deck(layers=[all_layer], initial_view_state=view_state)
        st.pydeck_chart(deck)
