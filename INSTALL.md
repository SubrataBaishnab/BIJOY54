# INSTALLATION & SETUP GUIDE
# Bijoy Dibosh AI Poetry Generator

## Complete Installation Instructions

### Step 1: Install Python (if not already installed)
- Download Python 3.8 or higher from https://www.python.org/downloads/
- During installation, CHECK "Add Python to PATH"
- Verify installation: `python --version`

### Step 2: Install Dependencies
Open PowerShell in the BIJOY54 directory and run:

```powershell
# Navigate to project directory
cd d:\BIJOY54

# Install all required packages
pip install -r requirements.txt
```

This will install:
- PyTorch (deep learning framework)
- Transformers (Hugging Face models)
- Flask (web server)
- Bengali NLP tools
- Other utilities

**Note:** First installation may take 5-10 minutes and download ~2GB of data.

### Step 3: Test the Installation

```powershell
# Run the test script
python test_system.py
```

This will verify:
- Python version
- All dependencies installed
- File structure correct
- Generators working
- Sample poetry generation

### Step 4: Try It Out!

Choose one of these methods:

#### Method 1: Quick CLI Test
```powershell
python generate_poetry.py --theme "Freedom"
```

#### Method 2: Interactive Mode
```powershell
python generate_poetry.py --interactive
```

#### Method 3: Web Interface
```powershell
python app.py
```
Then open: http://localhost:5000

#### Method 4: Run Full Demo
```powershell
python demo.py
```

## Detailed Usage Guide

### Command Line Interface Options

```powershell
# Generate single poem
python generate_poetry.py --theme "Freedom"

# Generate in Bengali
python generate_poetry.py --theme "বিজয়" --language bengali

# Generate multiple variations
python generate_poetry.py --theme "Sacrifice" --num-outputs 3

# Get random slogan
python generate_poetry.py --slogan

# List all themes
python generate_poetry.py --list-themes

# Interactive mode
python generate_poetry.py --interactive

# Disable GPU (if causing issues)
python generate_poetry.py --theme "Victory" --no-gpu
```

### Web Interface Usage

1. Start server:
   ```powershell
   python app.py
   ```

2. Open browser to: `http://localhost:5000`

3. Use the web form:
   - Enter theme (Freedom, Sacrifice, etc.)
   - Select language (English/Bengali)
   - Choose number of variations (1-5)
   - Click "Generate Poem" or "Random Slogan"

### Python API Usage

Create a new Python script or use in Jupyter notebook:

```python
from poetry_generator import BijoyPoetryGenerator

# Initialize generator
generator = BijoyPoetryGenerator(language="english")

# Generate poem
poems = generator.generate(theme="Freedom", num_outputs=1)
print(poems[0])

# Generate multiple variations
poems = generator.generate(theme="Sacrifice", num_outputs=3)
for i, poem in enumerate(poems, 1):
    print(f"\n--- Poem {i} ---")
    print(poem)

# Get available themes
themes = generator.get_available_themes()
print(f"Available: {themes}")

# Get random slogan
slogan = generator.get_random_slogan()
print(slogan)

# Switch to Bengali
generator_bn = BijoyPoetryGenerator(language="bengali")
bengali_poems = generator_bn.generate(theme="বিজয়")
print(bengali_poems[0])
```

## Customization Guide

### Add Your Own Poems

Edit `data/training_data.json`:

```json
{
  "english_poems": [
    {
      "theme": "your_theme",
      "text": "Line 1 of your poem\nLine 2\nLine 3\nLine 4"
    }
  ]
}
```

### Add New Themes

Edit `data/themes.json`:

```json
{
  "themes": {
    "your_theme": {
      "bengali": ["keyword1", "keyword2"],
      "english": ["keyword1", "keyword2"],
      "prompts": ["Write a poem about..."]
    }
  }
}
```

### Adjust Generation Settings

Edit `config.py`:

```python
GENERATION_CONFIG = {
    "temperature": 0.8,      # 0.0-1.0 (higher = more creative)
    "max_new_tokens": 100,   # Length of output
    "top_k": 50,             # Diversity
    "top_p": 0.92,           # Nucleus sampling
}
```

### Change Models

Edit `config.py` to use different models:

```python
MODEL_CONFIG = {
    "bengali": {
        "model_name": "sagorsarker/bangla-gpt2",  # Alternative
    },
    "english": {
        "model_name": "gpt2-medium",  # Larger, better quality
    }
}
```

## Troubleshooting

### Problem: "pip install" fails
**Solution:**
```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Then try again
pip install -r requirements.txt
```

