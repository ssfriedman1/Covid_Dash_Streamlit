from simpledbf import Dbf5
import config as cfg
import pandas as pd
import streamlit as st

# Returns df of selected county
def get_county_key(df, state):
    return df[df.state == state].county.unique()

# Returns df of selected state
def get_state_key(df):
    return sorted(df.state.unique())

# Retrieves Federal Informatino Processing Standards codes for the map data
def get_fips():
    dbf = Dbf5(cfg.dbf)
    fips_df = dbf.to_dataframe()
    fips_df["FIPS"] = fips_df["FIPS"].astype(float)
    return fips_df.loc[:, ["FIPS", "LON", "LAT"]]

# Merging data frames for fips data
def df_left_merge(left_df, right_df):
    return left_df.merge(right_df, left_on="fips", right_on="FIPS", how="left")

# Cleaning function for lat and long data
def df_clean(ff):
    ff1 = ff.rename(columns={"LON": "lon", "LAT": "lat"})
    return ff1.dropna()


@st.cache # caches data for faster loading during usage
# Using fips to get coordinates via other functions
def get_coord(df):
    df1 = get_fips()
    merged_df = df_left_merge(df, df1)
    clean_df = df_clean(merged_df)
    return clean_df


@st.cache
# Retrieve data from the active dataset
def get_data():
    df = pd.read_csv(cfg.db)
    df["date"] = pd.to_datetime(df["date"])
    return df

# Filtering data by selected county and state for user
def filter_data_by_county_state(df, co, st):
    if (co == "All") & (st == "All"):
        return df
    elif co == "All":
        return df[df.state == st]
    elif st == "All":
        return df[df.county == co]
    else:
        return df[(df.state == st) & (df.county == co)]
