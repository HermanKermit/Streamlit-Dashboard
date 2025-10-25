import streamlit as st
from utils.viz import show_chart



def show(tables):
    st.title("Deep Dives")

    st.markdown("""
    Now we delve into data that is a little less obvious, 
    but which can nevertheless tell us a lot about socioeconomic
                situations or quality of life. Let us take : 
    """)
                
    st.subheader("Gasoline affordability")
    st.markdown("""
    This map shows how many liters of gasoline can be purchased with an average monthly salary.  
    It highlights the contrast between **oil-producing countries** 
                (where fuel is cheap relative to income) 
    and **import-dependent countries** (where fuel is expensive).
    """)
    st.plotly_chart(tables["map_gasoline"], use_container_width=True)

    st.markdown("""
    In an oil-producing country like Libya, Saudi Arabia (as we can see on the map), the 
                price per liter is low even with a relatively low average salary, 
                you can buy a lot of liters.

In an importing country with high taxes (Western Europe),
                 the price per liter is high even with a good salary, the number 
                of liters that can be purchased is much lower.

This highlights not only income differences, but also 
                energy and tax policies.

                
Also, this doesn't mean that residents actually consume the 
                same amount of gasoline. 
                This is a theoretical indicator,
                 used to compare relative affordability between countries.
    """)


    st.subheader("Public transport affordability")
    st.markdown("""
    Here we measure the cost of a monthly public transport pass as a share of salary at 
                the continent level.  
    """)
    st.plotly_chart(tables["transport_vs_salary_continent"], use_container_width=True)

    st.markdown("""
   South America and Africa = highest shares. This 
                means that, even if the absolute price of
                 the pass isn't necessarily huge in dollar terms, it weighs heavily relative to local wages.

Europe, Asia, North America, Oceania = lower shares. 
                Here, wages are higher and/or public transport 
                is subsidized, so the relative burden is lighter.

It highlights unequal access to mobility : in some 
                regions, traveling by public transport represents a real financial outlay.

It's a good indirect indicator of public policy: subsidies, infrastructure, budget priorities.

As with gasoline, this clearly illustrates that the absolute price is not enough: what matters is the price relative to income.
    Gasoline + public transport show how salaries translate 
                into real-world access to services.
                 
    """)

    st.markdown("""
    ---
    """)
    st.subheader("Imported vs Domestic Beer Ratios")
    st.markdown("""
    This scatter plot shows the ratio Imported / Domestic for beer.  
    - A value of **1** means imported beer costs the same as local.  
    - A value of **2** means imported beer is twice as expensive.  
    - Countries above/right of the red lines mean imported beer is more expensive both in restaurants and supermarkets.
    """)

    st.plotly_chart(tables["beer_ratio_scatter"], use_container_width=True)

    st.markdown("""
    ---
    ### Top 15 countries (restaurant prices)
    These are the countries where imported beer is the most expensive compared to domestic.  
    """)
    st.plotly_chart(tables["beer_ratio_top15"], use_container_width=True)


    st.markdown("""
    In these countries, drinking imported beer is a 
                luxury, reserved for a minority, 
                probably due to taxes, logistics costs, or protectionist policies.


- These differences often reflect high customs duties or restrictions on alcohol imports.

- In countries with low average incomes,
                 even a small absolute additional cost translates into a huge ratio.

- The more a country produces its own beer, the more competitive the local beer becomes, and the more expensive the imported beer seems.

So consuming local products is 
                 encouraged voluntarily or by economic constraint.

The price gap becomes an indirect indicator of protectionism and the level of trade openness.

It is also a good example of how a banal product like beer 
                can reveal economic dynamics.
    """)
