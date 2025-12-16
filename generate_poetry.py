"""
Command Line Interface for Bijoy Dibosh Poetry Generator
"""

import argparse
import sys
from poetry_generator import BijoyPoetryGenerator
import config


def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║   BIJOY DIBOSH AI POETRY GENERATOR  🇧🇩                  ║
    ║   Victory Day Poem & Slogan Generator                    ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_poem(poem: str, theme: str, language: str, index: int = 1, total: int = 1):
    """Pretty print a generated poem"""
    print(f"\n{'='*60}")
    if total > 1:
        print(f"  Poem {index} of {total}")
    print(f"  Theme: {theme}")
    print(f"  Language: {language.capitalize()}")
    print(f"{'='*60}\n")
    
    for line in poem.split('\n'):
        print(f"    {line}")
    
    print(f"\n{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate AI-powered Victory Day poems and slogans",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate a poem about freedom in English
  python generate_poetry.py --theme "Freedom"
  
  # Generate 3 variations about sacrifice in Bengali
  python generate_poetry.py --theme "ত্যাগ" --language bengali --num-outputs 3
  
  # Get a random slogan
  python generate_poetry.py --slogan
  
  # List available themes
  python generate_poetry.py --list-themes

Available Themes:
  freedom, sacrifice, victory, heroes, future, independence, unity, courage
  (Or use Bengali equivalents: স্বাধীনতা, ত্যাগ, বিজয়, বীর, ভবিষ্যৎ, etc.)
        """
    )
    
    parser.add_argument(
        "--theme",
        type=str,
        help="Theme for the poem (e.g., Freedom, Sacrifice, Victory)"
    )
    
    parser.add_argument(
        "--language",
        type=str,
        choices=["english", "bengali"],
        default="english",
        help="Language for generation (default: english)"
    )
    
    parser.add_argument(
        "--num-outputs",
        type=int,
        default=1,
        help="Number of different poems to generate (default: 1)"
    )
    
    parser.add_argument(
        "--slogan",
        action="store_true",
        help="Generate a random Victory Day slogan instead of a poem"
    )
    
    parser.add_argument(
        "--list-themes",
        action="store_true",
        help="List all available themes"
    )
    
    parser.add_argument(
        "--no-gpu",
        action="store_true",
        help="Disable GPU usage even if available"
    )
    
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # List themes and exit
    if args.list_themes:
        print("Available Themes:")
        print("-" * 60)
        for theme, aliases in config.THEME_ALIASES.items():
            print(f"  • {theme.capitalize():15} | Aliases: {', '.join(aliases[:3])}")
        print()
        return 0
    
    # Initialize generator
    try:
        use_gpu = not args.no_gpu
        generator = BijoyPoetryGenerator(language=args.language, use_gpu=use_gpu)
        print(f"✓ Generator initialized ({args.language})\n")
    except Exception as e:
        print(f"✗ Error initializing generator: {e}")
        return 1
    
    # Interactive mode
    if args.interactive:
        return interactive_mode(generator)
    
    # Generate slogan
    if args.slogan:
        print("Random Victory Day Slogan:")
        print("-" * 60)
        print(f"  {generator.get_random_slogan()}")
        print()
        return 0
    
    # Generate poem
    if not args.theme:
        print("✗ Error: --theme is required (or use --slogan or --interactive)")
        print("   Use --help for more information")
        return 1
    
    try:
        print(f"Generating poem(s) for theme: {args.theme}...")
        poems = generator.generate(
            theme=args.theme,
            num_outputs=args.num_outputs
        )
        
        for i, poem in enumerate(poems, 1):
            print_poem(poem, args.theme, args.language, i, len(poems))
        
        print(f"✓ Successfully generated {len(poems)} poem(s)!\n")
        
    except Exception as e:
        print(f"✗ Error generating poem: {e}")
        return 1
    
    return 0


def interactive_mode(generator: BijoyPoetryGenerator):
    """Run the generator in interactive mode"""
    print("=== Interactive Mode ===")
    print("Type 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            # Get theme
            theme = input("Enter theme (or 'help' for themes): ").strip()
            
            if theme.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye! জয় বাংলা! 🇧🇩\n")
                break
            
            if theme.lower() == 'help':
                themes = generator.get_available_themes()
                print("\nAvailable themes:")
                for t in themes:
                    print(f"  • {t}")
                print()
                continue
            
            if not theme:
                print("Please enter a theme.\n")
                continue
            
            # Get language
            lang_input = input("Language (english/bengali) [english]: ").strip().lower()
            language = lang_input if lang_input in ['bengali', 'english'] else 'english'
            
            # Generate
            print(f"\nGenerating poem for '{theme}'...\n")
            poems = generator.generate(theme=theme, language=language, num_outputs=1)
            
            if poems:
                print_poem(poems[0], theme, language)
            
            # Ask if user wants another
            another = input("Generate another? (y/n) [y]: ").strip().lower()
            if another == 'n':
                print("\nGoodbye! জয় বাংলা! 🇧🇩\n")
                break
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! জয় বাংলা! 🇧🇩\n")
            break
        except Exception as e:
            print(f"Error: {e}\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
