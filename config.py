"""
Configuration settings for Bijoy Dibosh Poetry Generator
"""

import os

# Model Configuration
MODEL_CONFIG = {
    "bengali": {
        "model_name": "csebuetnlp/mT5_multilingual_XLSum",  # Good for Bengali
        "tokenizer_name": "csebuetnlp/mT5_multilingual_XLSum",
        "max_length": 150,
        "alternative_models": [
            "sagorsarker/bangla-gpt2",
            "flax-community/gpt2-bengali"
        ]
    },
    "english": {
        "model_name": "gpt2",  # Standard GPT-2 for English
        "tokenizer_name": "gpt2",
        "max_length": 150,
        "alternative_models": [
            "gpt2-medium",
            "distilgpt2"
        ]
    }
}

# Generation Parameters
GENERATION_CONFIG = {
    "temperature": 0.8,          # Higher = more creative, lower = more focused
    "top_k": 50,                  # Consider top k tokens
    "top_p": 0.92,                # Nucleus sampling
    "repetition_penalty": 1.2,    # Penalize repetition
    "num_return_sequences": 1,    # Number of outputs per generation
    "do_sample": True,            # Enable sampling
    "max_new_tokens": 100,        # Maximum tokens to generate
    "num_beams": 4,               # Beam search width
    "early_stopping": True        # Stop when all beams finish
}

# Poetry Format
POETRY_FORMAT = {
    "lines": 4,                   # Default number of lines
    "min_line_length": 10,        # Minimum characters per line
    "max_line_length": 80,        # Maximum characters per line
}

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")
TRAINING_DATA_PATH = os.path.join(DATA_DIR, "training_data.json")
THEMES_DATA_PATH = os.path.join(DATA_DIR, "themes.json")

# Create directories if they don't exist
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Prompts Templates
PROMPT_TEMPLATES = {
    "bengali": {
        "prefix": "বিজয় দিবসের উপর একটি {theme} সম্পর্কিত কবিতা:\n",
        "suffix": "\n\n"
    },
    "english": {
        "prefix": "A patriotic Victory Day poem about {theme}:\n",
        "suffix": "\n\n"
    }
}

# Theme Mapping (for user input flexibility)
THEME_ALIASES = {
    "freedom": ["freedom", "liberty", "independence", "মুক্তি", "স্বাধীনতা"],
    "sacrifice": ["sacrifice", "martyrs", "ত্যাগ", "শহীদ"],
    "victory": ["victory", "triumph", "win", "বিজয়", "জয়"],
    "heroes": ["heroes", "fighters", "warriors", "বীর", "মুক্তিযোদ্ধা"],
    "future": ["future", "tomorrow", "next generation", "ভবিষ্যৎ", "প্রজন্ম"],
    "independence": ["independence", "liberation", "স্বাধীনতা", "মুক্তিযুদ্ধ"],
    "unity": ["unity", "together", "solidarity", "ঐক্য", "একতা"],
    "courage": ["courage", "bravery", "valor", "সাহস", "বীরত্ব"]
}

# API Configuration (if using web interface)
import os
API_CONFIG = {
    "host": "0.0.0.0",
    "port": int(os.environ.get("PORT", 5000)),
    "debug": os.environ.get("DEBUG", "False") == "True"
}

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
