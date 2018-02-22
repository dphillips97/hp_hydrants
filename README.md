# hp_hydrants
Top-level goal: read Excel sheet of hydrant locations to geocode

Problem: addresses are not consistent; there are several types of addresses. Examples:
- Brickley & CDS
- 687 W. Coy
- Shevlin & Lennox
- Mall - South End
- American House N.
- Barn #23 South
- Service Road #1

Ideas:
1. Use regex to grab address info
2. Just pass address info to Google Maps API and filter results via bounding box
3. If regex can not find address, address outside of city boundaries, or not found via maps write "not found" next to cell
4. Output sheet with info - coordinates, "not found"

# TODO
- Read Excel sheet
- Replace "CD" with "Chrysler Drive"
- Plug address directly into Google Maps API
- See if coordinates returned
- See if coordinates in bounding box
- If None, return "error"
