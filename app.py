import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

# -------------------- LOAD CSV --------------------
csv = pd.read_csv(
    'colors.csv',
    names=["color", "color_name", "hex", "R", "G", "B"],
    header=None
)

# -------------------- COLOR FUNCTION --------------------
def getColorName(R, G, B):
    minimum = 10000
    cname = "Unknown"

    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + \
            abs(G - int(csv.loc[i, "G"])) + \
            abs(B - int(csv.loc[i, "B"]))

        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]

    return cname

# -------------------- UI --------------------
st.title("🎨 Color Detection App (Click on Image)")

uploaded_file = st.file_uploader(
    "Upload an image", type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  # ✅ ensure RGB
    img = np.array(image)

    st.write("👉 Click anywhere on the image")

    # Get click coordinates
    value = streamlit_image_coordinates(image)

    if value is not None:
        x = value["x"]
        y = value["y"]

        # ✅ FIX: Correct RGB order (PIL uses RGB)
        r, g, b = img[y, x]
        r, g, b = int(r), int(g), int(b)

        # Get color name
        color_name = getColorName(r, g, b)

        # -------------------- OUTPUT --------------------
        st.write(f"### 🎯 Color: {color_name}")
        st.write(f"📍 Coordinates: ({x}, {y})")
        st.write(f"RGB: ({r}, {g}, {b})")

        # Color preview bar
        st.markdown(
            f"""
            <div style="
                width:100%;
                height:100px;
                background-color: rgb({r},{g},{b});
                border-radius:10px;">
            </div>
            """,
            unsafe_allow_html=True
        )