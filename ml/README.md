# ML – AI Journal

This folder contains all data science and machine learning code for the AI Journal project. It focuses on extracting structure, patterns, and insights from long-term journal data to power features like emotion analytics, topic discovery, life phases, and personalised AI behaviour.

The goal of this module is to make the AI Journal more intelligent, not just by calling an LLM, but by building real ML pipelines that analyse the user’s writing over time.

## Responsibilities

- Preprocessing journal and chat data for modelling
- Training and evaluating ML/NLP models
- Running offline analysis (clustering, topic modelling, time series)
- Exporting models for use in the backend services
- Producing reports that are useful for recruiters and documentation

## Planned ML Components

- **Emotion Classification**  
  Predicts emotional states (e.g. sad, anxious, hopeful, calm, angry) from each journal entry.

- **Topic Modelling / Classification**  
  Discovers or classifies recurring themes such as relationships, uni, gym, work, family, identity, etc.

- **Life Phase Clustering**  
  Groups entries into “phases” or “chapters” (e.g. *The Alina Phase*, *School Captain Era*, *Gym Grind*) using embeddings and clustering.

- **Time Series Mood Analysis**  
  Tracks mood and emotional volatility over time and supports features like weekly dashboards and burnout risk estimation.

- **Entity & Relationship Analysis**  
  Uses NER and sentiment/emotion signals to understand how different people or entities (e.g. Alina, Mum, Uni, Gym) affect the user emotionally.

- **Long-Term Memory Extraction**  
  Identifies important facts and insights from chats (e.g. core fears, values, goals) and stores them as structured memory.

## Suggested Folder Structure

- `notebooks/`  
  Jupyter notebooks for exploration, prototyping, and visualisation. Examples:
  - `01_explore_journals.ipynb`
  - `02_emotion_model.ipynb`
  - `03_topic_modelling.ipynb`
  - `04_phase_clustering.ipynb`
  - `05_time_series_mood.ipynb`

- `pipeline/`  
  Python scripts that implement reusable steps:
  - `preprocess.py` – text cleaning, tokenisation, normalisation
  - `features.py` – turning text into features/embeddings
  - `train_emotion.py` – training the emotion classifier
  - `train_topics.py` – training topic models/classifiers
  - `train_phases.py` – clustering and phase discovery
  - `evaluate_*.py` – evaluation scripts with metrics and plots

- `models/`  
  Saved model artefacts:
  - `emotion_classifier/`
  - `topic_model/`
  - `phase_clustering/`
  Each folder can contain model weights (`.pt`, `.pkl`, etc.), configuration files, and label mappings.

- `reports/`  
  Short markdown or PDF reports describing:
  - datasets used
  - model architectures and parameters
  - evaluation metrics (accuracy, F1, confusion matrices, etc.)
  - interpretation of results and limitations

## How This Integrates With the Backend

The backend (`/backend`) will import and use parts of this module to power features like:

- Weekly dashboards (emotion and topic trends per user)
- Life timeline and phases
- Relationship insights
- Enhanced context for AI chat (e.g. passing emotion/topic summaries into GPT)

Typical flow:

1. Journals are stored in the database.
2. Batch or online jobs in `/ml/pipeline` generate features and model predictions.
3. Results (e.g. emotion scores, topic tags, cluster IDs) are written back into the database.
4. Backend services (e.g. `analytics_service.py`, `timeline_service.py`) read these values and expose them via API to the frontend.

## Getting Started

1. Create a Python virtual environment for ML work (you can share or separate from the backend venv).
2. Install common DS/ML libraries:
   - `pandas`, `numpy`
   - `scikit-learn`
   - `matplotlib`, `seaborn`, `plotly`
   - `transformers`, `datasets` (for NLP models, optional but useful)
3. Start with `notebooks/01_explore_journals.ipynb` once you have some sample journal data in the database. Use this to understand:
   - average entry length
   - common words/phrases
   - rough emotional distribution (even using simple heuristics at first)

From there, you can iteratively build and improve models, then integrate them into the backend once they reach a useful level of performance.
