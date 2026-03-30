import streamlit as st
from utils.menu import show_menu

show_menu()

st.title("📍 Zone étudiée")


REGIONS = ["IGB", "Africa", "data_augmentation\\IGB", "data_augmentation\\Africa"]


with st.form("form_zone_etudiee"):
    region = st.selectbox("Région", options=REGIONS, index=REGIONS.index(st.session_state.region))

    st.markdown("#### Coordonnées géographiques")
    st.caption("Laisser min = max pour un point unique.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Point minimum**")
        lon_min = st.number_input("Longitude min (°)", value=st.session_state.lon_min, step=0.01, format="%.4f")
        lat_min = st.number_input("Latitude min (°)", value=st.session_state.lat_min, step=0.01, format="%.4f")
    with col2:
        st.markdown("**Point maximum**")
        lon_max = st.number_input("Longitude max (°)", value=st.session_state.lon_max, step=0.01, format="%.4f")
        lat_max = st.number_input("Latitude max (°)", value=st.session_state.lat_max, step=0.01, format="%.4f")

    map_df = pd.DataFrame({
        "lat": [lat_min, lat_max],
        "lon": [lon_min, lon_max],
    })
    st.map(map_df, zoom=6)

    submitted = st.form_submit_button("Valider")

if submitted:
    st.session_state.region = region 
    st.session_state.lon_min = lon_min
    st.session_state.lat_min = lat_min
    st.session_state.lon_max = lon_max
    st.session_state.lat_max = lat_max

    st.success("Configuration sauvegardée !")