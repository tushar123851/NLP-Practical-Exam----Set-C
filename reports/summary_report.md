# NLP Practical Exam – Set C

## Final Project Summary Report

**Project:** Women's Clothing Review Recommendation Analysis  
**Author:** Tushar Vala  
**Domain:** Natural Language Processing (NLP) and Machine Learning

---

## 1. Business Problem and Dataset

Online customer reviews contain useful information about product quality and customer satisfaction. This project uses Natural Language Processing (NLP) to analyse women's clothing reviews and predict whether a customer recommends a product.

The dataset contains **22,641 records and 9 columns**. It was divided into **18,112 training records** and **4,529 testing records**. The not-recommended rate is **18.11%**, indicating that the target classes are imbalanced.

Therefore, accuracy alone is not sufficient to evaluate model performance. Class 0 precision, recall, F1-score, and ROC-AUC are also considered.

## 2. Text Preprocessing and Feature Extraction

The project workflow includes preparing review text for analysis and converting text into numerical features that machine-learning models can process.

The feature-extraction approaches evaluated were:

- Bag of Words (BoW)
- TF-IDF
- TF-IDF with unigrams and bigrams
- Word2Vec Skip-gram

The trained Word2Vec Skip-gram model contains **3,910 vocabulary words** and uses **100-dimensional word vectors**.

The TF-IDF vocabulary size should be confirmed from the fitted vectorizer before reporting it. The notebook summary displayed 16, which may need verification.

## 3. Classification and Model Evaluation

Four Logistic Regression approaches were compared with an always-recommends baseline.

The baseline achieved **81.89% accuracy**, but its Class 0 precision, recall, and F1-score were all **0.00**. This demonstrates why a high accuracy score can be misleading when the classes are imbalanced.

### Model comparison

| Model | Accuracy | Class 0 Precision | Class 0 Recall | Class 0 F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline – Always Recommends | 0.8189 | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| Word2Vec Skip-gram + Logistic Regression | 0.8651 | 0.5837 | **0.8890** | 0.7047 | 0.9413 |
| **TF-IDF Unigrams + Bigrams + Logistic Regression** | **0.8881** | 0.6381 | 0.8817 | **0.7404** | **0.9463** |
| TF-IDF + Logistic Regression | 0.8794 | 0.6185 | 0.8720 | 0.7237 | 0.9441 |
| Bag of Words + Logistic Regression | 0.8834 | 0.6446 | 0.7939 | 0.7115 | 0.9257 |

### Key findings

- **Best overall accuracy:** TF-IDF Unigrams + Bigrams + Logistic Regression – 88.81%.
- **Best ROC-AUC:** TF-IDF Unigrams + Bigrams + Logistic Regression – 0.9463.
- **Best Class 0 recall:** Word2Vec Skip-gram + Logistic Regression – 0.8890 (88.90%).
- **Baseline limitation:** The always-recommends baseline achieved 81.89% accuracy but 0% Class 0 recall.

The TF-IDF unigram-and-bigram model achieved the strongest overall results in accuracy, Class 0 F1-score, and ROC-AUC. Word2Vec achieved slightly higher Class 0 recall.

The preferred model therefore depends on the evaluation priority.

## 4. Heuristic Analysis and POS Tagging

A warning-word heuristic was evaluated using different minimum warning-match thresholds.

### Heuristic comparison

| Minimum Warning Matches | Accuracy | Class 0 Recall | Class 0 F1 |
|---:|---:|---:|---:|
| 1 | 0.8160 | 0.3077 | 0.3784 |
| 2 | 0.8240 | 0.0714 | 0.1287 |

A threshold of one warning match detected more Class 0 reviews than a threshold of two.

Although the two-match rule had slightly higher accuracy, its Class 0 recall was much lower.

POS tagging was also performed on review text to identify grammatical categories of words. The available results confirm token-level POS tagging. A separate quantitative complaint-phrase extraction result has not been included here.

### VADER analysis

A VADER comparison should be added after checking its actual notebook output. No VADER metric is reported here because a verified result was not available in the collected project summary.

## 5. Application and Deployment

The project includes a trained classification pipeline integrated into a Streamlit application.

The application provides:

- Product title input.
- Customer review text input.
- Example positive, negative, and mixed reviews.
- Analyze Review functionality.
- Customer recommendation prediction.
- Recommendation probability.
- Prediction confidence.
- Review statistics, including word count, exclamation marks, and ALL-CAPS words.

The application screenshot demonstrates a sample prediction:

| Application Output | Example Value |
|---|---:|
| Prediction | Customer would recommend |
| Recommendation probability | 87.55% |
| Not-recommend probability | 12.45% |
| Review word count | 18 |
| Exclamation marks | 0 |
| ALL-CAPS words | 0 |

These values represent the example shown in the application screenshot. Predictions and probabilities may differ for other reviews.

The application should be tested locally before submission. This report does not claim that the application has been publicly deployed.

## 6. Challenges and Future Improvements

The main challenges encountered during this project include:

- Cleaning unstructured customer review text.
- Handling imbalanced target classes.
- Selecting suitable text feature-extraction techniques.
- Comparing multiple machine-learning models.
- Evaluating performance beyond accuracy.
- Identifying useful warning words in customer feedback.

### Future improvements

- Improve handling of Hinglish and multilingual customer reviews.
- Experiment with transformer-based NLP models.
- Improve complaint-phrase extraction.
- Tune classification thresholds.
- Add additional review-level analytics and visualisations.
- Test the model on additional customer review datasets.
- Improve the Streamlit interface and deployment process.

## 7. Conclusion

This project demonstrates an end-to-end NLP workflow for customer-review recommendation analysis, including text preprocessing, feature extraction, Word2Vec, Logistic Regression classification, heuristic analysis, POS tagging, and Streamlit application development.

The TF-IDF unigram-and-bigram model produced the strongest overall evaluation results, achieving **88.81% accuracy** and **0.9463 ROC-AUC**.

The Word2Vec Skip-gram model achieved the highest Class 0 recall among the compared classifiers, at **88.90%**.

The baseline comparison highlights the importance of evaluating minority-class performance rather than relying on accuracy alone.

Overall, this project demonstrates how NLP and machine learning can be used to analyse customer feedback and predict product recommendation behaviour.

---

**Project Author:** Tushar Vala  
**Project:** NLP Practical Exam – Set C  
**Application:** Fashion Review Analytics  
**Technologies:** Python | NLP | Machine Learning | Scikit-learn | Word2Vec | Streamlit
