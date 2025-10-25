#its in this file that we will prepare the data for the dashboard visualizations

import pandas as pd
import plotly.express as px
import pycountry_convert as pc

#as we see in the dashboard, classifying meal prices by couuntries isn't efficient. 
#There are too many countries, so we will classify meal prices by continents instead.
#I used the pycountry_convert library to map country names to continents.
#the problem i faced here is that some country names in my dataset do not match the names used by the pycountry_convert library.

#To solve this, i created a dictionary called country_corrections that maps the country names in my dataset to the corresponding names
country_corrections = {
    "South Korea" : "Korea, Republic of",
    "North Korea" : "Korea, Democratic People's Republic of",
    "Czechia" : "Czech Republic",
    "Russia" : "Russian Federation",
    "Vietnam" : "Viet Nam",
    "Iran" : "Iran, Islamic Republic of",
    "Venezuela" : "Venezuela, Bolivarian Republic of",
    "Syria" : "Syrian Arab Republic",
    "Laos" : "Lao People's Democratic Republic",
    "Bolivia" : "Bolivia, Plurinational State of",
    "Tanzania" : "Tanzania, United Republic of",
    "Moldova" : "Moldova, Republic of",
    "Palestine" : "Palestine, State of",
    "Bosnia And Herzegovina": "Bosnia and Herzegovina",
    "Timor-Leste": "East Timor",  
    "Reunion": "Réunion",
    "Sao Tome And Principe": "Sao Tome and Principe",
    "Trinidad And Tobago": "Trinidad and Tobago",
    "Isle Of Man": "Isle of Man",
    "Saint Kitts And Nevis": "Saint Kitts and Nevis",
    "Saint Vincent And The Grenadines": "Saint Vincent and the Grenadines",
    "Antigua And Barbuda": "Antigua and Barbuda",
    "Turks And Caicos Islands": "Turks and Caicos Islands",
    "Vatican City": "Holy See (Vatican City State)",
    "Sint Maarten": "Sint Maarten (Dutch part)",
    "East Timor": "Timor-Leste",
    "Holy See (Vatican City State)": "Vatican City",
    "Sint Maarten (Dutch part)": "Sint Maarten"
}
#but even after these corrections, some countries were still not recognized by the library and could not be mapped to a continent.
#To handle these cases, i created another dictionary called manual_continents that manually assigns the correct continent to these countries.
manual_continents = {
    "Vatican City": "Europe",
    "Sint Maarten": "North America",
    "Timor-Leste": "Asia"
}

