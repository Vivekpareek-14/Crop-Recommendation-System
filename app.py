import streamlit as st
import numpy as np
import joblib

# Load the trained model and scalers
model = joblib.load('model.pkl')
sc = joblib.load('standscaler.pkl')
mx = joblib.load('minmaxscaler.pkl')

# Crop Dictionary with Emojis
crop_dict = {
    1: "🌾 Rice", 2: "🌽 Maize", 3: "🧵 Jute", 4: "👕 Cotton", 5: "🥥 Coconut",
    6: "🍈 Papaya", 7: "🍊 Orange", 8: "🍏 Apple", 9: "🍉 Muskmelon", 10: "🍉 Watermelon",
    11: "🍇 Grapes", 12: "🥭 Mango", 13: "🍌 Banana", 14: "🍎 Pomegranate",
    15: "🥣 Lentil", 16: "🫘 Blackgram", 17: "🟢 Mungbean", 18: "🟤 Mothbeans",
    19: "🟠 Pigeonpeas", 20: "🔴 Kidneybeans", 21: "🧆 Chickpea", 22: "☕ Coffee"
}

# Fun Messages
fun_messages = {
    "🌾 Rice": "🍚 Get ready for a rice-yielding adventure!",
    "🌽 Maize": "🌽 Corn-gratulations! Your farm is popping with potential!",
    "🧵 Jute": "🧵 Time to weave success! Jute is your golden thread to prosperity.",
    "👕 Cotton": "👕 Soft and fluffy profits ahead! Cotton is a smooth choice!",
    "🥥 Coconut": "🥥 Crack open success! Your coconut farm is going nuts!",
    "🍈 Papaya": "🍈 Sweet and tropical vibes! Your farm will be a papaya paradise!",
    "🍊 Orange": "🍊 Juicy profits ahead! Your oranges will make the world zestier!",
    "🍏 Apple": "🍏 An apple a day keeps bad crops away! Great choice!",
    "🍉 Muskmelon": "🍉 Sweet victory! Your muskmelon farm will be a juicy hit!",
    "🍉 Watermelon": "🍉 Refreshing and sweet! Your watermelon farm will be a cool success!",
    "🍇 Grapes": "🍇 Time to crush it! Your grapes are going to make a fine harvest!",
    "🥭 Mango": "🥭 The king of fruits has arrived! Your mangoes will rule the farm!",
    "🍌 Banana": "🍌 Going bananas for profits! Your farm is on the right peel!",
    "🍎 Pomegranate": "🍎 A seedy but fruitful decision! Pomegranates will bring juicy success!",
    "🥣 Lentil": "🥣 A lentil-tastic choice! Protein-packed profits await!",
    "🫘 Blackgram": "🫘 The dark horse of pulses! Blackgram is a smart pick!",
    "🟢 Mungbean": "🟢 Tiny but mighty! Mungbean will sprout success in no time!",
    "🟤 Mothbeans": "🟤 Tough and resilient! Your mothbeans will stand strong!",
    "🟠 Pigeonpeas": "🟠 Peas and prosperity! Your pigeonpeas will thrive!",
    "🔴 Kidneybeans": "🔴 A beany good choice! Kidneybeans will bring hearty harvests!",
    "🧆 Chickpea": "🧆 Hummus your way to success! Chickpeas will bring in great returns!",
    "☕ Coffee": "☕ Brew-tiful choice! Your coffee farm is going to wake up the world! 🌍"
}


# Set Page Configuration
st.set_page_config(page_title="Crop Prediction", page_icon="🌱", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        /* General Page Background */
        body {
            background: #F4F9F4;
        }

        /* Title Styling */
        .title {
            color: #2E8B57;
            text-align: center;
            font-size: 45px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .subtext {
            color: #666;
            text-align: center;
            font-size: 18px;
            font-style: italic;
            margin-bottom: 30px;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: #1E1E1E !important;
            color: white;
        }

        .sidebar-box {
            background: rgba(46, 139, 87, 0.8);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.2);
        }

        /* Centered Button */
        .center-button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 15px;
            margin-bottom: 20px;
        }

        /* Result Box */
        .result-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #008080;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
        }

        .fun-message {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #2E8B57;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown("<h1 class='title'>🌱 Crop Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Enter required data, and we'll tell you which crop to grow! 🚜</p>", unsafe_allow_html=True)

# Sidebar Input Section with Card Styling
with st.sidebar:
    st.markdown("<div class='sidebar-box'><h2>🔍 Enter Data</h2>", unsafe_allow_html=True)

    N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=90)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=40)
    K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=120)
    temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=27.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=80.0)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=170.0)

    st.markdown("</div>", unsafe_allow_html=True)

# Predict Button - Centered
st.markdown("<div class='center-button'>", unsafe_allow_html=True)
predict_button = st.button("🌾 Predict Crop", help="Click to get the best crop recommendation")
st.markdown("</div>", unsafe_allow_html=True)

# Processing Prediction
if predict_button:
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    # Apply Transformations
    mx_features = mx.transform(single_pred)
    sc_mx_features = sc.transform(mx_features)

    # Make Prediction
    prediction = model.predict(sc_mx_features)

    # Display Result
    st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        fun_message = fun_messages.get(crop, "🌾 Get ready for a great harvest! 🚜")

        st.markdown(f"<div class='result-box'>{crop} is the best crop for your farm! </div>", unsafe_allow_html=True)
        st.markdown(f"<div class='fun-message'>{fun_message}</div>", unsafe_allow_html=True)
    else:
        st.error("❌ Sorry, we could not determine the best crop for the given data.")