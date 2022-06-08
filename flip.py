import streamlit as st
import requests, json


# # select box - drop menu > select one of the offered collections: and all data will be printed out.
# endpoint = st.sidebar.selectbox("Collection", ['cooldogsofficial', 'deadfellaz' , 'smilesssvrs'])
#
# id = endpoint #variable for using "slug" collectiong name
# url = "https://api.opensea.io/api/v1/collection/{0}/stats".format(id)
#
# r = requests.get(url)
#
#

#
# st.header(id)
# st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
# st.write(f"24h Volume:", r.json()["stats"]["one_day_volume"],f"ETH")
# st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
# st.write(f"Number of sales in last 7 days", r.json()["stats"]["seven_day_sales"])
# st.write(f"Number of sales in last 30 days", r.json()["stats"]["thirty_day_sales"])
# st.write(f"24h AVG price:", r.json()["stats"]["one_day_average_price"],f"ETH")
# st.write(f"Unique owners:", r.json()["stats"]["num_owners"],f"/", r.json()["stats"]["count"] )

col1, col2 = st.columns(2)

#   #####################
# Collection 1
# ########################


with col1:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 42px' href="https://opensea.io/collection/vividlimited" target="_blank">Vivid</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/vividlimited/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"------------------------------------------------------")
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h AVG price:", r.json()["stats"]["one_day_average_price"],f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", r.json()["stats"]["count"])
    st.write(f"24h Volume:", r.json()["stats"]["one_day_volume"], f"ETH")
    st.write(f"Number of sales in last 7 days", r.json()["stats"]["seven_day_sales"])
    st.write(f"Number of sales in last 30 days", r.json()["stats"]["thirty_day_sales"])
    st.write(f"------------------------------------------------------")


#   #####################
# Collection 2
# ########################
with col2:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 42px' href="https://opensea.io/collection/mev-army" target="_blank">MEV army</a>
        """,
        unsafe_allow_html=True,
    )

    url = "https://api.opensea.io/api/v1/collection/mev-army/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"------------------------------------------------------")

    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h AVG price:", r.json()["stats"]["one_day_average_price"],f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", r.json()["stats"]["count"])
    st.write(f"24h Volume:", r.json()["stats"]["one_day_volume"], f"ETH")
    st.write(f"Number of sales in last 7 days", r.json()["stats"]["seven_day_sales"])
    st.write(f"Number of sales in last 30 days", r.json()["stats"]["thirty_day_sales"])
    st.write(f"------------------------------------------------------")

#   #####################
# Collection 3
# ########################

with col1:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 42px' href="https://opensea.io/collection/sketchy-ape-comic-club" target="_blank">SACC</a>
        """,
        unsafe_allow_html=True,
    )
    st.write(f"------------------------------------------------------")

    url = "https://api.opensea.io/api/v1/collection/sketchy-ape-comic-club/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h AVG price:", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", r.json()["stats"]["count"])
    st.write(f"24h Volume:", r.json()["stats"]["one_day_volume"], f"ETH")
    st.write(f"Number of sales in last 7 days", r.json()["stats"]["seven_day_sales"])
    st.write(f"Number of sales in last 30 days", r.json()["stats"]["thirty_day_sales"])
#   #####################
# Collection 3
# ########################

with col2:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 42px' href="https://opensea.io/collection/sketchy-ape-book-club" target="_blank">SABC</a>
        """,
        unsafe_allow_html=True,
    )
    st.write(f"------------------------------------------------------")

    url = "https://api.opensea.io/api/v1/collection/sketchy-ape-book-club/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h AVG price:", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", r.json()["stats"]["count"])
    st.write(f"24h Volume:", r.json()["stats"]["one_day_volume"], f"ETH")
    st.write(f"Number of sales in last 7 days", r.json()["stats"]["seven_day_sales"])
    st.write(f"Number of sales in last 30 days", r.json()["stats"]["thirty_day_sales"])
