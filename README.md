![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Time of Concentration Calculator
 
*For hydrologists and stormwater engineers: enter watershed length, slope, and surface cover to instantly compute time of concentration using Kirpich or SCS lag equations.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Hydrology
 
INPUTS: (1) Watershed length L (in feet or meters, user selects units via radio button). (2) Average watershed slope S (in ft/ft or m/m, as a decimal; user selects units). (3) Surface cover type (dropdown: Smooth bare soil, Pasture/grassland, Cultivated with residue, Forest/woodland). Internally, each cover maps to a Manning's n or a roughness coefficient used in the SCS lag method. The tool also offers a 'Method' radio button (Kirpich or SCS Lag). CORE CALCULATION: For the Kirpich method (appropriate for agricultural watersheds < 200 acres): Tc (min) = 0.0078 * L^0.77 * S^(-0.385), where L is in feet and S in ft/ft. If L or S is entered in meters, convert to feet internally (1 m = 3.28084 ft). For the SCS lag method: first compute lag time Tlag (hours) = L^0.8 * (S+1)^0.7 / (1900 * Y^0.5), where L is in feet, S is dimensionless, and Y is the watershed curve number derived from the surface cover (lookup table: Bare = 85, Pasture = 75, Cultivated = 70, Forest = 65). Then concentration time Tc = 0.6 * Tlag (hours). The tool outputs Tc in both minutes and hours, clearly labeled. Additionally, the tool provides a confidence note: Kirpich valid for L < 10,000 ft, S between 0.003 and 0.07; SCS valid for any, but derived for rural watersheds. UI: Gradio interface with Textbox for L, Textbox for S, Radio buttons for L units and S units, Dropdown for Cover, Radio buttons for Method, and a 'Calculate' button. Output area displays results in two numeric readouts, plus a short interpretation sentence (e.g., 'For Kirpich, time of concentration is 12.3 minutes (0.21 hours).'). No AI/ML component.
 
## Run it
 
```bash
docker build -t time-of-concentration-calculator .
docker run -p 7860:7860 time-of-concentration-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-27.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
