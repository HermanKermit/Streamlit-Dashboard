import streamlit as st
from utils.viz import show_chart

def show(tables):
    st.title("Overview")

    st.markdown("""
    I made the **Overview** section to make a first snapshot of the dataset.  
    Firstly, we highlight three indicators that structure the cost of living :
    - **Average Meal Price**
    - **Average Rent**
    - **Average Salary**

    These three KPIs (Key Performance Indicator) form the basis of our analysis.
    """)

    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("Average Meal in USD", f"{tables['kpis']['avg_meal']:.2f}")
    c2.metric("Average Rent in USD", f"{tables['kpis']['avg_rent']:.0f}")
    c3.metric("Average Salary in USD", f"{tables['kpis']['avg_salary']:.0f}")

    st.markdown("""
    ---
    ### Country-level comparisons
    We compare **meals** and **rents** across countries.  
    These charts reveal where daily consumption is cheap or expensive, and where housing costs dominate household budgets.
    """)

    st.markdown("""
    But of course theses graphs do not tell us anything as they are. There are many countries for a direct comparison.
    Let's first take a look on the map we can draw from these data. 
                
                    """)



    show_chart(tables["by_country_meal"])
    show_chart(tables["by_country_rent"])
    show_chart(tables["salary_vs_rent"])
    show_chart(tables["map_meal"])
    show_chart(tables["map_rent"])
    show_chart(tables["map_salary"])

    st.markdown("""
    We can visualize better the regions where the cost of living is the highest. 
    Let us now move to a more detailed analysis by continent.
                
    ---
 
    """)


    st.subheader("Meal Prices by Continent")
    st.markdown("""
    By aggregating at the **continent level** (using ), we smooth out local variations and highlight broader regional patterns.  
    For example:
    - North America and Europe show higher average meal prices = higher living standards, and higher costs.
    - Africa and Asia appear cheaper, but this must later be compared to income levels to get the real affordability.
    """)
    show_chart(tables["meal_by_continent"])

    st.subheader("Education vs salary")
    st.markdown("""
    Education is a long-term investment for families.  
    Now we compare average monthly salary with 
    the monthly cost of private preschool
    and the monthly equivalent of international primary school fee.

    - If the bars for education are close to or higher than the salary bar, it means private schooling is financially inaccessible for the average household.
    - If the salary bar is much higher, private education is more affordable relative to income.

    To make this comparison clearer, we also compute an **Education Index**:
    - It is the average ratio of school fees (preschool + primary) to salary.
    - A value of `1.0` means one month of salary is needed to pay one month of school fees.
    - A value of `>2` means two or more salaries are required.
    """)

    st.plotly_chart(tables["education_vs_salary_continent"], use_container_width=True)

    st.markdown("""
                
    The ratio in some continents is worrying:
    In Africa, on average, families must spend nearly 2 months of salary to
        afford one month of preschool.
    ---
    ### Top 10 countries where private education is least affordable
    This ranking shows the countries where private education costs represent the largest share of income.  
    It does not  mean that education is the most expensive in money terms, but that salaries are too low compared to fees.

    This index is a powerful lens on **inequality of access**.
    """)

    st.plotly_chart(tables["education_vs_salary_top10"], use_container_width=True)

    st.markdown("""
    ---
    ### Where do we go from here?
    We have seen basic costs vs. income (meals, rent, salary).
    In the *Deep dives part* we will explore other domains with the same logic: 
                **absolute prices vs. relative affordability**.
    """)


  