def country_to_continent(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continents = {
            "AF": "Africa",
            "AS": "Asia",
            "EU": "Europe",
            "NA": "North America",
            "SA": "South America",
            "OC": "Oceania"
        }
        return continents.get(continent_code, "Other")
    except:
        return "Other"
    


def make_tables(df):
    tables = {}

    df = df.rename(columns={
        "x1": "Meal Price (USD)",
        "x48": "Rent (USD)",
        "x54": "Salary (USD)"
    })
    
    df["country"] = df["country"].replace(country_corrections)
    df["continent"] = df["country"].apply(country_to_continent)

    df.loc[df["country"].isin(manual_continents.keys()), "continent"] = \
    df["country"].map(manual_continents)
    df = df[df["continent"] != "Other"]

    

    
    
    #this code is used to delete the "other" column of the graph. 


    """
    Unrecognized countries : ['country' 'Bosnia And Herzegovina' 'Timor-Leste' 'Reunion'
 'Sao Tome And Principe' 'Trinidad And Tobago' 'Isle Of Man'
 'Saint Kitts And Nevis' 'Saint Vincent And The Grenadines'
 'Antigua And Barbuda' 'Turks And Caicos Islands' 'Vatican City'
 'Sint Maarten']
 
    """
    


    # KPIs
    
    tables["kpis"] = {
        "avg_meal": df["Meal Price (USD)"].mean(),
        "avg_rent": df["Rent (USD)"].mean(),
        "avg_salary": df["Salary (USD)"].mean(),

        "preschool_salary_ratio": (df["x42"] / df["Salary (USD)"]).mean(),
    "primary_school_salary_ratio": (df["x43"] / df["Salary (USD)"]).mean(),
    "liters_gasoline_affordable": (df["Salary (USD)"] / df["x33"]).mean(),
    "transport_salary_ratio": (df["x29"] / df["Salary (USD)"]).mean(),
    "beer_ratio_restaurant": (df["x5"] / df["x4"]).mean(),   # importée / locale (restaurant)
    "beer_ratio_market": (df["x26"] / df["x25"]).mean()
    }

    df_meal = df.groupby("country")["Meal Price (USD)"].mean().reset_index()
    tables["map_meal"] = px.choropleth(
        df_meal,
        locations="country",
        locationmode="country names",
        color="Meal Price (USD)",
        title="Average Meal Price by Country",
        color_continuous_scale="Viridis",
        labels={"Meal Price (USD)"},
    )
    
    df_rent = df.groupby("country")["Rent (USD)"].mean().reset_index()
    tables["map_rent"] = px.choropleth(
        df_rent,
        locations="country",
        locationmode="country names",
        color="Rent (USD)",
        title="Average Rent by Country",
        color_continuous_scale="Plasma",
        labels={"Rent (USD)": "Rent (USD)"}
    )

    df_salary = df.groupby("country")["Salary (USD)"].mean().reset_index()
    tables["map_salary"] = px.choropleth(
        df_salary,
        locations="country",
        locationmode="country names",
        color="Salary (USD)",
        title="Average Salary by Country",
        color_continuous_scale="Cividis",
        labels={"Salary (USD)": "Salary (USD)"}
    )


    df["continent"] = df["country"].apply(country_to_continent)
    df_continent = df.groupby("continent")["Meal Price (USD)"].mean().reset_index()
    tables["meal_by_continent"] = px.bar(
        df_continent,
        x="continent", y="Meal Price (USD)",
        title="Average Meal Price by Continent",
        color="continent"
    )


    tables["by_country_meal"] = px.bar(
        df.groupby("country")["Meal Price (USD)"].mean().reset_index(),
        x="country", y="Meal Price (USD)", title="Average Meal Price by Country"
    )

    tables["by_country_rent"] = px.bar(
        df.groupby("country")["Rent (USD)"].mean().reset_index(),
        x="country", y="Rent (USD)", title="Average Rent by Country"
    )

    tables["salary_vs_rent"] = px.scatter(
        df, x="Salary (USD)", y="Rent (USD)", hover_data=["city","country"],
        title="Salary vs Rent"
    )


    
    df["Preschool (monthly)"] = df["x42"]                
    df["Primary School (monthly)"] = df["x43"] / 12.0    
    df["Salary (monthly)"] = df["Salary (USD)"]

    df_edu_continent = df.groupby("continent")[["Salary (monthly)", "Preschool (monthly)", "Primary School (monthly)"]].mean().reset_index()

    tables["education_vs_salary_continent"] = px.bar(
        df_edu_continent,
        x="continent",
        y=["Salary (monthly)", "Preschool (monthly)", "Primary School (monthly)"],
        barmode="group",
        title="Private education vs Salary per continent (USD/month)",
        labels={
            "value": "USD / month",
            "variable": "Indicator",
            "continent": "Continent"
        },
        color_discrete_map={
            "Salary (monthly)": "white",
            "Preschool (monthly)": "red",
            "Primary School (monthly)": "orange"
        }
    )

    df_edu_country = (
        df.groupby("country")[["Salary (monthly)", "Preschool (monthly)", "Primary School (monthly)"]]
        .mean()
        .reset_index()
    )

    # we create an index to measure the relative cost of education compared to salary
    #Index = 1 means that on average, families spend 100% of the average salary on education (preschool + primary)


    df_edu_country["Preschool ratio"] = df_edu_country["Preschool (monthly)"] / df_edu_country["Salary (monthly)"]
    df_edu_country["Primary ratio"] = df_edu_country["Primary School (monthly)"] / df_edu_country["Salary (monthly)"]
    df_edu_country["Education Index"] = df_edu_country[["Preschool ratio", "Primary ratio"]].mean(axis=1)

    # Top 10 countries where education is the most expensive relative to salary
    top10 = df_edu_country.sort_values("Education Index", ascending=False).head(10)

    tables["education_vs_salary_top10"] = px.bar(
        top10,
        x="Education Index",
        y="country",
        orientation="h",
        title="Top 10 countries: Private education cost relative to Salary",
        labels={
            "Education Index": "Average ratio (school fees / salary)",
            "country": "Country"
        },
        color="Education Index",
        color_continuous_scale="Reds"
    )



    df["Liters affordable"] = df["Salary (USD)"] / df["x33"]
    df_gas = df.groupby("country")["Liters affordable"].mean().reset_index()
    tables["map_gasoline"] = px.choropleth(
        df_gas,
        locations="country",
        locationmode="country names",
        color="Liters affordable",
        title="Liters of Gasoline Affordable per Monthly Salary",
        color_continuous_scale="YlOrRd",
        labels={"Liters affordable": "Liters affordable"}
    )

    df["Transport ratio"] = df["x29"] / df["Salary (USD)"]

    df_transport = df.groupby("continent")["Transport ratio"].mean().reset_index()
    tables["transport_vs_salary_continent"] = px.bar(
        df_transport,
        x="continent",
        y="Transport ratio",
        title="Public Transport Monthly Pass vs Salary (by continent)",
        labels={"Transport ratio": "Share of Salary"},
        color="Transport ratio",
        color_continuous_scale="Oranges"
    )

    

    df_beer_ratio_country = df.groupby("country").apply(
        lambda g: pd.Series({
            "Restaurant ratio": (g["x5"] / g["x4"]).mean(),
            "Market ratio": (g["x26"] / g["x25"]).mean()
        })
    ).reset_index()

    fig_beer = px.scatter(
        df_beer_ratio_country,
        x="Restaurant ratio",
        y="Market ratio",
        hover_name="country", 
        title="Imported vs Domestic Beer Price Ratio",
        labels={
            "Restaurant ratio": "Imported / Domestic (Restaurant)",
            "Market ratio": "Imported / Domestic (Market)"
        }
    )

    fig_beer.add_shape(type="line", x0=1, x1=1,
                    y0=0, y1=df_beer_ratio_country["Market ratio"].max(),
                    line=dict(color="red", dash="dash"))
    fig_beer.add_shape(type="line", x0=0, x1=df_beer_ratio_country["Restaurant ratio"].max(),
                    y0=1, y1=1,
                    line=dict(color="red", dash="dash"))

    tables["beer_ratio_scatter"] = fig_beer

    top15_beer = df_beer_ratio_country.sort_values("Restaurant ratio", ascending=False).head(15)
    tables["beer_ratio_top15"] = px.bar(
        top15_beer,
        x="Restaurant ratio",
        y="country",
        orientation="h",
        title="Top 15 Countries: Imported Beer vs Domestic (Restaurant)",
        labels={"Restaurant ratio": "Ratio Imported / Domestic", "country": "Country"},
        color="Restaurant ratio",
        color_continuous_scale="Blues"
    )




    

    return tables
