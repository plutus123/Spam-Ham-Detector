# Spam-Ham-Detector
# Overview

This repository contains code for a Spam Ham Detector. The detector is built using a combination of regular expressions (re), lemmatization, TF-IDF (Term Frequency-Inverse Document Frequency), and an XGBoost classifier. This system is designed to classify messages into two categories: spam and ham (non-spam).

# Implementation Details

The detector is implemented using the following components:

Regular Expressions (re): Used for text preprocessing and feature extraction.

Lemmatization: A technique for reducing words to their base or root form.

TF-IDF Vectorization: Transforms text data into numerical format, representing the importance of each word in a document relative to a collection of documents.

XGBoost Classifier: A popular gradient boosting algorithm used for classification tasks.

# Results

The detector achieved an accuracy of 0.9617224880382775% on the test set, demonstrating its effectiveness in classifying spam and ham messages.

# Contributing

If you'd like to contribute to this project, please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Make your changes and commit them (git commit -m 'Add feature')

Push the branch (git push origin feature/your-feature)

Create a pull request
