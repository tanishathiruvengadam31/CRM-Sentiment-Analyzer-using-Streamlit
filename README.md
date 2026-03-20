# 📊 CRM Sentiment Link Analyzer

A **Customer Relationship Management (CRM) Sentiment Analysis Dashboard** that analyzes public opinion from any website link.
The system extracts textual content from a given URL and performs **sentiment analysis** to understand whether the public opinion expressed is **Positive, Negative, or Neutral**.

This project demonstrates how **Natural Language Processing (NLP)** can be integrated with **CRM analytics dashboards** to monitor customer feedback from web sources.

---

# 🚀 Project Overview

Organizations today receive large volumes of feedback from multiple online sources such as:

* Product reviews
* Blog posts
* News articles
* Social media discussions
* Customer forums

Manually analyzing this information is difficult and time-consuming.

This project provides an **automated solution** that:

1. Extracts textual content from a website.
2. Processes the text using **sentiment analysis techniques**.
3. Displays results through an **interactive CRM-style dashboard**.

The system helps businesses quickly understand **public opinion and customer sentiment** regarding their products or services.

---

# 🎯 Key Features

✔ Analyze sentiment from **any public website link**
✔ Automatic **text extraction from webpages**
✔ **Sentiment classification** (Positive / Negative / Neutral)
✔ **CRM analytics dashboard with KPIs**
✔ **Sentiment distribution visualization**
✔ **History tracking of analyzed links**
✔ **Interactive web interface using Streamlit**
✔ **Free cloud deployment**

---

# 🧠 How It Works

The system follows the workflow below:

```
User Input (Website URL)
        │
        ▼
Web Scraper (BeautifulSoup)
        │
        ▼
Text Extraction
        │
        ▼
Sentiment Analysis (TextBlob NLP)
        │
        ▼
CRM Dashboard Visualization
        │
        ▼
History Storage (JSON)
```

---

# 🧩 System Architecture

The project is divided into multiple modules for better maintainability.

```
CRM Sentiment Analyzer
│
├── streamlit_app.py      # Main Streamlit dashboard
├── scraper.py            # Web scraping module
├── sentiment.py          # Sentiment analysis logic
├── history.json          # Stores previous analyses
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Ignore unnecessary files
```

---

# 📊 Dashboard Modules

The application contains **three main dashboard tabs**.

## 1️⃣ Overview Dashboard

Displays high-level CRM insights including:

* Total links analyzed
* Positive sentiment count
* Negative sentiment count
* Sentiment distribution chart
* Recent analysis results

This helps understand **overall public opinion trends**.

---

## 2️⃣ Analyzer

This module allows users to:

1. Enter a website link
2. Extract webpage content
3. Perform sentiment analysis

The system outputs:

* Sentiment classification
* Confidence score
* Stored result in analysis history

---

## 3️⃣ History

The history module keeps track of all previous analyses.

Stored information includes:

* URL analyzed
* Sentiment result
* Confidence score
* Timestamp of analysis

This helps simulate a **CRM customer feedback database**.

---

# 🛠️ Technologies Used

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| Python        | Core programming language   |
| Streamlit     | Interactive web dashboard   |
| BeautifulSoup | Web scraping                |
| Requests      | Fetch webpage data          |
| TextBlob      | Natural language processing |
| Pandas        | Data processing             |
| Plotly        | Data visualization          |

---

# ⚙️ Installation Guide

Follow the steps below to run the project locally.

## Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/crm-sentiment-analyzer.git
cd crm-sentiment-analyzer
```

---

## Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 — Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

---

## Step 4 — Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# ☁️ Deployment (Free Hosting)

This project can be deployed easily using **Streamlit Cloud**.

### Steps

1. Push the project to GitHub
2. Visit

https://streamlit.io/cloud

3. Connect your GitHub repository
4. Select:

```
streamlit_app.py
```

5. Click **Deploy**

Your application will be hosted online.

---

# 📈 Example Output

Input URL:

```
https://example-news-article.com
```

Output:

```
Sentiment: Positive
Confidence Score: 0.42
```

Dashboard updates automatically with new analysis results.

---

# 📚 Applications

This system can be used in multiple real-world scenarios:

* Customer feedback monitoring
* Brand reputation analysis
* Product review analysis
* Public opinion tracking
* CRM customer insight generation
* Market research

---

# 🔮 Future Enhancements

Possible improvements for the system include:

* AI-based sentiment models (BERT)
* Emotion detection
* Topic modeling
* Word cloud visualization
* Social media integration (Twitter / Reddit)
* Multilingual sentiment analysis
* Real-time streaming data analysis

---

# 🎓 Academic Use

This project is suitable for:

* Smart India Hackathon (SIH)
* Data Science projects
* NLP coursework
* CRM analytics demonstrations
* Machine learning student portfolios

---

# 👩‍💻 Author

**Preethi L**

M.Tech Data Science Engineering
BITS Pilani

---

# ⭐ License

This project is open source and available for educational use.
