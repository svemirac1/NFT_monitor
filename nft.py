import streamlit as st
import requests, json

endpoint = st.sidebar.selectbox("Collection", ['creature-world-collection', 'fvck-crystal', 'fanggangnft', 'bad-bunnies-nft', 'capsulehouse',
                                               'madrabbitsriotclub', 'mutant-ape-yacht-club', 'sunsignals', 'hiddeninnoise', 'nftsiblings',
                                                'lostpoets','cryptoadz-by-gremplin', 'winterbears','galaxyeggs9999',
                                               'superlativesecretsociety', 'graycraft-2', 'savage-droids', 'f1-delta-time'])
id = endpoint
url = "https://api.opensea.io/api/v1/collection/{0}/stats".format(id)

r = requests.get(url)

st.header(id)
st.write(f"floor price:", r.json()["stats"]["floor_price"],f"ETH")
st.write(f"24h Volume:", r.json()["stats"]["one_day_volume"],f"ETH")
st.write(f"24h sales:", r.json()["stats"]["one_day_sales"])
s
st.write(f"Number of sales in last 30 days", r.json()["stats"]["thirty_day_sales"])
st.write(f"24h AVG price:", r.json()["stats"]["one_day_average_price"],f"ETH")
st.write(f"Unique owners:", r.json()["stats"]["num_owners"],f"/", r.json()["stats"]["count"] )

