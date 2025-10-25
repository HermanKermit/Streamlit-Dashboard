import streamlit as st

def show():
    st.title("Explore the Cost of Living Worldwide")

    st.markdown("""

This project draws on a VERY rich dataset, compiled from [Numbeo](https://www.numbeo.com/cost-of-living/) data.  
It gathers detailed information on **more than 50 prices and income indicators** such as :

- **Food** : restaurant meals, basic goods (bread, rice, meat, fruits, vegetables)
- **Beverages & Tobacco** : beer, wine, coffee, sodas, cigarettes
- **Transport** : bus tickets, gas, taxis, new cars
- **Housing** : rents, prices per square meter, utilities, mortgage rates
- **Services & Leisure** : internet, cinema, sports, clothing
- **Education** : kindergarten and international school fees
- **Income** : average net salary after taxes

### Why is this dataset valuable?
It will allow us to **compare the cost of living between countries and continents**.

### What we will explore
- **Price gaps** between continents and countries.
- **Relative purchasing power**: how many meals, rent, or tuition can an average salary finance?
- **World rankings**: where is life most expensive, and where is it most affordable?

---
We will try to make this dataset speak about the daily lives, inequalities, and economic choices of people around the world.

        """)
