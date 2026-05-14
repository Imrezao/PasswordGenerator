# Password Generator

A Python-based password generator with multiple generation methods and an interactive Streamlit dashboard.

## Requirements

- Python 3.7+
- streamlit
- nltk

Install dependencies:
```bash
pip install streamlit nltk
```
Download NLTK words corpus:

```
python -c "import nltk; nltk.download('words')"
```
## Running the Project

### Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```


## Features

- **PIN Generator**: Generate numeric PINs of any length
- **Random Password Generator**: Create secure passwords with customizable length, symbols, and numbers
- **Memorable Password Generator**: Generate easy-to-remember passphrases using English words
- **Interactive Dashboard**: User-friendly Streamlit interface with copy-to-clipboard functionality
