from textblob import TextBlob
import re
from collections import defaultdict


# -------------------------------
# STEP 1: CLEAN TEXT
# -------------------------------

def preprocess_text(text):

    text = re.sub(r'[^a-zA-Z0-9., ]', ' ', text)

    sentences = text.split(".")

    clean_sentences = []

    for s in sentences:
        s = s.strip()

        if (
            len(s.split()) > 6 and
            not any(x in s.lower() for x in [
                "login", "cart", "search", "menu",
                "flipkart", "seller", "home",
                "rating", "verified buyer"
            ])
        ):
            clean_sentences.append(s)

    return clean_sentences


# -------------------------------
# STEP 2: SENTIMENT CLASSIFICATION
# -------------------------------

def classify_sentences(sentences):

    positive = []
    negative = []
    polarity_total = 0

    for s in sentences:
        polarity = TextBlob(s).sentiment.polarity
        polarity_total += polarity

        if polarity > 0.05:
            positive.append(s)

        elif polarity < -0.05:
            negative.append(s)

    return positive, negative, polarity_total


# -------------------------------
# STEP 3: CLUSTERING
# -------------------------------

def cluster_sentences(sentences):

    clusters = defaultdict(list)

    for s in sentences:
        words = s.lower().split()

        # Take first meaningful words as cluster key
        key = " ".join(words[:3])

        clusters[key].append(s)

    return clusters


# -------------------------------
# STEP 4: INSIGHT GENERATION
# -------------------------------

def generate_insights(clusters):

    insights = []

    for key, group in clusters.items():

        combined = " ".join(group)

        blob = TextBlob(combined)

        # Choose most informative sentence
        best_sentence = max(blob.sentences, key=lambda x: len(x))

        insight = str(best_sentence).strip()

        insights.append(insight)

    # Remove duplicates
    unique = list(dict.fromkeys(insights))

    return unique[:5]


# def refine_insights(insights):

#     refined = []

#     for text in insights:

#         # -------------------------
#         # STEP 1: CLEAN TEXT
#         # -------------------------
#         text = re.sub(r'[^a-zA-Z0-9., ]', ' ', text)
#         text = text.strip()

#         # -------------------------
#         # STEP 2: REMOVE PERSONAL WORDS
#         # -------------------------
#         text = re.sub(r"\b(i|me|my|mine|we|our|us)\b", "", text, flags=re.IGNORECASE)

#         # -------------------------
#         # STEP 3: GRAMMAR CORRECTION
#         # -------------------------
#         blob = TextBlob(text)
#         text = str(blob.correct())

#         # -------------------------
#         # STEP 4: REFRAME TO INSIGHT
#         # -------------------------
#         words = text.split()

#         if len(words) < 5:
#             continue

#         # Create generalized sentence
#         text = " ".join(words[:15])

#         # Convert to neutral insight tone
#         text = text.capitalize()

#         if not text.endswith("."):
#             text += "."

#         refined.append(text)

def refine_insights(insights):

    refined = []

    for text in insights:

        # -------------------------
        # STEP 1: CLEAN TEXT
        # -------------------------
        text = re.sub(r'[^a-zA-Z0-9., ]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text.split()) < 6:
            continue

        # -------------------------
        # STEP 2: REMOVE PERSONAL WORDS
        # -------------------------
        text = re.sub(r"\b(i|me|my|we|our|us)\b", "", text, flags=re.IGNORECASE)

        # -------------------------
        # STEP 3: GRAMMAR NORMALIZATION
        # -------------------------
        blob = TextBlob(text)
        text = str(blob.correct())

        # -------------------------
        # STEP 4: EXTRACT CORE MEANING
        # -------------------------
        words = text.split()

        # Keep meaningful part (middle of sentence often better)
        if len(words) > 12:
            core = words[2:14]
        else:
            core = words

        sentence = " ".join(core)

        # -------------------------
        # STEP 5: MAKE IT GENERIC (REMOVE SUBJECT BIAS)
        # -------------------------
        sentence = re.sub(r"\b(this|that|it|device|product)\b", "the product", sentence, flags=re.IGNORECASE)

        # -------------------------
        # STEP 6: FINAL FORMATTING
        # -------------------------
        sentence = sentence.capitalize()

        if not sentence.endswith("."):
            sentence += "."

        refined.append(sentence)

    # -------------------------
    # STEP 7: REMOVE DUPLICATES
    # -------------------------
    refined = list(dict.fromkeys(refined))

    return refined[:5]

    # -------------------------
    # REMOVE DUPLICATES
    # -------------------------
    refined = list(dict.fromkeys(refined))

    return refined[:5]

    # -------------------------
    # STEP 5: REMOVE DUPLICATES
    # -------------------------
    refined = list(dict.fromkeys(refined))

    return refined[:5]# -------------------------------
# MAIN FUNCTION
# -------------------------------

def analyze_sentiment(text):

    if not text:
        return {
            "label": "UNKNOWN",
            "score": 0,
            "positive_dimensions": [],
            "negative_dimensions": []
        }

    sentences = preprocess_text(text)

    positive, negative, polarity_total = classify_sentences(sentences)

    avg = polarity_total / len(sentences) if sentences else 0

    label = "POSITIVE" if avg > 0 else "NEGATIVE" if avg < 0 else "NEUTRAL"

    # Build insights
    pos_clusters = cluster_sentences(positive)
    neg_clusters = cluster_sentences(negative)

    pos_dims = refine_insights(generate_insights(pos_clusters))
    neg_dims = refine_insights(generate_insights(neg_clusters))

    # Fallback
    if not pos_dims:
        pos_dims = ["General positive sentiment observed but without strong repeated patterns."]

    if not neg_dims:
        weaker_neg = [s for s in sentences if TextBlob(s).sentiment.polarity < 0]

        neg_clusters = cluster_sentences(weaker_neg)
        neg_dims = refine_insights(generate_insights(neg_clusters))

    return {
        "label": label,
        "score": round(abs(avg), 3),
        "positive_dimensions": pos_dims,
        "negative_dimensions": neg_dims
    }