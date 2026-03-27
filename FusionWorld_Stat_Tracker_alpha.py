import streamlit as st
import json
import os
import matplotlib.pyplot as plt

users = ["Denis", "Ali", "Sahid", "Ian", "Nino"]
key="search_my"
key="search_opp"
key="leader_my"
key="leader_opp"

# -------------------------
# 📦 Deck Daten
# -------------------------
decks = [
    {"name": "MUI Goku", "color": "blue", "set": "FB09"},
    {"name": "Gogeta Z", "color": "yellow", "set": "FB09"},
    {"name": "Gogeta BR", "color": "red", "set": "FB09"},
    {"name": "Goku Black", "color": "blue", "set": "FB01"},
    {"name": "Gogeta GT", "color": "black", "set": "FB09"},
]

# -------------------------
# ⚙️ Setup
# -------------------------
st.markdown(
    "<h1 style='text-align: center;'>Fusion World Stats Tracker</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>by sn0weye</p>",
    unsafe_allow_html=True
)

DATA_FILE = "matches.json"

# -------------------------
# 💾 Daten laden/speichern
# -------------------------
def load_matches():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
                json.dump([], f)

def save_matches(matches):
    with open(DATA_FILE, "w") as f:
        json.dump(matches, f, indent=4)

matches = load_matches()



#--------------------------
# Profil Auswahl
#--------------------------
st.subheader("User")
user = st.selectbox("Spieler", users)

# -------------------------
# 🔵 DEIN DECK
# -------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Dein Deck")

    search_my = st.text_input("🔍 Suche", key="search_my")

    color_my = st.selectbox(
        "Farbe",
        ["Alle", "blue", "red", "green", "yellow", "black"],
        key="color_my"
    )

    set_my = st.selectbox(
        "Set",
        ["Alle", "FB01", "FB02", "FB09"],
        key="set_my"
    )

    filtered_my = []
    for deck in decks:
        if search_my.lower() not in deck["name"].lower():
            continue
        if color_my != "Alle" and deck["color"] != color_my:
            continue
        if set_my != "Alle" and deck["set"] != set_my:
            continue
        filtered_my.append(deck)

    my_names = [d["name"] for d in filtered_my]

    if my_names:
        my_deck = st.selectbox("Leader", my_names, key="my_leader")
    else:
        st.warning("Keine Decks gefunden")
        my_deck = ""


# -------------------------
# 🔴 GEGNER DECK
# -------------------------
with col2:
    st.subheader("Gegner Deck")

    search_opp = st.text_input("🔍 Suche", key="search_opp")

    color_opp = st.selectbox(
        "Farbe",
        ["Alle", "blue", "red", "green", "yellow", "black"],
        key="color_opp"
    )

    set_opp = st.selectbox(
        "Set",
        ["Alle", "FB01", "FB02", "FB09"],
        key="set_opp"
    )

    filtered_opp = []
    for deck in decks:
        if search_opp.lower() not in deck["name"].lower():
            continue
        if color_opp != "Alle" and deck["color"] != color_opp:
            continue
        if set_opp != "Alle" and deck["set"] != set_opp:
            continue
        filtered_opp.append(deck)

    opp_names = [d["name"] for d in filtered_opp]

    if opp_names:
        opponent_deck = st.selectbox("Leader", opp_names, key="opp_leader")
    else:
        st.warning("Keine Decks gefunden")
        opponent_deck = ""

# -------------------------
# 🎮 Match Einstellungen
# -------------------------
st.markdown(" ")
st.subheader("Match Details")
first_or_second = st.selectbox(
    "First oder Second?",
    ["First", "Second"]
)

result = st.selectbox(
    "Win oder Loss?",
    ["win", "loss"]
)

# -------------------------
# 💾 Match speichern
# -------------------------
if st.button("Speichern"):
    matches.append({
        "user": user, 
        "leader": my_deck,
        "opponent": opponent_deck,
        "result": result,
        "start": first_or_second
    })
    save_matches(matches)

    st.success("Match gespeichert!")
    st.rerun()

# -------------------------
# 📊 STATISTIK
# -------------------------
with col3:
    st.header("Statistiken")

    filtered_matches = [
    m for m in matches
    if m["user"] == user
    and m["leader"] == my_deck
    and m["opponent"] == opponent_deck
    and m["start"] == first_or_second
]

    if filtered_matches:
        total = len(filtered_matches)
        wins = len([m for m in filtered_matches if m["result"] == "win"])
        winrate = (wins / total) * 100

        st.subheader("Matchup Statistik")
        st.write(f"{my_deck} vs {opponent_deck} ({first_or_second})")
        st.write(f"Spiele: {total}")
        st.write(f"Siege: {wins}")
        st.write(f"Winrate: {winrate:.1f}%")
    else:
        st.write("Noch keine Daten für dieses Matchup vorhanden")
