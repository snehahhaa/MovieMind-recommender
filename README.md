# MovieMind – A Simple Movie Recommendation App

**MovieMind** is a content-based movie recommender system built using Streamlit.  
It helps users discover movies similar to the ones they like, based on their content and features.

---

## 🔍 How It Works

- Uses **cosine similarity** to compare feature vectors of movies.  
- Based on the selected movie, it finds the top 5–6 most similar titles.  
- Movie data is preprocessed and stored in `.pkl` files for fast access.  
- Posters are fetched in real-time using the **TMDb API** to enhance user experience.

---

## 🛠️ Technologies Used

- Python  
- Streamlit – for building the web interface  
- Pandas & Scikit-learn – for data handling and similarity calculations  
- Pickle – for saving preprocessed data  
- TMDb API – for retrieving movie posters  

---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/snehahhaa/MovieMind-recommender.git
   ```

2. **Navigate into the folder**
   ```bash
   cd MovieMind-recommender
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```
5.  Live Demo  
👉 [Check out the app here](https://moviemind-recommender.streamlit.app/)

   
