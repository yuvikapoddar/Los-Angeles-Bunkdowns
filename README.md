Los Angeles Bunkdowns – Airbnb Safety Index

Overview

Los Angeles Bunkdowns is a geospatial data project that evaluates Airbnb listing safety using LAPD crime data and Airbnb reviews. The goal is to help travelers assess neighborhood safety through a clear, data-driven safety index.

Problem

Travelers often evaluate price and amenities but overlook localized safety risks. Raw crime datasets are large and difficult to interpret without structured analysis.

Approach
	-	Ingested and cleaned 50K+ LAPD crime records
	- Applied geospatial proximity analysis to map crimes to nearby listings
	- Categorized crimes by severity and impact
	- Designed a weighted scoring system to generate a “Danger Level” per listing
	- Integrated results into an interactive dashboard

Tech Stack

Python, Pandas, GeoPandas, Scikit-learn, Streamlit, Folium

Features
	- Interactive map-based visualization
	- Filter listings by safety level
	- Visualize high-crime zones
	- Data-driven severity scoring

Live Demo
  https://los-angeles-bunkdowns-qgnqwdpu6xiydobmrmy6kp.streamlit.app/
