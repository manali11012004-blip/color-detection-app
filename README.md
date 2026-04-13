# 🎨 Streamlit Color Detection App

## 📌 Overview

This project is a web-based application that allows users to detect the color of any pixel in an image.
Users can upload an image and click on any point to identify the color name along with its RGB values.

---

## 🚀 Features

* Upload image (JPG, PNG, JPEG)
* Click anywhere on the image to detect color
* Displays:

  * 🎯 Color name
  * 📍 Pixel coordinates
  * 🎨 RGB values
* Real-time color preview box
* Simple and interactive UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* NumPy
* Pandas
* Pillow (PIL)
* OpenCV
* streamlit-image-coordinates

---

## 📂 Project Structure

```
color-detection-app/
│
├── app.py
├── color_detection.ipynb
├── colors.csv
├── requirements.txt
├── README.md
│
└── images/
    ├── demo_input.jpg
    ├── output1.png
    ├── output2.png
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/manali11012004-blip/color-detection-app.git
cd color-detection-app
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```

---

## 📸 Demo

### 🔹 Input Image

(Add your uploaded image screenshot here)

### 🔹 Output

(Add screenshots showing detected color results)

---

## ⚠️ Note

* This project uses a **rule-based approach** (Manhattan distance) for color matching.
* It is **not a Machine Learning model**.

---

## 📌 Future Improvements

* Add HEX color output
* Show top 3 closest colors
* Improve accuracy using Euclidean distance
* Convert into ML-based color classifier
* Add download color palette feature

---

## 👨‍💻 Author

Manali S. Awale

---
