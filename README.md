# Bijoy Dibosh AI Poetry Generator 🇧🇩

An AI-powered text generation system that creates inspirational poems and slogans for Victory Day (Bijoy Dibosh) using machine learning and NLP.

## Features

- **Theme-based Generation**: Input themes like "Freedom," "Sacrifice," "Future" to generate contextual poetry
- **Bilingual Support**: Generates content in both Bengali and English
- **Transformer-based Model**: Uses pre-trained models fine-tuned on patriotic content
- **4-line Output Format**: Generates concise, impactful 4-line poems/slogans
- **Multiple Variations**: Generate multiple variations for the same theme

## Technology Stack

- **Python 3.8+**
- **Transformers** (Hugging Face)
- **PyTorch** for model training/inference
- **Bengali NLP** libraries for text processing

## Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download pre-trained model (optional):**
The system will automatically download the required model on first run.

## Usage

### Command Line Interface

```bash
# Generate poetry with a theme
python generate_poetry.py --theme "Freedom"

# Generate multiple variations
python generate_poetry.py --theme "Sacrifice" --num-outputs 3

# Specify language
python generate_poetry.py --theme "Future" --language "bengali"
```

### Python API

```python
from poetry_generator import BijoyPoetryGenerator

# Initialize generator
generator = BijoyPoetryGenerator()

# Generate poetry
poem = generator.generate(theme="Freedom", language="english")
print(poem)
```

### Web Interface

```bash
# Start Flask server
python app.py

# Access at http://localhost:5000
```

## Project Structure

```
BIJOY54/
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── poetry_generator.py      # Core generation module
├── generate_poetry.py       # CLI interface
├── app.py                   # Web interface (Flask)
├── config.py                # Configuration settings
├── data/
│   ├── training_data.json   # Sample training data
│   └── themes.json          # Theme keywords and prompts
└── models/
    └── (downloaded models stored here)
```

## Sample Output

**Theme: Freedom**
```
Through the blood of martyrs, we stand tall and free,
December's victory echoes across the land and sea,
Independence blooms where sacrifice once grew,
Bijoy Dibosh reminds us of the brave and true.
```

**Theme: Sacrifice (Bengali)**
```
শহীদদের রক্তে লেখা স্বাধীনতার গান,
বিজয়ের পতাকা উড়ে সকল প্রাণ,
আত্মত্যাগের মূল্যে পেয়েছি এই দেশ,
বীরদের স্মৃতি থাকবে চিরকাল অশেষ।
```

## Customization

- **Fine-tune on custom data**: Add your own poems/slogans to `data/training_data.json`
- **Adjust generation parameters**: Modify `config.py` for temperature, max_length, etc.
- **Add new themes**: Update `data/themes.json` with custom themes and keywords

## Model Information

This project uses transformer-based models:
- **Bengali**: BanglaBERT or similar models fine-tuned for poetry generation
- **English**: GPT-2 or similar models adapted for patriotic content

## Contributing

Feel free to contribute by:
- Adding more training data
- Improving the model fine-tuning
- Creating better UI/UX
- Adding more languages

## License

MIT License - Feel free to use for educational and commemorative purposes.

## Acknowledgments

Dedicated to the freedom fighters of Bangladesh and the spirit of December 16, 1971.

**জয় বাংলা! 🇧🇩**
