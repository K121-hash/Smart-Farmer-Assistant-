# Smart Farmer Assistant 🌾

<div align="center">

**An Interactive Agricultural Advisory System**

Helping farmers make informed decisions through intelligent guidance on crops, fertilizers, pest control, planting seasons, weather, and livestock management.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Open Source](https://img.shields.io/badge/Open-Source-green.svg)](https://github.com/K121-hash/Smart-Farmer-Assistant-)

**Author:** Kyauta Ayuba Dabu  
**Code in Place Final Project**

</div>

---

## 🚀 Quick Start - Try It Now!

### Run Online (No Installation Required!)

Click any badge below to run the code in your browser:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/K121-hash/Smart-Farmer-Assistant-/blob/main/examples/demo.ipynb) **Google Colab** - Free interactive environment

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/K121-hash/Smart-Farmer-Assistant-/main?filepath=examples%2Fdemo.ipynb) **Binder** - Free cloud notebook

[![Replit](https://replit.com/badge/github/K121-hash/Smart-Farmer-Assistant-)](https://replit.com/github/K121-hash/Smart-Farmer-Assistant-) **Replit** - Free online IDE

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Scoring System](#scoring-system)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## Overview

**Smart Farmer Assistant** is an interactive Python application that provides agricultural advisory services to farmers. The application guides farmers through key farming decisions with a gamified achievement system that rewards engagement.

### Why Use Smart Farmer Assistant?

- 📚 **Free Agricultural Knowledge** - Access farming expertise without expensive consultants
- 🎮 **Gamified Learning** - Earn achievement badges as you explore farming topics
- 🎯 **Practical Advice** - Get region-specific recommendations for your farm
- 💻 **Easy to Use** - Simple menu-driven interface for all skill levels
- 🌍 **Culturally Relevant** - Recommendations tailored to African farming regions

---

## Features

### 🌱 **Crop Recommendation**
- Region-based crop suggestions (North and South)
- Recommendations include:
  - **North:** Maize, Millet, Sorghum, Groundnut, Wheat, Cotton
  - **South:** Cassava, Yam, Rice, Plantain, Sugarcane, Potato, Onion

### 🌾 **Fertilizer Advice**
- Crop-specific fertilizer recommendations
- Includes application timing and types (NPK formulations)
- Covers 9 major crops with detailed guidance

### 🐛 **Pest Control Tips**
- Common pest identification and management strategies
- Disease monitoring guidance
- Pest-specific recommendations for 9 crops

### 📅 **Planting Season Guide**
- Optimal planting times for each crop
- Regional planting schedules
- Monsoon and seasonal timing information

### ☁️ **Weather-Based Farming Advice**
- Recommendations for different weather conditions (rainy/sunny/dry)
- Irrigation guidance
- Drought-resistant crop suggestions

### 🐄 **Livestock Management**
- Tips for cattle, goats, sheep, and poultry
- Health, housing, and nutrition guidelines
- Disease prevention advice

### 🏆 **Farmer Achievement System**
- Earn points for using each advisory feature
- Track your farmer level:
  - 👨‍🌾 **New Farmer** (0-9 points)
  - 🚜 **Beginner Farmer** (10-29 points)
  - 🌱 **Skilled Farmer** (30-49 points)
  - 🌟 **Master Farmer** (50+ points)

---

## Installation

### Prerequisites

- Python 3.6 or higher
- No external dependencies required!

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/K121-hash/Smart-Farmer-Assistant-.git
   cd Smart-Farmer-Assistant-
   ```

2. **Run the Application**
   ```bash
   python main.py
   ```

That's it! No additional installation needed.

---

## Usage

### Interactive Mode (Recommended)

Simply run the application:

```bash
python main.py
```

You'll see the main menu:

```
=============================================
🌿 SMART FARMER ASSISTANT 🌿
=============================================
1. Crop Recommendation
2. Fertilizer Advice
3. Pest Control Tips
4. Planting Season Guide
5. Weather Advice
6. Livestock Management
7. Farmer Achievement
8. Exit

Choose an option (1-8):
```

### Example Workflow

```
Choose an option (1-8): 1
🌱 Crop Recommendation
Enter your region (north/south): north

Recommended crops:
- Maize
- Millet
- Sorghum
- Groundnut
- Wheat
- Cotton

(You gain 10 points!)

Choose an option (1-8): 2
🌾 Fertilizer Advice
Enter crop name: maize

Recommendation: Apply NPK 15-15-15 during early growth.

(You gain 10 points!)
```

---

## How It Works

### Menu System

The application presents an interactive menu with 8 options:

| Option | Function | Points |
|--------|----------|--------|
| 1 | Get crop recommendations by region | +10 |
| 2 | Get fertilizer advice for a crop | +10 |
| 3 | Get pest control tips for a crop | +10 |
| 4 | Get planting season guide | +10 |
| 5 | Get weather-based farming advice | +10 |
| 6 | Get livestock management tips | +10 |
| 7 | View your farmer achievement level | N/A |
| 8 | Exit the application | N/A |

### Scoring System

Each advisory feature interaction adds **10 points** to your farmer score:
- Visit 5 features = 50 points = 🌟 Master Farmer
- Encourages exploration of all features
- Track your learning progress

---

## Examples

### Example 1: Get Crop Recommendations

```python
Choose an option (1-8): 1
🌱 Crop Recommendation
Enter your region (north/south): south

Recommended crops:
- Cassava
- Yam
- Rice
- Plantain
- Sugarcane
- Potato
- Onion
```

### Example 2: Get Fertilizer Advice

```python
Choose an option (1-8): 2
🌾 Fertilizer Advice
Enter crop name: rice

Recommendation: Use NPK and Urea for better yield.
```

### Example 3: Check Weather Advice

```python
Choose an option (1-8): 5
☁️ Weather-Based Farming Advice
Enter current weather (rainy/sunny/dry): rainy

✅ Good time for planting maize, rice, vegetables, and sugarcane.
```

### Example 4: Livestock Management

```python
Choose an option (1-8): 6
🐄 Livestock Management Tips
Enter livestock (cattle/goat/sheep/poultry): cattle

Tip: Provide adequate water, vaccination, and quality feed.
```

### Example 5: View Achievement

```python
Choose an option (1-8): 7
🏆 Farmer Achievement Status
Your Score: 50
🌟 Master Farmer
```

---

## Scoring System

### Achievement Levels

```
Points    Level              Badge  Description
─────────────────────────────────────────────────
0-9       New Farmer         👨‍🌾   Just starting your farming journey
10-29     Beginner Farmer    🚜    Learning the basics
30-49     Skilled Farmer     🌱    Building expertise
50+       Master Farmer      🌟    Mastered all features
```

**How to Reach Each Level:**
- **New Farmer**: Start the application
- **Beginner Farmer**: Use 1-2 features
- **Skilled Farmer**: Use 3-4 features
- **Master Farmer**: Use 5 or more features

---

## Project Structure

```
Smart-Farmer-Assistant/
├── main.py                      # Main application (core program)
├── examples/
│   ├── demo.ipynb              # Interactive Jupyter notebook demo
│   └── README.md               # Examples documentation
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore file
```

---

## Technology Stack

- **Language:** Python 3.6+
- **Type:** Interactive CLI Application
- **Dependencies:** None (pure Python)
- **Platform:** Cross-platform (Windows, macOS, Linux)

---

## Contributing

Contributions are welcome! Here's how you can help:

### Report Issues
- Found a bug? [Open an issue](https://github.com/K121-hash/Smart-Farmer-Assistant-/issues)
- Have a feature request? [Create a discussion](https://github.com/K121-hash/Smart-Farmer-Assistant-/discussions)

### Improve the Code
1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/Smart-Farmer-Assistant-.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Add new crops, pests, or fertilizers
   - Improve existing advice
   - Add new features
   - Fix bugs

4. **Test your changes**
   ```bash
   python main.py
   ```

5. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   git push origin feature/your-feature-name
   ```

6. **Submit a pull request**

### Areas for Contribution

- 🌍 **Expand regional data:** Add more regions and crops
- 🌾 **Add new crops:** More fertilizer and pest control data
- 🔧 **Enhancement features:** 
  - Save user scores
  - Export recommendations
  - Multi-language support
  - Web interface
- 📚 **Documentation:** Improve guides and examples
- 🧪 **Testing:** Add unit tests

---

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use for personal or commercial projects
- ✅ Modify and distribute
- ✅ Include in other projects
- ✅ Sublicense

---

## Support & Contact

### Get Help

- **Issues**: [GitHub Issues](https://github.com/K121-hash/Smart-Farmer-Assistant-/issues)
- **Discussions**: [GitHub Discussions](https://github.com/K121-hash/Smart-Farmer-Assistant-/discussions)
- **Author**: [Kyauta Ayuba Dabu](https://github.com/K121-hash)

### Feedback

We'd love to hear from you!
- 💬 Share your experience using the app
- 🐛 Report any bugs or issues
- 💡 Suggest new features
- 📝 Improve documentation

---

## Changelog

### Version 1.0.0
- Initial release
- 6 main advisory features
- Gamified achievement system
- Support for 9 major crops
- Livestock management tips
- Weather-based farming advice

---

## FAQ

### Q: Do I need to install any dependencies?
**A:** No! Smart Farmer Assistant is built with pure Python and requires no external libraries.

### Q: Can I use this on my phone?
**A:** You can use it on a phone with Python installed, or run it online using Google Colab or Replit (see Quick Start section).

### Q: How often is the advice updated?
**A:** The advice is based on established agricultural practices. Updates are made through community contributions.

### Q: Can I add my own crops or regions?
**A:** Yes! You can modify the dictionaries in `main.py` to add your own crops, pests, and regions. See the Contributing section.

### Q: Is this suitable for my country?
**A:** The application is designed with African farming regions in mind. You can customize it for your specific region by modifying the data.

---

## Disclaimer

This application provides advisory recommendations based on general agricultural best practices. While every effort is made to ensure accuracy:

⚠️ **Always:**
- Verify recommendations with local agricultural experts
- Consider local soil testing results
- Consult extension services for region-specific guidance
- Adapt suggestions based on your specific circumstances

**For major farming decisions, consult with professional agricultural consultants.**

---

## Acknowledgments

- **Author:** Kyauta Ayuba Dabu
- **Project Type:** Code in Place Final Project
- **Inspired by:** Agricultural extension services and farming communities

---

<div align="center">

**Happy Farming! 🌾🚜**

*Making agriculture smarter, one recommendation at a time.*

[⬆ Back to Top](#smart-farmer-assistant-)

</div>
