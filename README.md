# 📊 COVID_Mortality_Forecasting — Messy Data Wrangling & Seasonal Forecasting Case Study  

**Author:** Sam Ginzburg  
**Email:** samginzee@gmail.com  
**Tech Stack:** Python · Pandas · NumPy · Matplotlib · Time Series Analysis  

---

## Business Problem & Motivation  

Real-world public health data is rarely clean, consistent, or analysis-ready. Metrics are reported at different temporal granularities, cumulative and incremental values are mixed, and data quality varies significantly across regions.

The goal of this project is to demonstrate how a data analyst can:

- Ingest and reconcile heterogeneous real-world datasets  
- Apply thoughtful data-cleaning and aggregation strategies  
- Identify data quality limitations and adapt methodology accordingly  
- Build interpretable, assumption-aware forecasts under imperfect conditions  

Rather than producing high-confidence predictions, this project emphasizes **analytical judgment, transparency, and disciplined modeling** when working with messy data.

---

## Project Scope  

This project delivers an end-to-end analytical case study that:

- Loads and cleans multiple public health datasets (demographics, epidemiology, hospitalizations, vaccinations, health indicators)
- Resolves inconsistent temporal structures through weekly aggregation
- Handles cumulative vs. incremental metrics to prevent double-counting
- Merges static and time-varying data responsibly
- Analyzes cross-country differences in data quality and reporting
- Applies seasonal regression models to forecast COVID-related mortality trends
- Adapts forecasting strategy when critical data is missing (Italy)

The project is intentionally scoped as an **analytical and forecasting exercise**, not a clinical or policy-making tool.

---

## Methods & Skills Demonstrated  

This project highlights the following technical and analytical competencies:

- **Python** (data pipelines, analysis, forecasting)
- **Pandas** (cleaning, joins, grouping, time-series transformations)
- **Time-Series Aggregation** (daily → weekly alignment)
- **Data Quality Assessment** (nulls, reporting inconsistencies, structural limitations)
- **Feature Engineering** (incremental vs. cumulative metrics)
- **Seasonal Modeling** (sinusoidal regression with trend)
- **Analytical Decision-Making Under Constraints**
- **Clear Communication of Assumptions & Limitations**
- **Portfolio-minded Project Structuring**

---

## Analytical Approach  

### Data Preparation  

- Filtered datasets to retain only analytically relevant columns  
- Standardized dates and aggregated uneven daily data into weekly intervals  
- Reconstructed cumulative metrics from incremental values to avoid inflation  
- Preserved static variables (e.g., population) during temporal joins  
- Applied country and date filters prior to aggregation to prevent leakage  

### Modeling Strategy  

- Identified consistent seasonal patterns in mortality data across countries  
- Selected sinusoidal regression models to capture annual seasonality  
- Applied forecasting only where data quality supported reasonable inference  
- Developed a proxy-based forecasting approach for Italy due to missing death data  

---

## Results & Insights  

- Countries differ significantly in data completeness and reliability  
  - The United States and Germany report consistent mortality trends  
  - Spain exhibits reporting inconsistencies that limit interpretability  
  - Italy lacks death data entirely, requiring indirect estimation  

- Mortality trends across countries show strong seasonal behavior  
  - 1–2 peaks per year, typically in winter  
  - Summer troughs appear consistently  

- Vaccination rates did not exhibit stable inverse correlation with deaths  
  - Variant emergence (Delta, Omicron) confounded simple causal relationships  

- Proxy modeling can provide *plausible* forecasts when direct data is unavailable, but uncertainty must be clearly communicated  

---

## Project Structure  

```text
COVID_Mortality_Forecasting/
│
├── notebooks/
│   ├── final_analysis.ipynb        # Portfolio-facing, curated analysis
│   └── analysis_exploration.ipynb  # Extended exploratory work & reasoning
│
├── scripts/
│   ├── load_data.py
│   └── clean_data.py
│
├── data/
│   └── final_merge.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```
---

## How to Run This Project

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Open the final notebook:
   notebooks/final_analysis.ipynb

The exploratory notebook is included for transparency and deeper inspection but is not required to understand the final results.

## Limitations

- Forecasts are trend-based and assume seasonal stability
- External policy changes and behavioral effects are not modeled
- Data quality varies significantly by country
- Results are intended for analytical demonstration, not real-world decision-making

## Disclaimer

This project is for educational and analytical purposes only and does not constitute medical, public health, or policy advice.