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

Solution:
Easiest to change values in Excel (I'd use pandas now). Changed "CDS" and "CDN" to "Chrysler Drive <N or S>" and removed all full stops. Then passed locations directly to Google Maps API. Much easier than using regex data on my end; let Google do that!
