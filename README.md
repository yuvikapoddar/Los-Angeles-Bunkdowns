Los Angeles Bunkdowns: Airbnb Safety Index

Los Angeles Bunkdowns is a data-driven geospatial tool designed to help travelers make informed lodging decisions by quantifying the safety of Airbnb listings in Los Angeles. By merging historical crime data with vacation rental listings, the platform provides a "Danger Level" score for each Airbnb, transforming raw data into actionable safety insights.

Project Overview
While Airbnbs offer unique and economical travel experiences, guests often lack clear information regarding the safety of the surrounding neighborhood. This project bridges that gap by analyzing proximity to reported incidents and visualizing high-crime zones.

Key Features
- Geospatial Safety Index: Developed an algorithm to analyze 50,000+ LAPD crime records alongside Airbnb reviews to generate a localized safety score.
- Proximity Analysis: Applied geospatial techniques to identify crime patterns specifically surrounding individual listings.
- Danger Level Categorization: Classified crimes by severity and impact to assign a simplified "Danger Level" to each listing.
- Interactive Dashboard: Built a Streamlit web application that allows users to explore listings on an interactive map.
- Custom Filters: Users can filter listings by safety levels and visualize high-crime areas to avoid digging through raw data.

Technical Stack
- Language: Python 
- Data Analysis: Pandas, GeoPandas, NumPy, Folium
- Visualization & UI: Streamlit 
- Data Sources: LAPD Crime Records, Airbnb Listing Data
