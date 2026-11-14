
import streamlit as st
import joblib
import re
import os

from pathlib import Path
from text_utils import clean_text


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Fashion Review Analytics",
    page_icon="👗",
    layout="wide"
)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "recommend_pipeline.pkl"


@st.cache_resource
def load_model():

    model = joblib.load(MODEL_PATH)

    return model


model = load_model()


# ==========================================
# APPLICATION HEADER
# ==========================================

st.title("👗 Fashion Review Analytics")

st.write(
    "Analyze customer fashion reviews using "
    "Natural Language Processing and Machine Learning."
)

st.divider()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📌 About This Project")

st.sidebar.write(
    """
    This application predicts whether a customer
    would recommend a fashion product based on
    their written review.

    **Technologies:**
    - Python
    - NLP
    - TF-IDF
    - Logistic Regression
    - Streamlit
    """
)

st.sidebar.subheader("📝 Example Reviews")

st.sidebar.markdown(
    """
    **Example 1 – Positive**

    I absolutely love this dress. The quality
    is excellent and it fits perfectly.

    ---

    **Example 2 – Negative**

    The fabric quality is poor and the dress
    is uncomfortable.

    ---

    **Example 3 – Mixed**

    The design is beautiful but the material
    is not worth the price.
    """
)


# ==========================================
# USER INPUT
# ==========================================

st.subheader("Enter Customer Review")

title_input = st.text_input(
    "Product Title",
    placeholder="Example: Beautiful Summer Dress"
)

review_text = st.text_area(
    "Customer Review",
    placeholder="Write your fashion product review here...",
    height=150
)


# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button("🔍 Analyze Review", use_container_width=True):

    if not review_text.strip():

        st.warning("Please enter a review.")

    else:

        # Combine title and review
        full_text = str(title_input) + " " + str(review_text)

        # Clean input text
        cleaned_review = clean_text(full_text)

        # Convert into list for prediction
        input_data = [cleaned_review]

        # Predict class
        prediction = model.predict(input_data)[0]

        # Get probabilities
        probabilities = model.predict_proba(input_data)[0]

        # Identify class indexes
        classes = list(model.classes_)

        recommend_index = classes.index(1)
        not_recommend_index = classes.index(0)

        recommend_probability = probabilities[recommend_index]
        not_recommend_probability = probabilities[not_recommend_index]


        # ==================================
        # PREDICTION RESULT
        # ==================================

        st.divider()

        st.subheader("📊 Prediction Result")

        if prediction == 1:

            st.success("Customer would recommend")

        else:

            st.error("Customer would NOT recommend")


        # ==================================
        # PROBABILITY
        # ==================================

        st.subheader("Recommendation Probability")

        percentage = recommend_probability * 100

        st.metric(
            label="Probability of Recommendation",
            value=f"{percentage:.2f}%"
        )

        st.progress(float(recommend_probability))


        # ==================================
        # QUALITY WARNING
        # ==================================

        if not_recommend_probability > 0.5:

            st.warning(
                "⚠️ Send to quality team: "
                "The customer may not recommend this product."
            )


        # ==================================
        # REVIEW STATISTICS
        # ==================================

        st.divider()

        st.subheader("📝 Review Statistics")

        word_count = len(
            re.findall(r"\b\w+\b", review_text)
        )

        exclamation_count = review_text.count("!")

        capital_words = re.findall(
            r"\b[A-Z]{2,}\b",
            review_text
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Word Count", word_count)

        col2.metric(
            "Exclamation Marks",
            exclamation_count
        )

        col3.metric(
            "ALL-CAPS Words",
            len(capital_words)
        )


        # ==================================
        # PROBABILITY DETAILS
        # ==================================

        st.divider()

        st.subheader("Prediction Confidence")

        col1, col2 = st.columns(2)

        col1.metric(
            "Recommend",
            f"{recommend_probability * 100:.2f}%"
        )

        col2.metric(
            "Not Recommend",
            f"{not_recommend_probability * 100:.2f}%"
        )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "NLP Practical Exam – Set C | "
    "Fashion Review Analytics"
)
