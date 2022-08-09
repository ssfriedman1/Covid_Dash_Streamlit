import streamlit as st

# Graph for total covid cases using streamlit built in
def draw_tot_cases_graph(df):
    tot_cases_by_day = df.groupby("date")["cases"].sum()
    st.write("Total cases(US):")
    st.line_chart(tot_cases_by_day)

# Graph for daily cases using streamlit built in
def draw_daily_cases_graph(df):
    cases_by_day = df.groupby("date")["cases"].sum().reset_index(name="cases")
    shifted = cases_by_day["cases"].shift(1)
    cases_by_day["daily_cases"] = cases_by_day["cases"] - shifted
    cases_by_day.drop(columns=["cases"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write("Daily cases(US):")
    st.bar_chart(cases_by_day)

# Graph for total deaths using built in
def draw_tot_deaths_graph(df):
    tot_cases_by_day = df.groupby("date")["deaths"].sum()
    st.write("Total deaths(US):")
    st.line_chart(tot_cases_by_day)

# Graph for daily deaths using built in
def draw_daily_deaths_graph(df):
    cases_by_day = df.groupby("date")["deaths"].sum().reset_index(name="deaths")
    shifted = cases_by_day["deaths"].shift(1)
    cases_by_day["daily_deaths"] = cases_by_day["deaths"] - shifted
    cases_by_day.drop(columns=["deaths"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write("Daily deaths(US):")
    st.bar_chart(cases_by_day)

# Total Cases Graph for selected county and state
def draw_county_state_cases_graph(df, co, state):
    county_state_cases_by_day = df.groupby("date")["cases"].sum()
    st.write(f"Total cases({co}, {state}):")
    st.line_chart(county_state_cases_by_day)

# Daily cases graph for selected county and state
def draw_daily_county_state_cases_graph(df, co, state):
    cases_by_day = df.groupby("date")["cases"].sum().reset_index(name="cases")
    shifted = cases_by_day["cases"].shift(1)
    cases_by_day["daily_cases"] = cases_by_day["cases"] - shifted
    cases_by_day.loc[cases_by_day.daily_cases < 0, "daily_cases"] = 0
    cases_by_day.drop(columns=["cases"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write(f"Daily cases({co}, {state}):")
    st.bar_chart(cases_by_day)

# Total death for selected county and state
def draw_county_state_deaths_graph(df, co, state):
    county_state_deaths_by_day = df.groupby("date")["deaths"].sum()
    st.write(f"Total deaths({co}, {state}):")
    st.line_chart(county_state_deaths_by_day)

# Daily death for county and state
def draw_daily_county_state_deaths_graph(df, co, state):
    cases_by_day = df.groupby("date")["deaths"].sum().reset_index(name="deaths")
    shifted = cases_by_day["deaths"].shift(1)
    cases_by_day["daily_deaths"] = cases_by_day["deaths"] - shifted
    cases_by_day.loc[cases_by_day.daily_deaths < 0, "daily_deaths"] = 0
    cases_by_day.drop(columns=["deaths"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write(f"Daily deaths({co}, {state}):")
    st.bar_chart(cases_by_day)

# Build map for selected county and state
def draw_map(df, state, co, date):
    st_co_data_for_date = df[df.date.dt.date == date]
    st.subheader(f"Map of CoVid cases on {date} for {co}, {state}")
    st.map(st_co_data_for_date)
    st.write(f"{len(st_co_data_for_date.index)} counties affected in {co}, {state}")
    st.write(
        f"Total deaths in {co}, {state} till {date} : {st_co_data_for_date['deaths'].sum()}"
    )
    st.write(
        f"Total cases in {co}, {state} till {date} : {st_co_data_for_date['cases'].sum()}"
    )
