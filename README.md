# Frameworks_Assignment

## 📊 CORD-19 Research Paper Analysis App

This is a beginner-friendly data analysis and visualization project built with **Python**, **Pandas**, and **Streamlit**. It analyzes the **CORD-19 metadata dataset**, which contains information about research papers related to COVID-19.

The app loads the dataset, cleans the data, and provides interactive visualizations such as:
- Publications per year/month
- Top publishing journals and sources
- A word cloud of frequent words in paper titles

---

### 🚀 Features

✅ Count and visualize papers by **publication year**  
✅ Identify **top journals** and **sources** publishing COVID-19 papers  
✅ Generate a **word cloud** of the most frequent words in paper titles  
✅ Interactive filters using **Streamlit sidebar**  
✅ Raw data preview for exploration  

---

### 📦 Dataset Used

We use the **metadata.csv** file from the [CORD-19 Research Challenge Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) on Kaggle, which includes:

- Paper titles and abstracts  
- Authors and publication dates  
- Journals and sources  

> **Note**: Make sure to download the `metadata.csv` file.

---

### 🛠️ Installation Instructions

Follow the steps below to set up and run the project locally.

#### 🔹 1. Clone the Repository

```bash
git clone https://github.com/Happy-Grace/Frameworks_Assignment
cd Frameworks_Assignment
```

#### 🔹 2. Install Required Dependencies

Install all required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install:

* `streamlit`
* `pandas`
* `matplotlib`
* `seaborn`
* `nltk`
* `wordcloud`
* `numpy`

---

### 🧠 NLTK Download (Stopwords)

One-time setup: Inside the app, the following is included to ensure stopwords are downloaded for text cleaning:

```python
import nltk
nltk.download('stopwords')
```

This happens automatically when you run the app for the first time.

---

### ▶️ How to Run the App

After installing the dependencies, run the Streamlit app with:

```bash
streamlit run app.py
```

This will open the app in your default web browser at:

```
http://localhost:8501
```

---

### 🗂️ Project Structure

```
Frameworks_Assignment/
│
├── data/
│   └── metadata.csv              # Dataset file
│
├── app.py                        # Main Streamlit app
├── requirements.txt              # All required Python packages
└── README.md                     # Project overview and setup guide
> **Note**: After cloning te repository, create a directory/folder named `data` and save the downloaded `metadata.csv` file in it.
 
```

---

### 👨‍💻 Author

- Personal Project by: 
**C. DIVINEGIFT AKUWUDIKE**
[Happy-Grace](https://github.com/Happy-Grace/Frameworks_Assignment)
- Feel free to fork or contribute to improve this project!

---


