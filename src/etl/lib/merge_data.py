import pandas as pd
import numpy as np

def merge_data_country(demographics, epidemiology, vaccinations, hospitalizations, health, index):
    # Merge each with index to get country_name
    demographics = demographics.merge(index, on='location_key', how='left')
    epidemiology = epidemiology.merge(index, on='location_key', how='left')
    health = health.merge(index, on='location_key', how='left')
    hospitalizations = hospitalizations.merge(index, on='location_key', how='left')
    vaccinations = vaccinations.merge(index, on='location_key', how='left')
    return demographics, epidemiology, vaccinations, hospitalizations, health

def group_data(demographics, epidemiology, vaccinations, hospitalizations, health):
    # DEMOGRAPHICS: group by country_name (sum)
    demographics = demographics.groupby(['country_name', 'country_code'], as_index=False)[
        ['population','population_male','population_female','population_age_00_09','population_age_10_19',
         'population_age_20_29','population_age_30_39','population_age_40_49','population_age_50_59',
         'population_age_60_69','population_age_70_79','population_age_80_and_older']].sum()

    # HEALTH: group by country_name (mean)
    health = health.groupby(['country_name', 'country_code'], as_index=False)['life_expectancy'].mean()

    # EPIDEMIOLOGY: group by country_name, week_start and sum new_* columns
    epidemiology = epidemiology.groupby(['country_name', 'country_code', 'week_start'], as_index=False).agg({
        'new_confirmed':'sum','new_deceased':'sum','new_recovered':'sum','new_tested':'sum'
    })
    epidemiology = epidemiology.sort_values(by=['country_name', 'country_code', 'week_start'])
    epidemiology['cumulative_confirmed'] = epidemiology.groupby(['country_name', 'country_code'])['new_confirmed'].cumsum()
    epidemiology['cumulative_deceased'] = epidemiology.groupby(['country_name', 'country_code'])['new_deceased'].cumsum()
    epidemiology['cumulative_recovered'] = epidemiology.groupby(['country_name', 'country_code'])['new_recovered'].cumsum()
    epidemiology['cumulative_tested'] = epidemiology.groupby(['country_name', 'country_code'])['new_tested'].cumsum()

    # VACCINATIONS
    vaccinations = vaccinations.groupby(['country_name','country_code','week_start'], as_index=False)['new_persons_fully_vaccinated'].sum()
    vaccinations = vaccinations.sort_values(by=['country_name','country_code','week_start'])
    vaccinations['cumulative_persons_fully_vaccinated'] = vaccinations.groupby(['country_name', 'country_code'])['new_persons_fully_vaccinated'].cumsum()

    # HOSPITALIZATIONS
    hospitalizations = hospitalizations.groupby(['country_name','country_code','week_start'], as_index=False).agg({
        'new_hospitalized_patients':'sum',
        'current_hospitalized_patients':'mean',
        'current_intensive_care_patients':'mean'
    })
    hospitalizations = hospitalizations.sort_values(by=['country_name','country_code','week_start'])
    hospitalizations['cumulative_hospitalized_patients'] = hospitalizations.groupby('country_name')['new_hospitalized_patients'].cumsum()

    return demographics, epidemiology, vaccinations, hospitalizations, health

def complete_merge(demographics, epidemiology, vaccinations, hospitalizations, health):
    # Merge demographics and health (no dates)
    merge_without_dates = demographics.merge(health, on=['country_name', 'country_code'], how='outer')

    # Merge epidemiology, hospitalizations, vaccinations (with dates)
    merge_with_dates = epidemiology.merge(hospitalizations, on=['country_name','country_code', 'week_start'], how='outer') \
                                   .merge(vaccinations, on=['country_name','country_code', 'week_start'], how='outer')

    # Merge all together
    complete_merge_data = merge_without_dates.merge(merge_with_dates, on=['country_name', 'country_code'], how='outer')
    return complete_merge_data
