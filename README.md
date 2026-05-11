
 📰 News Topic Discovery & Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

An intelligent dashboard that scrapes live news via RSS feeds and applies **Unsupervised Machine Learning** to categorize headlines into thematic clusters. 

[Explore the Code](#-project-structure) • [Installation](#-installation) • [How it Works](#-the-nlp-pipeline)




## 🚀 Features

*   **Real-Time Data:** Fetches live articles from **BBC** and **The Hindu** using `feedparser`.
*   **Smart Preprocessing:** Automated text cleaning (lowercase, regex noise removal, and stop-word filtering).
*   **ML-Driven Clustering:** Uses **TF-IDF Vectorization** and **K-Means** to group similar stories without manual labels.
*   **Dynamic UI:** Adjust the number of topics via a sidebar slider in real-time.
*   **Visual Insights:** Built-in **Matplotlib** charts to visualize topic frequency.
*   **Data Portability:** Export your clustered news data as a CSV directly from the browser.


## 📖 The NLP Pipeline

To turn raw headlines into organized topics, the app follows these steps:

1.  **Text Preprocessing:** Headlines are stripped of special characters and common "stop words" (like *the, is, and*) that don't carry topical meaning.
2.  **TF-IDF Vectorization:** Words are converted into numerical vectors. 
    *   *Term Frequency:* How often a word appears.
    *   *Inverse Document Frequency:* Down-weights words that appear too often across all articles (like "news").
3.  **K-Means Clustering:** The algorithm calculates the "centroid" of article vectors to find $k$ distinct groups.
4.  **Top Keyword Extraction:** The app identifies the words closest to each cluster center to describe the topic.


## 🛠️ Technologies Used

| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.x |
| **Frontend** | Streamlit |
| **ML/NLP** | Scikit-Learn, NLTK (Stopwords) |
| **Data** | Pandas, NumPy |
| **Parsing** | Feedparser, Requests |
| **Viz** | Matplotlib |


## 📂 Project Structure



News-Topic-Discovery-and-Analysis/
├── app.py              # Main Streamlit application logic
├── requirements.txt    # Python dependencies
└── README.md           # Documentation




## ⚙️ Installation

### 1. Clone & Enter

git clone [https://github.com/Anurag0018/News-Topic-Discovery-and-Analysis.git](https://github.com/Anurag0018/News-Topic-Discovery-and-Analysis.git)
cd News-Topic-Discovery-and-Analysis


### 2. Setup Environment

bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


### 3. Launch
streamlit run app.py




