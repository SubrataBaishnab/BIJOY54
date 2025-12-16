"""
Flask Web Application for Bijoy Dibosh Poetry Generator
Provides a simple web interface for generating poems
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import logging
from poetry_generator import BijoyPoetryGenerator
import config

# Setup Flask app
app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize generators (one for each language)
generators = {
    'english': None,
    'bengali': None
}


def get_generator(language: str) -> BijoyPoetryGenerator:
    """Get or create a generator for the specified language"""
    if generators[language] is None:
        logger.info(f"Initializing {language} generator")
        generators[language] = BijoyPoetryGenerator(language=language)
    return generators[language]


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def generate_poem():
    """API endpoint to generate a poem"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate input
        theme = data.get('theme', '').strip()
        if not theme:
            return jsonify({'error': 'Theme is required'}), 400
        
        language = data.get('language', 'english').lower()
        if language not in ['english', 'bengali']:
            return jsonify({'error': 'Invalid language'}), 400
        
        num_outputs = int(data.get('num_outputs', 1))
        if num_outputs < 1 or num_outputs > 5:
            return jsonify({'error': 'num_outputs must be between 1 and 5'}), 400
        
        # Generate poems
        generator = get_generator(language)
        poems = generator.generate(
            theme=theme,
            num_outputs=num_outputs
        )
        
        return jsonify({
            'success': True,
            'poems': poems,
            'theme': theme,
            'language': language
        })
        
    except Exception as e:
        logger.error(f"Error generating poem: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/slogan', methods=['GET'])
def get_slogan():
    """API endpoint to get a random slogan"""
    try:
        generator = get_generator('english')
        slogan = generator.get_random_slogan()
        return jsonify({
            'success': True,
            'slogan': slogan
        })
    except Exception as e:
        logger.error(f"Error getting slogan: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/themes', methods=['GET'])
def get_themes():
    """API endpoint to get available themes"""
    try:
        generator = get_generator('english')
        themes = generator.get_available_themes()
        return jsonify({
            'success': True,
            'themes': themes
        })
    except Exception as e:
        logger.error(f"Error getting themes: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    
    print("\n" + "="*60)
    print("  BIJOY DIBOSH POETRY GENERATOR - Web Interface")
    print("="*60)
    print(f"\n  Starting server at http://0.0.0.0:{port}")
    print("  Press Ctrl+C to stop\n")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )
