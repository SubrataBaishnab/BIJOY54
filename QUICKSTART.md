# Quick Start Guide - Bijoy Dibosh Poetry Generator

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd d:\BIJOY54
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - TensorFlow/PyTorch and Transformers
   - Bengali NLP libraries
   - Flask (for web interface)
   - Other dependencies

## Usage Options

### Option 1: Command Line Interface (Simplest)

**Generate a single poem:**
```bash
python generate_poetry.py --theme "Freedom"
```

**Generate multiple variations:**
```bash
python generate_poetry.py --theme "Sacrifice" --num-outputs 3
```

**Bengali poetry:**
```bash
python generate_poetry.py --theme "বিজয়" --language bengali
```

**Interactive mode:**
```bash
python generate_poetry.py --interactive
```

**Get a random slogan:**
```bash
python generate_poetry.py --slogan
```

**List available themes:**
```bash
python generate_poetry.py --list-themes
```

### Option 2: Web Interface (Most User-Friendly)

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   Navigate to: `http://localhost:5000`

3. **Use the web interface:**
   - Enter a theme (Freedom, Sacrifice, etc.)
   - Select language (English or Bengali)
   - Choose number of variations
   - Click "Generate Poem" or "Random Slogan"

### Option 3: Python API (For Developers)

```python
from poetry_generator import BijoyPoetryGenerator

# Initialize generator
generator = BijoyPoetryGenerator(language="english")

# Generate a poem
poems = generator.generate(theme="Freedom", num_outputs=2)
for poem in poems:
    print(poem)
    print("-" * 60)

# Get available themes
themes = generator.get_available_themes()
print(f"Available themes: {themes}")

# Get a random slogan
slogan = generator.get_random_slogan()
print(f"Slogan: {slogan}")
```

## Themes Available

- **freedom** - স্বাধীনতা
- **sacrifice** - ত্যাগ
- **victory** - বিজয়
- **heroes** - বীর
- **future** - ভবিষ্যৎ
- **independence** - স্বাধীনতা
- **unity** - ঐক্য
- **courage** - সাহস

## How It Works

1. **Template-Based Generation (Default):**
   - Uses pre-written Bengali and English patriotic poems
   - Mixes and matches lines based on themes
   - Fast and reliable, no model download needed

2. **AI Model Generation (Advanced):**
   - Downloads pre-trained transformer models on first run
   - Fine-tunes on patriotic content
   - Generates unique, contextually relevant poetry
   - Requires GPU for best performance (but works on CPU)

## Model Information

### Bengali:
- Primary: `csebuetnlp/mT5_multilingual_XLSum` (Multilingual T5)
- Alternatives: `sagorsarker/bangla-gpt2`, `flax-community/gpt2-bengali`

### English:
- Primary: `gpt2` (OpenAI GPT-2)
- Alternatives: `gpt2-medium`, `distilgpt2`

Models are automatically downloaded from Hugging Face on first use.

## Customization

### Add Your Own Poems:
Edit `data/training_data.json` and add poems in this format:
```json
{
  "theme": "your_theme",
  "text": "Your four-line poem here\nLine 2\nLine 3\nLine 4"
}
```

### Adjust Generation Settings:
Edit `config.py` to change:
- `temperature` - Creativity level (0.0 to 1.0)
- `max_new_tokens` - Length of generated text
- `num_beams` - Quality of generation

### Add New Themes:
Edit `data/themes.json` to add new themes with keywords.

## Troubleshooting

**Problem:** Model download is slow
- **Solution:** First run downloads ~500MB of model files. This is one-time only.

**Problem:** Out of memory error
- **Solution:** Use `--no-gpu` flag or edit config.py to use smaller models like `distilgpt2`.

**Problem:** Bengali text not displaying
- **Solution:** Ensure your terminal/browser supports Unicode. Use the web interface for best results.

**Problem:** Generation takes too long
- **Solution:** Template-based generation is instant. Model-based takes 5-10 seconds first time.

## Performance Notes

- **First Run:** 30-60 seconds (model download)
- **Subsequent Runs:** 2-5 seconds per poem
- **Template Mode:** Instant
- **Recommended:** 4GB+ RAM, GPU optional but helpful

## Examples

### Example 1: Quick English Poem
```bash
python generate_poetry.py --theme "Freedom"
```

Output:
```
Through the blood of martyrs, we stand tall and free,
December's victory echoes across the land and sea,
Independence blooms where sacrifice once grew,
Bijoy Dibosh reminds us of the brave and true.
```

### Example 2: Bengali Interactive
```bash
python generate_poetry.py --interactive
```

```
Enter theme: বিজয়
Language: bengali

ডিসেম্বরের সূর্য ওঠে
বিজয়ের আলো নিয়ে
লাল সবুজ পতাকা
উড়ছে আকাশে স্বাধীনভাবে
```

## Next Steps

1. Test with various themes
2. Experiment with the web interface
3. Add your own custom poems to the dataset
4. Fine-tune generation parameters for your needs
5. Share with others to celebrate Victory Day! 🇧🇩

## জয় বাংলা! 🇧🇩
