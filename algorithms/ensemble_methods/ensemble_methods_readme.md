# Ensemble Methods

**What it is:**

Ensemble methods combine multiple models (often called base models) to improve overall predictive performance. The core idea is “the wisdom of the crowd.”

**Why it’s needed:**
    - A single model may overfit or underfit; ensemble methods reduce bias and variance by leveraging the strengths of multiple models.
    - They enhance robustness and generalization.

**Common methods:**
1.	Bagging (Bootstrap Aggregating):
- Idea: Train multiple independent models on different random subsets of the data, then combine predictions via averaging or voting.
- Representative methods:
    - Random Forest: A Bagging method using decision trees as base models.
    - Extra Trees: Similar to Random Forest but adds more randomness in selecting split points.
2.	Boosting:
- Idea: Train models sequentially, with each focusing on the errors of the previous model. Combine predictions using a weighted approach.
- Representative methods:
    - Gradient Boosted Decision Trees (GBDT)
    - XGBoost
    - LightGBM
    - CatBoost
3.	Stacking:
- Idea: Train multiple diverse base models, use their outputs as new features, and train a meta-model (often linear regression or logistic regression) for final predictions.
4.	Voting:
- Idea: Combine predictions using simple voting or weighted voting (for classification) or averaging (for regression).