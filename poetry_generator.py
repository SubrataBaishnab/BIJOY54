"""
Bijoy Dibosh Poetry Generator - Core Module
Uses transformer models to generate patriotic poems and slogans
Falls back to template-based generation in low-memory environments
"""

import json
import random
import logging
from typing import List, Optional, Dict
import config

# Try to import ML libraries (optional for template-based generation)
try:
    import torch
    from transformers import (
        AutoTokenizer, 
        AutoModelForCausalLM,
        AutoModelForSeq2SeqLM,
        pipeline
    )
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False
    torch = None

# Setup logging
logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)


class BijoyPoetryGenerator:
    """
    AI-powered poetry generator for Victory Day (Bijoy Dibosh)
    """
    
    def __init__(self, language: str = "english", use_gpu: bool = None):
        """
        Initialize the poetry generator
        
        Args:
            language: "bengali" or "english"
            use_gpu: Use GPU if available (default: auto-detect)
        """
        self.language = language.lower()
        self.device = self._get_device(use_gpu)
        self.model = None
        self.tokenizer = None
        self.training_data = self._load_training_data()
        self.themes_data = self._load_themes_data()
        
        logger.info(f"Initializing Bijoy Poetry Generator for {language}")
        if ML_AVAILABLE:
            logger.info(f"Using device: {self.device}")
        else:
            logger.info("ML libraries not available - using template-based generation only")
        
    def _get_device(self, use_gpu: Optional[bool]) -> str:
        """Determine which device to use for inference"""
        if not ML_AVAILABLE or torch is None:
            return "cpu"
        if use_gpu is None:
            use_gpu = torch.cuda.is_available()
        return "cuda" if use_gpu else "cpu"
    
    def _load_training_data(self) -> Dict:
        """Load training data from JSON file"""
        try:
            with open(config.TRAINING_DATA_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Training data not found, using empty dataset")
            return {"bengali_poems": [], "english_poems": [], "slogans": []}
    
    def _load_themes_data(self) -> Dict:
        """Load themes data from JSON file"""
        try:
            with open(config.THEMES_DATA_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Themes data not found, using empty dataset")
            return {"themes": {}}
    
    def _load_model(self):
        """Load the appropriate model for the selected language"""
        # Skip model loading in low-memory environments (Render free tier)
        import os
        if os.environ.get('RENDER') or os.environ.get('SKIP_MODEL_LOADING'):
            logger.info("Skipping model loading (using template-based generation)")
            self.model = None
            self.tokenizer = None
            return
        
        if self.model is not None:
            return  # Already loaded
        
        model_config = config.MODEL_CONFIG[self.language]
        model_name = model_config["model_name"]
        
        logger.info(f"Loading model: {model_name}")
        
        try:
            # Try loading the model
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_config["tokenizer_name"],
                trust_remote_code=True
            )
            
            # Determine model type (CausalLM for GPT-style, Seq2SeqLM for T5-style)
            if "t5" in model_name.lower() or "mt5" in model_name.lower():
                self.model = AutoModelForSeq2SeqLM.from_pretrained(
                    model_name,
                    trust_remote_code=True
                ).to(self.device)
            else:
                self.model = AutoModelForCausalLM.from_pretrained(
                    model_name,
                    trust_remote_code=True
                ).to(self.device)
            
            logger.info("Model loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading model {model_name}: {e}")
            logger.info("Falling back to template-based generation")
            self.model = None
            self.tokenizer = None
    
    def _normalize_theme(self, theme: str) -> str:
        """Normalize theme input to standard theme name"""
        theme_lower = theme.lower().strip()
        
        # Check if it's already a valid theme
        if theme_lower in config.THEME_ALIASES:
            return theme_lower
        
        # Check aliases
        for standard_theme, aliases in config.THEME_ALIASES.items():
            if theme_lower in [alias.lower() for alias in aliases]:
                return standard_theme
        
        # Default to the input if no match found
        return theme_lower
    
    def _get_prompt(self, theme: str) -> str:
        """Generate a prompt for the model based on theme"""
        normalized_theme = self._normalize_theme(theme)
        template = config.PROMPT_TEMPLATES[self.language]
        
        # Get theme-specific prompts if available
        if normalized_theme in self.themes_data.get("themes", {}):
            theme_info = self.themes_data["themes"][normalized_theme]
            if "prompts" in theme_info and theme_info["prompts"]:
                base_prompt = random.choice(theme_info["prompts"])
            else:
                base_prompt = f"A Victory Day poem about {theme}"
        else:
            base_prompt = f"A Victory Day poem about {theme}"
        
        # Add examples from training data
        examples = self._get_example_poems(normalized_theme, num_examples=2)
        if examples:
            examples_text = "\n\n".join(examples)
            return f"{examples_text}\n\n{base_prompt}:\n"
        
        return template["prefix"].format(theme=theme) + base_prompt + "\n"
    
    def _get_example_poems(self, theme: str, num_examples: int = 2) -> List[str]:
        """Get example poems matching the theme from training data"""
        if self.language == "bengali":
            poems = self.training_data.get("bengali_poems", [])
        else:
            poems = self.training_data.get("english_poems", [])
        
        # Filter by theme
        matching_poems = [p["text"] for p in poems if p.get("theme") == theme]
        
        # If no exact matches, get random poems
        if not matching_poems:
            matching_poems = [p["text"] for p in poems]
        
        # Return random selection
        if len(matching_poems) <= num_examples:
            return matching_poems
        return random.sample(matching_poems, num_examples)
    
    def _generate_with_model(self, prompt: str) -> str:
        """Generate text using the transformer model"""
        self._load_model()
        
        if self.model is None or self.tokenizer is None:
            return self._generate_template_based(prompt)
        
        try:
            # Tokenize input
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                truncation=True,
                max_length=512
            ).to(self.device)
            
            # Generate
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=config.GENERATION_CONFIG["max_new_tokens"],
                    temperature=config.GENERATION_CONFIG["temperature"],
                    top_k=config.GENERATION_CONFIG["top_k"],
                    top_p=config.GENERATION_CONFIG["top_p"],
                    repetition_penalty=config.GENERATION_CONFIG["repetition_penalty"],
                    do_sample=config.GENERATION_CONFIG["do_sample"],
                    num_beams=config.GENERATION_CONFIG["num_beams"],
                    early_stopping=config.GENERATION_CONFIG["early_stopping"],
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            # Decode output
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract only the generated part (remove prompt)
            if generated_text.startswith(prompt):
                generated_text = generated_text[len(prompt):].strip()
            
            return generated_text
            
        except Exception as e:
            logger.error(f"Error during generation: {e}")
            return self._generate_template_based(prompt)
    
    def _generate_template_based(self, theme: str) -> str:
        """
        Fallback: Generate poetry using templates and mixing existing poems
        This is used when model loading fails or for faster prototyping
        """
        normalized_theme = self._normalize_theme(theme)
        
        # Get theme-specific poems
        if self.language == "bengali":
            poems = [p for p in self.training_data.get("bengali_poems", []) 
                    if p.get("theme") == normalized_theme]
        else:
            poems = [p for p in self.training_data.get("english_poems", []) 
                    if p.get("theme") == normalized_theme]
        
        # If no theme-specific poems, use any poems
        if not poems:
            poems = (self.training_data.get("bengali_poems", []) 
                    if self.language == "bengali" 
                    else self.training_data.get("english_poems", []))
        
        if not poems:
            return self._generate_default_poem(theme)
        
        # Select a random poem and add variation
        base_poem = random.choice(poems)
        poem_text = base_poem["text"]
        
        # Add some variation by mixing lines (simple approach)
        lines = poem_text.strip().split('\n')
        
        # Take first 4 lines or pad if needed
        if len(lines) >= 4:
            result_lines = lines[:4]
        else:
            result_lines = lines + self._generate_additional_lines(
                normalized_theme, 
                4 - len(lines)
            )
        
        return '\n'.join(result_lines)
    
    def _generate_additional_lines(self, theme: str, count: int) -> List[str]:
        """Generate additional lines to complete a 4-line poem"""
        templates_en = [
            f"The spirit of {theme} lives forever strong",
            f"Through {theme} we find our way",
            f"In hearts of heroes, {theme} stays",
            "Victory's song will always play"
        ]
        
        templates_bn = [
            f"বাংলার আকাশে উড়ে স্বাধীনতার পতাকা",
            f"বিজয়ের গান গাই আমরা",
            f"শহীদদের স্মৃতি অমর",
            "জয় বাংলা জয় বাংলাদেশ"
        ]
        
        templates = templates_bn if self.language == "bengali" else templates_en
        return random.sample(templates, min(count, len(templates)))
    
    def _generate_default_poem(self, theme: str) -> str:
        """Generate a basic default poem when no data is available"""
        if self.language == "bengali":
            return f"""বিজয় দিবসের শুভেচ্ছা
{theme} এর মহিমায় ভরা
স্বাধীনতার সূর্য উঠেছে
বাংলাদেশ আমার প্রিয় দেশ"""
        else:
            return f"""On Victory Day we celebrate
The {theme} of our nation great
December's triumph we relate
Freedom's story, never late"""
    
    def _format_as_4_lines(self, text: str) -> str:
        """Ensure output is formatted as 4 lines"""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        # Take first 4 meaningful lines
        result_lines = []
        for line in lines:
            if len(result_lines) >= 4:
                break
            # Skip very short lines (likely formatting artifacts)
            if len(line) >= config.POETRY_FORMAT["min_line_length"]:
                result_lines.append(line[:config.POETRY_FORMAT["max_line_length"]])
        
        # Pad if we don't have 4 lines
        while len(result_lines) < 4:
            result_lines.append(self._generate_additional_lines("victory", 1)[0])
        
        return '\n'.join(result_lines[:4])
    
    def generate(
        self, 
        theme: str, 
        language: Optional[str] = None,
        num_outputs: int = 1
    ) -> List[str]:
        """
        Generate poetry based on a theme
        
        Args:
            theme: The theme for the poem (e.g., "Freedom", "Sacrifice")
            language: Override the default language (optional)
            num_outputs: Number of different poems to generate
            
        Returns:
            List of generated poems (4 lines each)
        """
        if language:
            self.language = language.lower()
        
        logger.info(f"Generating {num_outputs} poem(s) for theme: {theme}")
        
        results = []
        for i in range(num_outputs):
            prompt = self._get_prompt(theme)
            
            # Try model-based generation first, fallback to template
            try:
                generated = self._generate_with_model(prompt)
            except Exception as e:
                logger.warning(f"Model generation failed: {e}, using template")
                generated = self._generate_template_based(theme)
            
            # Format to 4 lines
            formatted = self._format_as_4_lines(generated)
            results.append(formatted)
        
        return results
    
    def get_available_themes(self) -> List[str]:
        """Get list of available themes"""
        return list(config.THEME_ALIASES.keys())
    
    def get_random_slogan(self) -> str:
        """Get a random Victory Day slogan"""
        slogans = self.training_data.get("slogans", [])
        if slogans:
            return random.choice(slogans)
        return "জয় বাংলা! 🇧🇩"


# Example usage
if __name__ == "__main__":
    # Test the generator
    print("=== Bijoy Dibosh Poetry Generator ===\n")
    
    # English test
    print("English Poetry:\n")
    gen_en = BijoyPoetryGenerator(language="english")
    poems = gen_en.generate(theme="Freedom", num_outputs=2)
    for i, poem in enumerate(poems, 1):
        print(f"Poem {i}:")
        print(poem)
        print()
    
    # Bengali test
    print("\nBengali Poetry:\n")
    gen_bn = BijoyPoetryGenerator(language="bengali")
    poems = gen_bn.generate(theme="বিজয়", num_outputs=1)
    for i, poem in enumerate(poems, 1):
        print(f"কবিতা {i}:")
        print(poem)
        print()
    
    # Random slogan
    print("\nRandom Slogan:")
    print(gen_en.get_random_slogan())
