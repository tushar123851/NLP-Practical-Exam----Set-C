# NLP Practical Exam -- Set C

## Final Project Summary Report

**Project:** Women's Clothing Review Recommendation Analysis\
**Author:** Tushar Vala\
**Domain:** Natural Language Processing (NLP) and Machine Learning

------------------------------------------------------------------------

## 1. Business Problem and Dataset

Online customer reviews contain useful information about product quality
and customer satisfaction. This project uses Natural Language Processing
(NLP) to analyse women's clothing reviews and predict whether a customer
recommends a product.

The dataset contains **22,641 records and 9 columns**. It was divided
into **18,112 training records** and **4,529 testing records**. The
not-recommended rate is **18.11%**, indicating that the target classes
are imbalanced. Therefore, accuracy alone is not sufficient to evaluate
model performance; Class 0 precision, recall, F1-score, and ROC-AUC are
also considered.

## 2. Text Preprocessing and Feature Extraction

The project workflow includes preparing review text for analysis and
converting text into numerical features that machine-learning models can
process.

The feature-extraction approaches evaluated were:

-   Bag of Words (BoW)
-   TF-IDF
-   TF-IDF with unigrams and bigrams
-   Word2Vec Skip-gram

The trained Word2Vec Skip-gram model contains **3,910 vocabulary words**
and uses **100-dimensional word vectors**. The TF-IDF vocabulary size
should be confirmed from the fitted vectorizer before reporting it: the
notebook summary displayed 16, which may need verification.

## 3. Classification and Model Evaluation

Four Logistic Regression approaches were compared with an
always-recommends baseline. The baseline achieved **81.89% accuracy**,
but its Class 0 precision, recall, and F1-score were all **0.00**. This
demonstrates why a high accuracy score can be misleading when the
classes are imbalanced.

  ------------------------------------------------------------------------------
  Model             Accuracy      Class 0      Class 0   Class 0 F1      ROC-AUC
                                Precision       Recall              
  ------------- ------------ ------------ ------------ ------------ ------------
  Baseline --         0.8189       0.0000       0.0000       0.0000       0.5000
  Always                                                            
  Recommends                                                        

  Word2Vec            0.8651       0.5837       0.8890       0.7047       0.9413
  Skip-gram +                                                       
  Logistic                                                          
  Regression                                                        

  TF-IDF          **0.8881**       0.6381       0.8817   **0.7404**   **0.9463**
  Unigrams +                                                        
  Bigrams +                                                         
  Logistic                                                          
  Regression                                                        

  TF-IDF +            0.8794       0.6185       0.8720       0.7237       0.9441
  Logistic                                                          
  Regression                                                        

  Bag of              0.8834       0.6446       0.7939       0.7115       0.9257
  Words +                                                           
  Logistic                                                          
  Regression                                                        
  ------------------------------------------------------------------------------

The **TF-IDF Unigrams + Bigrams + Logistic Regression** model achieved
the best overall accuracy (**88.81%**), Class 0 F1-score (**0.7404**),
and ROC-AUC (**0.9463**). The Word2Vec Skip-gram model achieved the
highest Class 0 recall (**0.8890**, approximately **88.90%**). The
preferred model therefore depends on the evaluation priority: overall
ranking and balance favour TF-IDF unigrams and bigrams, while Word2Vec
has a small advantage in Class 0 recall.

## 4. Heuristic Analysis and POS Tagging

A warning-word heuristic was evaluated using different minimum
warning-match thresholds.

    Minimum Warning Matches   Accuracy   Class 0 Recall   Class 0 F1
  ------------------------- ---------- ---------------- ------------
                          1     0.8160           0.3077       0.3784
                          2     0.8240           0.0714       0.1287

A threshold of one warning match detected more Class 0 reviews than a
threshold of two. Although the two-match rule had slightly higher
accuracy, its Class 0 recall was much lower. POS tagging was also
performed on review text to identify grammatical categories of words.
The available results confirm token-level POS tagging; a separate
quantitative complaint-phrase extraction result has not been included
here.

A VADER comparison should be added after its actual notebook output has
been checked. No VADER metric is stated in this report because a
verified result was not available in the collected project summary.

## 5. Application and Deployment

The project includes a trained classification pipeline intended for use
in a Streamlit application. The application can accept a customer review
and display a recommendation prediction. Before submission, verify the
app locally and update this section with the actual test result,
screenshots, and any deployment URL. Do not describe the application as
deployed unless it has genuinely been deployed.

## 6. Challenges and Future Improvements

The main challenges include cleaning unstructured review text, handling
class imbalance, selecting useful text representations, and evaluating
models beyond accuracy. Future improvements include better handling of
Hinglish and multilingual reviews, more systematic complaint-phrase
extraction, threshold tuning, transformer-based models, and testing on
additional review datasets.

## 7. Conclusion

This project demonstrates an end-to-end NLP workflow for customer-review
recommendation analysis, including preprocessing, feature extraction,
Word2Vec, Logistic Regression classification, heuristic analysis, and
POS tagging. The TF-IDF unigram-and-bigram model produced the strongest
overall evaluation results, while Word2Vec achieved the highest Class 0
recall among the compared classifiers. The baseline comparison
highlights the importance of evaluating minority-class performance
rather than relying on accuracy alone.
