# 🚦 Smart Traffic Pollution Reducer

## 📌 Overview

Smart Traffic Pollution Reducer is a Machine Learning-based project designed to predict traffic congestion and estimate pollution levels. Based on these predictions, the system suggests optimized traffic signal timings to reduce vehicle idle time and emissions.

## ❗ Problem Statement

Urban traffic congestion leads to:

* Increased fuel consumption
* Higher CO₂ emissions
* Longer waiting times at traffic signals

Traditional traffic systems are static and do not adapt to real-time conditions, leading to inefficiency and environmental impact.


## 💡 Solution

This project uses Machine Learning to:

* Predict traffic congestion using input parameters
* Estimate pollution levels based on congestion
* Suggest optimized traffic signal timings

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn (Random Forest)
* Matplotlib

---

## 📁 Project Structure

```
Smart-Traffic-Pollution-Reducer/
│
├── src/
│   └── traffic_system.py
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/Smart-Traffic-Pollution-Reducer.git
cd Smart-Traffic-Pollution-Reducer
```

### 2. Install Dependencies

```
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run

```
python src/traffic_system.py
```

---

## 📊 Example Input

```
Enter hour (0-23): 9
Enter day (0=Mon ... 6=Sun): 1
Enter number of vehicles: 300
Enter temperature: 30
```

---

## 📈 Output

```
Predicted Congestion: 71.86%
Estimated CO₂ Emission: 35.93 kg/h
Signal Recommendation: Increase Green Time (60s)
```

---

## 📊 Visualization

The program generates a bar graph comparing:

* Traffic congestion level
* CO₂ emission level

This helps visualize the relationship between congestion and pollution.

---

## 🧠 How It Works

### 1. Data Generation

Synthetic traffic data is generated including:

* Hour of the day
* Day of the week
* Number of vehicles
* Temperature

### 2. Model Training

A Random Forest Regressor is trained to predict traffic congestion.

### 3. Prediction

User input is taken, and congestion is predicted using the trained model.

### 4. Pollution Estimation

Pollution is calculated based on congestion levels.

### 5. Signal Optimization

Traffic signal timing is adjusted based on predicted congestion.

---

## 🌍 Real-World Impact

This system can help:

* Reduce traffic congestion
* Lower pollution levels
* Improve fuel efficiency
* Support smart city initiatives

---

## 🚀 Future Improvements

* Use real-world traffic datasets
* Integrate real-time data sources
* Improve model accuracy
* Develop a live dashboard

---

## 🧑‍💻 Author

Your Name

---

## 📜 License

MIT License
