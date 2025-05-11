# Spanglish Sentiment Classification with LLMs

This project evaluates how well Large Language Models (LLMs) handle *Spanglish*—a blend of Spanish and English—specifically in the task of sentiment analysis.  
Given that millions of U.S. residents regularly communicate in Spanglish, and that most LLMs are primarily trained on English, this study investigates whether these models show bias or reduced performance when interpreting code-mixed text.  

The goal is to better understand LLM limitations in multilingual settings and advocate for more inclusive and representative NLP systems.

## Report
[Evaluating LLM Comprehension of Spanglish](Evaluating%20LLM%20Comprehension%20of%20Spanglish.pdf)

## Repository Structure
### `dataset/`
Contains all data files used throughout the project.

- **`predictions.json`**  
  Contains the LLM-generated sentiment predictions. Each entry includes:  
  - `id`: unique identifier for the tweet  
  - `sentiment`: predicted label (`positive`, `neutral`, or `negative`)  
  - `confidence`: model's confidence score (0–1)  
  - `reason`: brief justification for the prediction

- **`spanglish_dataset.json`**  
  Reformatted version of the original dataset from `.conll` to `.json` for ease of use.

- **`test_dataset.json`**  
  A subset of `spanglish_dataset.json` used for evaluating the LLM’s performance.

- **`Spanglish_dev.conll`**  
  The full original dataset in `.conll` format.

- **`Spanglish_test_conll_unlabeled.txt`**  
  Unlabeled test set from the original corpus (not used in this project).

- **`Spanglish_train.conll`**  
  Training set from the original corpus (not used in this project).

### `pictures/`
Includes visualizations and graphs generated during exploratory data analysis and used in the final report.

## Scripts and Notebooks

- **`FormatData.py`**  
  Script for converting `.conll` format files into `.json` format.

- **`dataEDA.ipynb`**  
  Notebook for performing exploratory data analysis and generating visual insights from the dataset.

- **`LLM_Testing_Script.ipynb`**  
  Sanity check notebook used to verify the prompt format and model behavior.

- **`Spanglish Sentiment Model.ipynb`**  
  Core notebook that runs the structured prompt, gathers model outputs, and saves results into `predictions.json`.
