"""
Test script to verify the Bijoy Poetry Generator installation and functionality
Run this to ensure everything is working correctly
"""

import sys
import os

print("="*70)
print("BIJOY DIBOSH POETRY GENERATOR - SYSTEM TEST")
print("="*70)
print()

# Test 1: Check Python version
print("Test 1: Python Version Check")
print("-" * 70)
python_version = sys.version_info
print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
if python_version.major >= 3 and python_version.minor >= 8:
    print("✓ Python version is compatible (3.8+)")
else:
    print("✗ Python version too old. Need 3.8+")
    sys.exit(1)
print()

# Test 2: Check dependencies
print("Test 2: Dependency Check")
print("-" * 70)
required_packages = [
    'torch',
    'transformers',
    'flask',
    'numpy',
]

missing_packages = []
for package in required_packages:
    try:
        __import__(package)
        print(f"✓ {package:20} - installed")
    except ImportError:
        print(f"✗ {package:20} - MISSING")
        missing_packages.append(package)

if missing_packages:
    print(f"\n✗ Missing packages: {', '.join(missing_packages)}")
    print("  Run: pip install -r requirements.txt")
    sys.exit(1)
print()

# Test 3: Check file structure
print("Test 3: File Structure Check")
print("-" * 70)
required_files = [
    'config.py',
    'poetry_generator.py',
    'generate_poetry.py',
    'app.py',
    'data/training_data.json',
    'data/themes.json',
    'templates/index.html'
]

missing_files = []
for file_path in required_files:
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    if os.path.exists(full_path):
        print(f"✓ {file_path:30} - exists")
    else:
        print(f"✗ {file_path:30} - MISSING")
        missing_files.append(file_path)

if missing_files:
    print(f"\n✗ Missing files: {', '.join(missing_files)}")
    sys.exit(1)
print()

# Test 4: Load configuration
print("Test 4: Configuration Loading")
print("-" * 70)
try:
    import config
    print(f"✓ Config loaded successfully")
    print(f"  - Bengali model: {config.MODEL_CONFIG['bengali']['model_name']}")
    print(f"  - English model: {config.MODEL_CONFIG['english']['model_name']}")
    print(f"  - Temperature: {config.GENERATION_CONFIG['temperature']}")
except Exception as e:
    print(f"✗ Failed to load config: {e}")
    sys.exit(1)
print()

# Test 5: Test poetry generator initialization
print("Test 5: Poetry Generator Initialization")
print("-" * 70)
try:
    from poetry_generator import BijoyPoetryGenerator
    
    print("Testing English generator...")
    gen_en = BijoyPoetryGenerator(language="english", use_gpu=False)
    print("✓ English generator initialized")
    
    print("Testing Bengali generator...")
    gen_bn = BijoyPoetryGenerator(language="bengali", use_gpu=False)
    print("✓ Bengali generator initialized")
    
except Exception as e:
    print(f"✗ Generator initialization failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
print()

# Test 6: Generate sample poems (template-based)
print("Test 6: Sample Poetry Generation (Template Mode)")
print("-" * 70)
try:
    print("\nGenerating English poem (theme: Freedom)...")
    poems_en = gen_en.generate(theme="Freedom", num_outputs=1)
    print("✓ Generated successfully:")
    print()
    for line in poems_en[0].split('\n'):
        print(f"  {line}")
    print()
    
    print("Generating Bengali poem (theme: বিজয়)...")
    poems_bn = gen_bn.generate(theme="বিজয়", num_outputs=1)
    print("✓ Generated successfully:")
    print()
    for line in poems_bn[0].split('\n'):
        print(f"  {line}")
    print()
    
except Exception as e:
    print(f"✗ Generation failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 7: Test themes and slogans
print("Test 7: Themes and Slogans")
print("-" * 70)
try:
    themes = gen_en.get_available_themes()
    print(f"✓ Available themes ({len(themes)}): {', '.join(themes)}")
    
    slogan = gen_en.get_random_slogan()
    print(f"✓ Random slogan: {slogan}")
    
except Exception as e:
    print(f"✗ Themes/slogans test failed: {e}")
    sys.exit(1)
print()

# Test 8: Check GPU availability
print("Test 8: GPU Availability")
print("-" * 70)
try:
    import torch
    if torch.cuda.is_available():
        print(f"✓ GPU available: {torch.cuda.get_device_name(0)}")
        print(f"  CUDA version: {torch.version.cuda}")
    else:
        print("ℹ GPU not available (will use CPU)")
        print("  This is fine - generation will work but be slower")
except Exception as e:
    print(f"ℹ Could not check GPU: {e}")
print()

# Final summary
print("="*70)
print("TEST SUMMARY")
print("="*70)
print("✓ All core tests passed!")
print()
print("Your Bijoy Poetry Generator is ready to use!")
print()
print("Quick Start Commands:")
print("  1. CLI:  python generate_poetry.py --theme \"Freedom\"")
print("  2. Web:  python app.py  (then open http://localhost:5000)")
print("  3. Interactive: python generate_poetry.py --interactive")
print()
print("জয় বাংলা! 🇧🇩")
print("="*70)
