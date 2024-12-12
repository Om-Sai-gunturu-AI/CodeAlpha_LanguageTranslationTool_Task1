# CodeAlpha_LanguageTranslationTool_Task1

# Language Translation Tool

## Description
This project is a simple language translation tool built in Python. It allows users to translate text from one language to another using Google's pre-trained machine translation models via the `googletrans` library.

## Features
- Supports multiple languages including English, Spanish, French, German, Chinese, and Hindi.
- Validates user input for language selection to ensure accurate translations.
- Provides an interactive command-line interface for translation.

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - `googletrans==4.0.0-rc1`

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python translator.py
   ```
2. Follow the on-screen instructions:
   - Enter the text you want to translate.
   - Select the target language by its name (e.g., `French`, `Hindi`).

Example:
```
Available Languages:
English: en
Spanish: es
French: fr
German: de
Chinese: zh-cn
Hindi: hi

Enter the text you want to translate: Hello, how are you?
Enter the target language (e.g., English, Spanish): French
Translated Text: Bonjour, comment ça va ?
```

## Supported Languages
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Chinese (zh-cn)
- Hindi (hi)

## Notes
- Ensure you have a stable internet connection as the translation relies on an external API.
- If you encounter any issues, ensure you are using `googletrans==4.0.0-rc1` as it is the recommended version for this project.


