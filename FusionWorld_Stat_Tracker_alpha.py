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
    {"name": "FB01-001 U7 Son Goku", "color": "red", "set": "FB01"},
    {"name": "FB01-002 Beerus", "color": "red", "set": "FB01"},
    {"name": "FB01-035 Goku Black", "color": "blue", "set": "FB01"},
    {"name": "FB01-036 Trunks : Future", "color": "blue", "set": "FB01"},
    {"name": "FB01-070 Android 17", "color": "green", "set": "FB01"},
    {"name": "FB01-071 Son Gohan : Childhood", "color": "green", "set": "FB01"},
    {"name": "FB01-104 Ginyu", "color": "yellow", "set": "FB01"},
    {"name": "FB01-105 Cooler", "color": "yellow", "set": "FB01"},
    {"name": "FB02-001 ToPku", "color": "red", "set": "FB02"},
    {"name": "FB02-036 Zamasu : Fused", "color": "blue", "set": "Fb02"},
    {"name": "FB02-070 Cell", "color": "green", "set": "FB02"},
    {"name": "FB02-105 Y-Vegeta", "color": "yellow", "set": "FB02"},
    {"name": "FB03-001 Jiren", "color": "red", "set": "FB03"},
    {"name": "FB03-027 HaloKu", "color": "blue", "set": "FB03"},
    {"name": "FB03-053 Piccolo", "color": "green", "set": "FB03"},
    {"name": "FB03-070 Babidi", "color": "yellow", "set": "FB03"},
    {"name": "FB03-104 Son Goku : GT", "color": "black", "set": "FB03"},
    {"name": "FB04-001 UI Goku", "color": "red", "set": "Fb04"},
    {"name": "FB04-026 Son Gohan : Adolescence", "color": "blue", "set": "FB04"},
    {"name": "FB04-051 G-Vegeta", "color": "green", "set": "FB04"},
    {"name": "FB04-077 Majin Buu : Evil", "color": "yellow", "set": "FB04"},
    {"name": "FB04-103 Baby Vegeta", "color": "black", "set": "FB04"},
    {"name": "FB05-001 Son Goku (mini) : DA", "color": "red", "set": "FB05"},
    {"name": "FB05-025 Vegito", "color": "blue", "set": "FB05"},
    {"name": "FB05-049 Nameku v1", "color": "green", "set": "FB05"},
    {"name": "FB05-072 Janemba", "color": "yellow", "set": "FB05"},
    {"name": "FB05-095 B-Gogeta", "color": "black", "set": "FB05"},
    {"name": "FB06-001 Android 18", "color": "red", "set": "FB06"},
    {"name": "FB06-025 Son Goku : Childhood", "color": "blue", "set": "FB06"},
    {"name": "FB06-048 Broly : BR", "color": "green", "set": "FB06"},
    {"name": "FB06-071 King Gomah : DA", "color": "yellow", "set": "FB06"},
    {"name": "FB06-095 King Piccolo", "color": "black", "set": "FB06"},
    {"name": "SB01.001 Cell", "color": "red", "set": "SB01"},
    {"name": "SB01-029 Majin Buu : Evil", "color": "yellow", "set": "SB01"},
    {"name": "SB01-045 Bulma", "color": "black", "set": "SB01"},
    {"name": "FB07-001 Gloria : DA", "color": "red", "set": "FB07"},
    {"name": "FB07-025 Syn Shenron", "color": "blue", "set": "FB07"},
    {"name": "FB07-049 Piccolo : SH", "color": "green", "set": "FB07"},
    {"name": "FB07-073 Golden Frieza", "color": "yellow", "set": "FB07"},
    {"name": "FB07-097 Draon Ball", "color": "black", "set": "FB07"},
    {"name": "SB02-001 Trunks : Future", "color": "red", "set": "SB02"},
    {"name": "SB02-017 Gotenks", "color": "blue", "set": "SB02"},
    {"name": "SB02-033 Nameku v2", "color": "green", "set": "SB02"},
    {"name": "FB08-001 Son Gohan : Adolescence", "color": "red", "set": "FB08"},
    {"name": "FB08-025 Caulifla", "color": "blue", "set": "FB08"},
    {"name": "FB08-049 Turles", "color": "green", "set": "FB08"},
    {"name": "FB08-073 Broly", "color": "yellow", "set": "FB08"},
    {"name": "FB08-097 Son Goku Jr.", "color": "black", "set": "FB08"},
    {"name": "FB09-001 Gogeta : BR", "color": "red", "set": "FB09"},
    {"name": "FB09-025 MUI Goku", "color": "blue", "set": "FB09"},
    {"name": "Fb09-049 Son Gohan : SH", "color": "green", "set": "FB09"},
    {"name": "FB09-073 Y-Gogeta", "color": "yellow", "set": "FB09"},
    {"name": "FB09-097 Gogeta : GT", "color": "black", "set": "FB09"},
    {"name": "FS01-01 StarterKu", "color": "red", "set": "FS01"},
    {"name": "FS02-01 B-Vegeta", "color": "blue", "set": "FS02"},
    {"name": "FS03-01 Broly", "color": "green", "set": "FS03"},
    {"name": "FS04-01 Frieza", "color": "yellow", "set": "FS04"},
    {"name": "FS05-01 Bardock", "color": "black", "set": "FS05"},
    {"name": "FS06-01 Son Goku (MINI) : DA", "color": "red", "set": "FS06"},
    {"name": "FS07-01 Vegeta (MINI) : DA", "color": "blue", "set": "FS07"},
    {"name": "FS08-01 Vegeta (MINI) : DA Ssj3", "color": "yellow", "set": "FS08"},
    {"name": "FS09-01 Shallot", "color": "black", "set": "FS09"},
    {"name": "FS10-01 Giblet", "color": "green", "set": "FS10"},
    {"name": "FS11-01 Son Goku Ssj3", "color": "yellow", "set": "FS11"},
    {"name": "FS12-01 B-Nameku", "color": "black", "set": "FS12"}]


# -------------------------
# ⚙️ Setup
# -------------------------
st.markdown(
    "<h1 style='text-align: center;'>Fusion World Stats Tracker</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>by Sn0wEye</p>",
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
user = st.selectbox(
    "Spieler auswählen",
    users,
    index=0,
    key="user_select")


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
# -------------------------
# 🔒 JSON Backup (Passwort-geschützt)
# -------------------------
st.subheader("Matches JSON Backup")

# Passwort aus st.secrets ziehen
# In .streamlit/secrets.toml musst du z.B. haben:
# download_password = "meinSuperGeheimesPasswort"
DOWNLOAD_PASSWORD = st.secrets["download_password"]

# Passwortfeld
password_input = st.text_input(
    "Passwort eingeben, um JSON herunterzuladen:", 
    type="password"
)

# Prüfen
if password_input == DOWNLOAD_PASSWORD:
    st.download_button(
        label="Matches als JSON herunterladen",
        data=json.dumps(matches, indent=4),
        file_name="matches_backup.json",
        mime="application/json"
    )
elif password_input:
    st.warning("Falsches Passwort! 🔒")
