# Logistic Regression with Python

## Objectives

After completing this lab you will be able to:

* Use scikit-learn's Logistic Regression to classify data
* Understand how to evaluate a model using a confusion matrix

In this notebook, you will learn Logistic Regression, and then create a model for a telecommunication company to predict when its customers will leave for a competitor, so they can take some action to retain the customers.

## Table of Contents

1. [About the dataset](#about_dataset)
2. [Data Pre-processing and Selection](#preprocessing)
3. [Modeling (Logistic Regression with Scikit-learn)](#modeling)
4. [Evaluation](#evaluation)
5. [Practice](#practice)

---

## What is the Difference Between Linear and Logistic Regression?

While **Linear Regression** is suited for estimating continuous values (e.g., estimating house prices), it is not the best tool for predicting the class of an observed data point. To predict the class of a data point, we need guidance on the most probable class for that data point. For this, we use **Logistic Regression**.

### Recall Linear Regression:

Linear Regression finds a function that relates a continuous dependent variable, `y`, to some predictors (independent variables `x1`, `x2`, etc.). For example, simple linear regression assumes a function of the form:

$$
y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots
$$

Logistic Regression is a variation of Linear Regression, used when the observed dependent variable `y` is categorical. It predicts the probability of a class label as a function of the independent variables. The output is transformed into a probability using the **sigmoid function**.

$$
h_\theta(x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots)}}
$$

This function provides a predicted probability between 0 and 1, helping us classify the data points.

---

## Customer Churn with Logistic Regression

A telecommunications company is concerned about the number of customers leaving for cable competitors. They need to understand who is leaving. Imagine that you are an analyst at this company and you have to identify who is leaving and why.

### Install Required Libraries

```bash
!pip install scikit-learn
!pip install matplotlib
!pip install pandas
!pip install numpy