# data.py - All Amaravati Data in one place
# This is like the database for APCRDA dashboard

import pandas as pd

# 1. ZONES OF AMARAVATI - With real approx location
zones_data = [
    {"Zone": "Secretariat", "Latitude": 16.52, "Longitude": 80.51, "Progress": 72, "Status": "On Track"},
    {"Zone": "Assembly", "Latitude": 16.53, "Longitude": 80.52, "Progress": 60, "Status": "On Track"},
    {"Zone": "High Court", "Latitude": 16.51, "Longitude": 80.50, "Progress": 45, "Status": "Delayed"},
    {"Zone": "Residential Zone", "Latitude": 16.54, "Longitude": 80.53, "Progress": 55, "Status": "Delayed"},
    {"Zone": "Seed Capital Road", "Latitude": 16.55, "Longitude": 80.54, "Progress": 85, "Status": "On Track"},
    {"Zone": "Krishna Riverfront", "Latitude": 16.50, "Longitude": 80.49, "Progress": 40, "Status": "Delayed"},
]

zones_df = pd.DataFrame(zones_data)

# 2. CONSTRUCTION PROJECTS
construction_data = [
    {"Project": "Secretariat", "Progress %": 72, "Status": "On Track"},
    {"Project": "High Court", "Progress %": 45, "Status": "Delayed"},
    {"Project": "Assembly", "Progress %": 60, "Status": "On Track"},
    {"Project": "Seed Capital Road", "Progress %": 85, "Status": "On Track"},
    {"Project": "Housing", "Progress %": 55, "Status": "Delayed"},
]
construction_df = pd.DataFrame(construction_data)

# 3. LAND POOLING DATA
land_total = 33000  # Total acres pooled
land_returned = 28000  # Acres returned as developed plots

# 4. GRIEVANCE DATA
grievance_total = 1500
grievance_solved = 1240
grievance_pending = 260