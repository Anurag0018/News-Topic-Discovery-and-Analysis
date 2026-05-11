# 📰 News Topic Discovery & Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

An intelligent dashboard that fetches live news articles using RSS feeds and applies **Unsupervised Machine Learning** to automatically categorize headlines into thematic clusters.

---

## 🚀 Features

- ✅ Fetches live news articles from **BBC** and **The Hindu**
- ✅ Real-time RSS parsing using `feedparser`
- ✅ Smart NLP preprocessing and text cleaning
- ✅ TF-IDF vectorization for feature extraction
- ✅ K-Means clustering for topic discovery
- ✅ Interactive Streamlit dashboard
- ✅ Dynamic topic selection using sidebar controls
- ✅ Topic frequency visualization with Matplotlib
- ✅ Export analyzed news data as CSV

---

## 📖 The NLP Pipeline

The application transforms raw news headlines into meaningful topic clusters using the following pipeline:

### 1️⃣ Text Preprocessing
- Converts text to lowercase
- Removes special characters using regex
- Removes stopwords (e.g., *the, is, and*)

### 2️⃣ TF-IDF Vectorization
Converts textual data into numerical vectors.

- **Term Frequency (TF):** Measures how often a word appears
- **Inverse Document Frequency (IDF):** Reduces importance of overly common words

### 3️⃣ K-Means Clustering
Groups similar news articles into clusters using unsupervised learning.

### 4️⃣ Topic Keyword Extraction
Extracts top keywords from each cluster to represent discovered topics.

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| **Language** | Python 3.x |
| **Frontend** | Streamlit |
| **Machine Learning** | Scikit-Learn |
| **NLP** | TF-IDF, Stopword Removal |
| **Data Handling** | Pandas |
| **Visualization** | Matplotlib |
| **RSS Parsing** | Feedparser |
| **HTTP Requests** | Requests |

---

## 📂 Project Structure

```text
News-Topic-Discovery-and-Analysis/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Anurag0018/News-Topic-Discovery-and-Analysis.git
```

---

### 2️⃣ Move into Project Directory

```bash
cd News-Topic-Discovery-and-Analysis
```

---

### 3️⃣ Create Virtual Environment (Optional)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📊 How It Works

1. Fetches RSS news feeds
2. Cleans and preprocesses article text
3. Converts text into TF-IDF vectors
4. Applies K-Means clustering
5. Displays discovered topics
6. Visualizes topic distribution
7. Allows CSV export of analyzed results

---

## 🎯 Future Improvements

- 🔹 Add more news sources
- 🔹 Add sentiment analysis
- 🔹 Add word cloud visualization
- 🔹 Deploy online using Streamlit Cloud
- 🔹 Add real-time trend analysis
- 🔹 Improve automatic topic naming

---

## 👨‍💻 Author

### Anurag Jha

GitHub: https://github.com/Anurag0018

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
