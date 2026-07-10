# 📰 NewsLens AI

> A hybrid news recommendation system inspired by modern newsroom recommendation platforms.

## Overview

NewsLens AI combines Natural Language Processing (NLP), recommendation algorithms, and editorial analytics to personalize news recommendations while providing insights into reader engagement and content performance.

This project is inspired by the challenges faced by audience data science teams at large digital news organizations.

## Features

- Personalized article recommendations
- Content-based recommendations using NLP embeddings
- Collaborative filtering
- Hybrid recommendation engine
- Editorial ranking controls
- Recommendation evaluation (Precision@K, Recall@K, MAP, NDCG)
- A/B testing simulation
- Interactive analytics dashboard

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Sentence Transformers
- FAISS
- Plotly
- Streamlit
- Git
- GitHub

## Repository Structure

```text
newslens-ai/
├── app/
├── data/
├── notebooks/
├── src/
├── tests/
└── docs/
```

## Dataset

This project uses the Microsoft **MIND News Dataset**.

To download:

https://msnews.github.io/

Place the extracted files inside:

```text
data/raw/MINDsmall/
```

The dataset is excluded from this repository because of its size and licensing.

## Roadmap

- [x] Project setup
- [ ] Data exploration
- [ ] Data preprocessing
- [ ] Content-based recommender
- [ ] Collaborative filtering
- [ ] Hybrid recommender
- [ ] Evaluation metrics
- [ ] Editorial analytics dashboard
- [ ] A/B testing simulation
- [ ] Streamlit application

## License

MIT
