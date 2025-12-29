import pandas as pd

def filter_data(complete_merge_data, start_date, end_date, countries):
    # This is your existing filter function that filters after merges.
    if 'week_start' in complete_merge_data.columns:
        mask = (complete_merge_data['week_start'] >= pd.to_datetime(start_date)) & \
               (complete_merge_data['week_start'] <= pd.to_datetime(end_date))
        complete_merge_data = complete_merge_data[mask]

    if countries is not None and 'country_name' in complete_merge_data.columns:
        c_list = [c.strip() for c in countries.split(',')]
        complete_merge_data = complete_merge_data[complete_merge_data['country_name'].isin(c_list)]

    return complete_merge_data

def filter_datasets_by_date(demographics, epidemiology, vaccinations, hospitalizations, health, index, start_date, end_date):
    # Convert start and end to datetime
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)

    # Filter epidemiology by date if date column exists
    if 'date' in epidemiology.columns:
        epi_mask = (epidemiology['date'] >= start_dt) & (epidemiology['date'] <= end_dt)
        epidemiology = epidemiology[epi_mask]

    # Filter vaccinations by date if date column exists
    if 'date' in vaccinations.columns:
        vac_mask = (vaccinations['date'] >= start_dt) & (vaccinations['date'] <= end_dt)
        vaccinations = vaccinations[vac_mask]

    # Filter hospitalizations by date if date column exists
    if 'date' in hospitalizations.columns:
        hosp_mask = (hospitalizations['date'] >= start_dt) & (hospitalizations['date'] <= end_dt)
        hospitalizations = hospitalizations[hosp_mask]

    # Demographics, health, and index likely have no date column, so we leave them as is
    return demographics, epidemiology, vaccinations, hospitalizations, health, index