### Problem: Model download is slow
**Solution:**
- This is normal for first run (downloading ~500MB-1GB)
- Subsequent runs will be fast (models are cached)
- Use template mode (automatic fallback) for instant results

### Problem: Out of memory error
**Solution:**
```powershell
# Use smaller model
python generate_poetry.py --theme "Freedom" --no-gpu
```

Or edit `config.py`:
```python
MODEL_CONFIG = {
    "english": {
        "model_name": "distilgpt2",  # Smaller, faster
    }
}
```

### Problem: Bengali text shows as boxes/squares
**Solution:**
- Use the web interface (best Unicode support)
- Update your terminal font to one supporting Bengali (e.g., "Noto Sans Bengali")
- Or output to file:
  ```powershell
  python generate_poetry.py --theme "বিজয়" --language bengali > output.txt
  ```

### Problem: "ModuleNotFoundError"
**Solution:**
```powershell
# Ensure you're in the right directory
cd d:\BIJOY54

# Install missing module specifically
pip install <module_name>

# Or reinstall all
pip install -r requirements.txt --force-reinstall
```

### Problem: Generation takes too long
**Solution:**
- First run is always slower (model loading)
- Subsequent runs: 2-5 seconds
- Template mode (fallback): instant
- Use `--no-gpu` if GPU causing issues

### Problem: Flask app won't start
**Solution:**
```powershell
# Check if port 5000 is in use
netstat -ano | findstr :5000

# Use different port in config.py
API_CONFIG = {
    "port": 5001,  # Change this
}
```

## Performance Optimization

### For Faster Generation:
1. Use GPU if available (automatically detected)
2. Keep models loaded (don't restart scripts)
3. Generate multiple poems at once
4. Use template mode for instant results

### For Better Quality:
1. Use larger models (gpt2-medium)
2. Add more training examples
3. Adjust temperature (0.7-0.9 for poetry)
4. Increase num_beams (4-8)

### For Lower Resource Usage:
1. Use `distilgpt2` or smaller models
2. Set `use_gpu=False`
3. Reduce `max_new_tokens`
4. Use template mode

## System Requirements

### Minimum:
- Python 3.8+
- 4GB RAM
- 2GB disk space
- Windows/Linux/Mac

### Recommended:
- Python 3.9+
- 8GB RAM
- 4GB disk space
- NVIDIA GPU (optional, but faster)

### For Bengali Support:
- Unicode-capable terminal/browser
- Bengali font installed
- UTF-8 encoding

## Advanced Features

### Batch Processing

Create `batch_generate.py`:
```python
from poetry_generator import BijoyPoetryGenerator

generator = BijoyPoetryGenerator()
themes = ["Freedom", "Sacrifice", "Victory", "Heroes"]

for theme in themes:
    poems = generator.generate(theme, num_outputs=2)
    with open(f"output_{theme}.txt", "w", encoding="utf-8") as f:
        for i, poem in enumerate(poems, 1):
            f.write(f"=== {theme} - Poem {i} ===\n")
            f.write(poem + "\n\n")
```

### API Integration

Use as REST API:
```python
import requests

response = requests.post("http://localhost:5000/api/generate", json={
    "theme": "Freedom",
    "language": "english",
    "num_outputs": 2
})

data = response.json()
for poem in data['poems']:
    print(poem)
```

## Getting Help

If you encounter issues:

1. Run diagnostic: `python test_system.py`
2. Check logs for error messages
3. Verify all files present: see project structure below
4. Ensure Python 3.8+ installed
5. Try reinstalling dependencies

## Project Structure

```
BIJOY54/
├── README.md                 # Main documentation
├── QUICKSTART.md            # Quick start guide
├── INSTALL.md               # This file
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
│
├── config.py               # Configuration settings
├── poetry_generator.py     # Core generator module
├── generate_poetry.py      # CLI interface
├── app.py                  # Web interface
├── demo.py                 # Interactive demo
├── test_system.py          # System test script
│
├── data/
│   ├── training_data.json  # Sample poems database
│   └── themes.json         # Theme definitions
│
├── templates/
│   └── index.html          # Web UI
│
└── models/
    └── README.md           # Models download here
```

## Next Steps

1. ✅ Complete installation
2. ✅ Run `python test_system.py`
3. ✅ Try `python demo.py`
4. ✅ Generate your first poem
5. ✅ Customize with your own poems
6. ✅ Share for Victory Day! 🇧🇩

## জয় বাংলা! 🇧🇩

Enjoy creating patriotic poetry for Bangladesh Victory Day!
