import pandas as pd
import numpy as np

def clean_data(demographics, epidemiology, vaccinations, hospitalizations, health, index):
    # DEMOGRAPHICS
    demographics = demographics[['location_key','population','population_male','population_female',
                                 'population_age_00_09','population_age_10_19','population_age_20_29',
                                 'population_age_30_39','population_age_40_49','population_age_50_59',
                                 'population_age_60_69','population_age_70_79','population_age_80_and_older']].copy()

    # EPIDEMIOLOGY: add date, week, week_start
    epidemiology['date'] = pd.to_datetime(epidemiology['date'])
    epidemiology['week'] = epidemiology['date'].dt.isocalendar().week
    epidemiology['week_start'] = epidemiology['date'] - pd.to_timedelta(epidemiology['date'].dt.weekday, unit='d')

    # VACCINATIONS: keep certain columns, add date, week, week_start
    vaccinations = vaccinations[['date','location_key','new_persons_fully_vaccinated','cumulative_persons_fully_vaccinated']].copy()
    vaccinations['date'] = pd.to_datetime(vaccinations['date'])
    vaccinations['week'] = vaccinations['date'].dt.isocalendar().week
    vaccinations['week_start'] = vaccinations['date'] - pd.to_timedelta(vaccinations['date'].dt.weekday, unit='d')

    # HOSPITALIZATIONS: keep certain columns, add date, week, week_start
    hospitalizations = hospitalizations[['date','location_key','new_hospitalized_patients','cumulative_hospitalized_patients',
                                         'current_hospitalized_patients','current_intensive_care_patients']].copy()
    hospitalizations['date'] = pd.to_datetime(hospitalizations['date'])
    hospitalizations['week'] = hospitalizations['date'].dt.isocalendar().week
    hospitalizations['week_start'] = hospitalizations['date'] - pd.to_timedelta(hospitalizations['date'].dt.weekday, unit='d')

    # HEALTH: keep location_key, life_expectancy
    health = health[['location_key','life_expectancy']].copy()

    # INDEX: keep location_key, country_name
    index = index[['location_key','country_name', 'country_code']].copy()

    return demographics, epidemiology, vaccinations, hospitalizations, health, index