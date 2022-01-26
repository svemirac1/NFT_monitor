import streamlit as st
import requests, json

# endpoint = st.sidebar.selectbox("Collection", ['creatureworld', 'fvck-crystal', 'fanggangnft',
#                                                'madrabbitsriotclub', 'hiddeninnoise', 'nftsiblings',
#                                                 'lostpoets','cryptoadz-by-gremplin','m'
#                                                'superlativesecretsociety', 'graycraft-2', 'savage-droids'])
# #id = endpoint
# #url = "https://api.opensea.io/api/v1/collection/{0}/stats".format(id)
#
# #r = requests.get(url)
#

#   #####################
# Collection 1
# ########################

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center; color: blue;'>Creature World x4</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/creatureworld/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h Average price:", r.json()["stats"]["one_day_average_price"],f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

#   #####################
# Collection 2
# ########################
with col2:
    st.markdown("<h3 style='text-align: center; color: magenta;'>Crystals x6</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/fvck-crystal/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h Average price:", r.json()["stats"]["one_day_average_price"],f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

#   #####################
# Collection 3
# ########################

with col3:
    st.markdown("<h3 style='text-align: center; color: blue;'>Moons of Mars x22</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/thefatedrenegades/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h avg price:", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

#   #####################
# Collection 4
# ########################
with col1:
    st.markdown("<h3 style='text-align: center; color: blue;'>Fang Gang x4</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/fanggangnft/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h avg price:", r.json()["stats"]["one_day_average_price"],f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])


#   #####################
# Collection 5
# ########################
with col2:
    st.markdown("<h3 style='text-align: center; color: blue;'>Merge x 134</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/m/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h avg price:   \n", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

#   #####################
# Collection 6
# ########################
with col3:
    st.markdown("<h3 style='text-align: center; color: blue;'>Mad Rabbits x11 </h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/madrabbitsriotclub/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h avg price:", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

    #   #####################
    # Collection 7
    # ########################

with col1:
    st.markdown("<h3 style='text-align: center; color: blue;'>SuperlativeSS x3 </h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/superlativesecretsociety/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h avg price:", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

    #   #####################
    # Collection 8
    # ########################
with col2:
    st.markdown("<h3 style='text-align: center; color: blue;'>Graycraft2 x3</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/graycraft-2/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h avg price:   \n", r.json()["stats"]["one_day_average_price"], f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])
    #   #####################
    # Collection 9
    # ########################

with col3:
    st.markdown("<h3 style='text-align: center; color: blue;'>Hidden in Noise x3</h3>", unsafe_allow_html=True)
    url = "https://api.opensea.io/api/v1/collection/hiddeninnoise/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h avg price:", r.json()["stats"]["one_day_average_price"],f"ETH")
    st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
    st.write(f"Sales in last 7 days", r.json()["stats"]["seven_day_sales"])

# with col1:
#
#     #   #####################
#     # Collection 10
#     # ########################
# with col2:
#
#     #   #####################
#     # Collection 11
#     # ########################
# with col3:
