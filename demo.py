"""
Simple demo script showcasing all features of the Bijoy Poetry Generator
This demonstrates the complete functionality in one script
"""

import time
from poetry_generator import BijoyPoetryGenerator


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def print_poem(poem, title="Generated Poem"):
    """Print a poem with nice formatting"""
    print(f"\n{title}:")
    print("-" * 60)
    for line in poem.split('\n'):
        print(f"  {line}")
    print("-" * 60)


def demo():
    """Run the complete demo"""
    print("\n")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                                                                  ║")
    print("║     BIJOY DIBOSH AI POETRY GENERATOR - DEMO  🇧🇩                ║")
    print("║     Victory Day Patriotic Poetry & Slogan Generator             ║")
    print("║                                                                  ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    
    # ===== SECTION 1: Introduction =====
    print_section("1. INTRODUCTION")
    print("This AI-powered tool generates patriotic poems and slogans for")
    print("Bangladesh Victory Day (Bijoy Dibosh - December 16).")
    print()
    print("Features:")
    print("  • Theme-based poetry generation (Freedom, Sacrifice, Victory, etc.)")
    print("  • Bilingual support (English & Bengali)")
    print("  • Multiple variations per theme")
    print("  • Random Victory Day slogans")
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 2: Initialize Generators =====
    print_section("2. INITIALIZING GENERATORS")
    print("Creating English and Bengali poetry generators...")
    print("(This may take a moment on first run)")
    print()
    
    gen_en = BijoyPoetryGenerator(language="english", use_gpu=False)
    print("✓ English generator ready")
    
    gen_bn = BijoyPoetryGenerator(language="bengali", use_gpu=False)
    print("✓ Bengali generator ready")
    
    time.sleep(1)
    
    # ===== SECTION 3: Available Themes =====
    print_section("3. AVAILABLE THEMES")
    themes = gen_en.get_available_themes()
    print(f"We have {len(themes)} themes available:\n")
    for i, theme in enumerate(themes, 1):
        print(f"  {i}. {theme.capitalize()}")
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 4: English Poetry Examples =====
    print_section("4. ENGLISH POETRY GENERATION")
    
    # Example 1: Freedom
    print("Theme: FREEDOM")
    print("Generating poem about freedom and independence...")
    poems = gen_en.generate(theme="Freedom", num_outputs=1)
    print_poem(poems[0], "Freedom Poem")
    print()
    input("Press Enter for next theme...")
    
    # Example 2: Sacrifice
    print("\nTheme: SACRIFICE")
    print("Generating poem honoring the martyrs...")
    poems = gen_en.generate(theme="Sacrifice", num_outputs=1)
    print_poem(poems[0], "Sacrifice Poem")
    print()
    input("Press Enter for next theme...")
    
    # Example 3: Victory
    print("\nTheme: VICTORY")
    print("Generating poem celebrating December 16...")
    poems = gen_en.generate(theme="Victory", num_outputs=1)
    print_poem(poems[0], "Victory Poem")
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 5: Bengali Poetry Examples =====
    print_section("5. BENGALI POETRY GENERATION (বাংলা কবিতা)")
    
    # Example 1: বিজয়
    print("থিম: বিজয় (Victory)")
    print("বাংলায় কবিতা তৈরি করা হচ্ছে...")
    poems = gen_bn.generate(theme="বিজয়", num_outputs=1)
    print_poem(poems[0], "বিজয়ের কবিতা")
    print()
    input("Press Enter for next theme...")
    
    # Example 2: স্বাধীনতা
    print("\nথিম: স্বাধীনতা (Independence)")
    print("বাংলায় কবিতা তৈরি করা হচ্ছে...")
    poems = gen_bn.generate(theme="স্বাধীনতা", num_outputs=1)
    print_poem(poems[0], "স্বাধীনতার কবিতা")
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 6: Multiple Variations =====
    print_section("6. GENERATING MULTIPLE VARIATIONS")
    print("Generating 3 different poems on the same theme: HEROES")
    print()
    
    poems = gen_en.generate(theme="Heroes", num_outputs=3)
    for i, poem in enumerate(poems, 1):
        print_poem(poem, f"Heroes Poem - Variation {i}")
        if i < len(poems):
            time.sleep(0.5)
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 7: Random Slogans =====
    print_section("7. RANDOM VICTORY DAY SLOGANS")
    print("Generating 5 random patriotic slogans...\n")
    
    for i in range(5):
        slogan = gen_en.get_random_slogan()
        print(f"  {i+1}. {slogan}")
        time.sleep(0.3)
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 8: Custom Theme Example =====
    print_section("8. CUSTOM THEME GENERATION")
    print("You can use ANY theme - the AI will adapt!")
    print()
    
    custom_themes = ["Courage", "Unity", "Future"]
    for theme in custom_themes:
        print(f"Theme: {theme.upper()}")
        poems = gen_en.generate(theme=theme, num_outputs=1)
        print_poem(poems[0])
        print()
        time.sleep(0.5)
    
    input("Press Enter to continue...")
    
    # ===== SECTION 9: Usage Summary =====
    print_section("9. HOW TO USE THIS TOOL")
    print("You have THREE ways to use this generator:\n")
    
    print("1. COMMAND LINE (Quickest):")
    print("   python generate_poetry.py --theme \"Freedom\"")
    print("   python generate_poetry.py --theme \"বিজয়\" --language bengali\n")
    
    print("2. WEB INTERFACE (Most User-Friendly):")
    print("   python app.py")
    print("   Then open http://localhost:5000 in your browser\n")
    
    print("3. PYTHON API (For Developers):")
    print("   from poetry_generator import BijoyPoetryGenerator")
    print("   generator = BijoyPoetryGenerator()")
    print("   poems = generator.generate(theme='Freedom')")
    print()
    input("Press Enter to continue...")
    
    # ===== SECTION 10: Conclusion =====
    print_section("10. CONCLUSION")
    print("🇧🇩 This AI Poetry Generator helps celebrate Victory Day!")
    print()
    print("Key Features Demonstrated:")
    print("  ✓ Theme-based poetry generation")
    print("  ✓ English and Bengali support")
    print("  ✓ Multiple variations")
    print("  ✓ Random slogans")
    print("  ✓ Customizable themes")
    print()
    print("Perfect for:")
    print("  • Victory Day celebrations")
    print("  • Social media posts")
    print("  • Educational purposes")
    print("  • Patriotic events")
    print("  • Commemorative content")
    print()
    print("Thank you for using the Bijoy Dibosh Poetry Generator!")
    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                    জয় বাংলা! 🇧🇩                                ║")
    print("║              Victory to Bengal! Long Live Bangladesh!            ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()
    print("For more information, see README.md and QUICKSTART.md")
    print()


if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. জয় বাংলা! 🇧🇩\n")
    except Exception as e:
        print(f"\n\nError during demo: {e}")
        print("Please ensure all dependencies are installed: pip install -r requirements.txt")
        import traceback
        traceback.print_exc()
