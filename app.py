# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud

# Download stopwords (only once)
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/metadata.csv', low_memory=False)

    # A copy of the DataFrame
    df_clean = df.copy()

    df_clean = df_clean.dropna(subset=['title', 'abstract'])
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    df_clean['year'] = df_clean['publish_time'].dt.year
    return df_clean

df_clean = load_data()

# Set Streamlit page
st.set_page_config(page_title="CORD-19 Analysis", layout="wide")

st.title("📊 COVID-19 Research Papers – CORD-19 Dataset Explorer")


# Sidebar year filter and copy for safety
df_2000s = df_clean[df_clean['year'] >= 2000]

# Drops the Publications with 'Unknown' or Missing Titles
st.markdown(f"Filtered by Publication Year (from [2000s]) except Publications with 'Unknown' or Missing Titles.\n")
selected_year = st.sidebar.selectbox("Filter by Publication Year (from [2000s])", sorted(df_2000s['year'].dropna().unique()))
filtered_df = df_2000s[df_2000s['year'] == selected_year].copy()


st.markdown(f"### Number of papers published in {selected_year}: {len(filtered_df)}")

# --- Plot 1: Publications over Time ---
df_2000s = df_clean[df_clean['year'] >= 2000]

st.subheader("Publications Over Time")
pubs_per_year = df_2000s['year'].value_counts().sort_index()

fig1, ax1 = plt.subplots()
sns.lineplot(x=pubs_per_year.index, y=pubs_per_year.values, marker="o", ax=ax1)
ax1.set_title("Number of Publications per Year [from 2000s]")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# --- Plot 2: Top Journals ---
st.subheader("Top Journals Publishing COVID-19 Research")
top_journals = df_clean['journal'].value_counts().head(20)

fig2, ax2 = plt.subplots()
top_journals.sort_values().plot(kind='barh', ax=ax2, color='skyblue')
ax2.set_title("Top 20 Journals")
ax2.set_xlabel("Number of Papers")
st.pyplot(fig2)

# --- Plot 3: Word Cloud from Titles ---
st.subheader("Most Frequent Words in Paper Titles")

# Clean and process titles
all_titles = ' '.join(df_clean['title'].str.lower())
cleaned_titles = re.sub(r'[^a-z\s]', '', all_titles)
all_words = cleaned_titles.split()
filtered_words = [word for word in all_words if word not in stop_words and len(word) > 2]

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))

fig3, ax3 = plt.subplots(figsize=(15, 7))
ax3.imshow(wordcloud, interpolation='bicubic')
ax3.axis('off')
st.pyplot(fig3)

# --- Plot 4: Top Sources ---
st.subheader("Top Sources of Papers")

top_sources = df_clean['source_x'].value_counts().head(10)

fig4, ax4 = plt.subplots()
top_sources.sort_values().plot(kind='barh', ax=ax4, color='purple')
ax4.set_title("Top 10 Sources")
ax4.set_xlabel("Number of Papers")
st.pyplot(fig4)

# --- Raw Data Preview ---
with st.expander("Show 30 rows of raw data"):
    st.dataframe(df_clean[['title', 'authors', 'journal', 'publish_time']].head(30))
