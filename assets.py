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


col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/otherdeed" target="_blank">Ape Land</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/otherdeed/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

#   #####################
# Collection 1
# ########################
    st.write(f"------------------------------------------------------")

with col2:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/fvck-crystal" target="_blank">Crystals x7</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/fvck-crystal/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"],3),f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

#   #####################
# Collection 2
# ########################
    st.write(f"------------------------------------------------------")

with col3:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/hiddeninnoise" target="_blank">Hidden in Noise x3</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/hiddeninnoise/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

    #   #####################
    # Collection 3
    # ########################
    st.write(f"------------------------------------------------------")

with col1:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/cryptoadz-by-gremplin" target="_blank">Cryptoadz</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/cryptoadz-by-gremplin/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))


#   #####################
# Collection 4
# ########################
    st.write(f"------------------------------------------------------")

with col2:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/lvcidiaavatars" target="_blank">Fvck Avatars x12</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/lvcidiaavatars/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"],3),f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

#   #####################
# Collection 5
# ########################
    st.write(f"------------------------------------------------------")

with col3:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/madrabbitsriotclub" target="_blank">Mad Rabbits x11 </a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/madrabbitsriotclub/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"],3),f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

    #   #####################
    # Collection 6
    # ########################
    st.write(f"------------------------------------------------------")

with col1:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/m" target="_blank">Merge</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/m/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"],3),f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

    #   #####################
    # Collection 7
    # ########################
    st.write(f"------------------------------------------------------")

with col2:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/creatureworld" target="_blank">Creature World x4</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/creatureworld/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", response["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))
    #   #####################
    # Collection 8
    # ########################
    st.write(f"------------------------------------------------------")

with col3:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/superlativesecretsociety" target="_blank">SuperlativeSS x3 </a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/superlativesecretsociety/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))
    # ########################
    # Collection 9
    # ########################
    st.write(f"------------------------------------------------------")

with col1:

    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/lostpoets" target="_blank">Pages/Poets</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/lostpoets/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))
    # ########################
    # Collection 10
    # ########################

    st.write(f"------------------------------------------------------")

with col2:

    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/graycraft-2" target="_blank">Graycraft2 x3 </a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/graycraft-2/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))


#

    #     #   #####################
    #     # Collection 11
    #     # ########################

    st.write(f"------------------------------------------------------")
with col3:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/mev-army" target="_blank">MEV army</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/mev-army/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"], 3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

#     #   #####################
#     # Collection 12
#     # ########################

    st.write(f"------------------------------------------------------")

with col2:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/thefatedrenegades" target="_blank">Moons of Mars x22</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/thefatedrenegades/stats"
    r = requests.get(url)
    response_cw = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"], f"ETH")
    st.write(f"24h avg price:", round(r.json()["stats"]["one_day_average_price"],3), f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

#   #####################
# Collection 3
# ########################
with col1:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/Fomoverse" target="_blank">Fomoverse</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/fomoverse/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"],3),f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))

with col3:
    st.markdown(
        """<a style='display: block; text-align: center; font-size: 28px' href="https://opensea.io/collection/fanggangnft" target="_blank">Fang Gang</a>
        """,
        unsafe_allow_html=True,
    )
    url = "https://api.opensea.io/api/v1/collection/fanggangnft/stats"
    r = requests.get(url)
    response = r.json()
    st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
    st.write(f"24h Average price:", round(response["stats"]["one_day_average_price"],3),f"ETH")
    st.write(f"24h sales:", round(response["stats"]["one_day_sales"]))
    st.write(f"Sales in last 7 days", round(response["stats"]["seven_day_sales"]))
    st.write(f"Unique owners:", r.json()["stats"]["num_owners"], f"/", round(response["stats"]["count"]))
