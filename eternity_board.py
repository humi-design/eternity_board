import streamlit as st
import pandas as pd

# ----------------------------------
# PAGE SETTINGS
# ----------------------------------

st.set_page_config(
    page_title="Eternity Leaderboard",
    layout="wide"
)

# ----------------------------------
# COSMIC STYLE
# ----------------------------------

st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #020111 0%, #000000 100%);
    color: white;
}

.big-title {
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    background: linear-gradient(90deg,#7afcff,#feff9c,#ff80f9);
    -webkit-background-clip: text;
    color: transparent;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 20px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🌌 ETERNITY LEADERBOARD</div>', unsafe_allow_html=True)

# ----------------------------------
# SAMPLE DATABASE
# ----------------------------------

data = [
    {"Name": "Aditi Sharma", "Role": "Campus Ambassador",
     "Points": 320, "Photo": "https://i.pravatar.cc/150?img=5"},

    {"Name": "Rohan Mehta", "Role": "Core Team",
     "Points": 450, "Photo": "https://i.pravatar.cc/150?img=8"},

    {"Name": "Priya Singh", "Role": "Volunteer",
     "Points": 280, "Photo": "https://i.pravatar.cc/150?img=12"},
]

df = pd.DataFrame(data)

# Sort ranking
df = df.sort_values(by="Points", ascending=False).reset_index(drop=True)
df["Rank"] = df.index + 1

# ----------------------------------
# VIEW MODE SELECTION
# ----------------------------------

mode = st.sidebar.selectbox("Access Mode", ["Participant View", "Admin View"])

# ==================================
# PARTICIPANT VIEW (READ ONLY)
# ==================================

if mode == "Participant View":

    st.subheader("🏆 Top Cosmic Leaders")

    for i, row in df.iterrows():

        col1, col2, col3, col4 = st.columns([1, 4, 2, 1])

        with col1:
            st.image(row["Photo"], width=80)

        with col2:
            st.markdown(f"### {row['Name']}")
            st.write(f"✨ {row['Role']}")

        with col3:
            st.markdown(f"## ⭐ {row['Points']}")

        with col4:
            st.markdown(f"## 👑 #{row['Rank']}")

        st.divider()

# ==================================
# ADMIN VIEW (PASSWORD PROTECTED)
# ==================================

else:

    password = st.sidebar.text_input("Admin Password", type="password")

    if password != "eternity_admin":

        st.warning("🔐 Admin access required")

    else:

        st.success("Admin Access Granted")

        st.subheader("⚙️ Manage Points")

        selected_user = st.selectbox("Select Participant", df["Name"])

        points = st.number_input("Add Points", 0, 1000, 10)

        if st.button("Assign Points"):
            df.loc[df["Name"] == selected_user, "Points"] += points
            st.success("Points Updated!")

        st.subheader("📊 Updated Leaderboard")

        df = df.sort_values(by="Points", ascending=False).reset_index(drop=True)
        df["Rank"] = df.index + 1

        st.dataframe(df)
