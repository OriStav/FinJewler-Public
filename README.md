# 🪙 FinJewler - Personal Finance Dashboard

> **Comprehensive financial analysis and management toolbox for informed decision-making**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [🚀 Features](#-features)
- [🛠️ Installation](#️-installation)
- [🎯 Available Tools](#-available-tools)
  - [💼 Personal Finance](#-personal-finance)
  - [📈 Investment Analysis](#-investment-analysis)
  - [🔜 Coming Soon](#-coming-soon)
- [📖 Usage](#-usage)
- [🏗️ Project Structure](#️-project-structure)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

---

## 🌟 Overview

**FinJewler** is a powerful Streamlit-based personal finance dashboard that provides comprehensive financial analysis tools to help you make informed decisions about your money. Whether you're planning for retirement, analyzing investments, or managing debt, FinJewler offers intuitive calculators and visualizations to guide your financial journey.

### ✨ Key Highlights

- 🎨 **Beautiful UI**: Modern, responsive interface with gradient designs
- 📊 **Interactive Charts**: Dynamic visualizations for better data understanding
- 🧮 **Advanced Calculators**: Sophisticated financial modeling tools
- 🌙 **Dark/Light Mode**: Customizable theme for comfortable viewing
- 📱 **Mobile Friendly**: Responsive design that works on all devices

---

## 🚀 Features

### 🎯 Core Capabilities

- **Financial Forecasting**: Long-term planning with scenario analysis
- **Investment Analysis**: Correlation studies and portfolio optimization
- **Debt Management**: Mortgage calculations and refinancing analysis
- **Emergency Planning**: Fund calculations and timeline visualization
- **Market Research**: Historical data analysis and trend identification

### 🛡️ Security & Privacy

- **Local Processing**: All calculations run on your device
- **No Data Storage**: Your financial information stays private
- **Open Source**: Transparent codebase for security verification

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FinJewler.git
   cd FinJewler
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

### 📦 Dependencies

The main dependencies include:
- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive visualizations
- `numpy` - Numerical computations

---

## 🎯 Available Tools

### 💼 Personal Finance

#### 🔭 Long Term Forecast
Plan your financial future with advanced forecasting tools and scenario analysis.

**Features:**
- Retirement planning calculators
- Investment growth projections
- Inflation-adjusted calculations
- Multiple scenario modeling

#### 💰 Emergency Fund Calculator
Calculate and visualize your recommended emergency fund timeline.

**Features:**
- Monthly expense analysis
- Fund accumulation planning
- Visual timeline representation
- Risk assessment tools

#### 🏖️ Postponement Consequences
Calculate the cost of postponing investments for specific time periods.

**Features:**
- Opportunity cost analysis
- Compound interest calculations
- Visual impact representation
- Decision-making insights

### 📈 Investment Analysis

#### 🧮 Correlations Analysis
Analyze relationships between different financial instruments and market sectors.

**Features:**
- Correlation matrix visualization
- Heatmap representations
- Statistical significance testing
- Portfolio diversification insights

#### 🏦 Mortgage Calculator
Estimate the cost/profit of mortgages and their impact on your financial plan.

**Features:**
- Amortization schedules
- Refinancing analysis
- Interest rate comparisons
- Equity building projections

### 🔜 Coming Soon

#### 📊 Historical Analysis
Deep dive into historical market data and performance analytics.

#### 📑 ETFs & Leverage
ETF comparison and leveraged investment strategies.

#### 🪙 Trades Analysis
Track trade performance and portfolio optimization tools.

---

## 📖 Usage

### 🚀 Getting Started

1. **Choose a Tool**: Select the appropriate calculator for your financial needs
2. **Input Data**: Use the intuitive forms to enter your financial information
3. **Analyze Results**: Review interactive charts and detailed insights
4. **Make Decisions**: Use the comprehensive analysis to inform your choices

### 💡 Pro Tips

- **Start with Emergency Fund**: Establish your financial foundation first
- **Use Multiple Tools**: Combine different calculators for comprehensive planning
- **Regular Updates**: Revisit your calculations as your situation changes
- **Scenario Planning**: Test different assumptions to prepare for various outcomes

### 🎨 Customization

The application supports both light and dark themes. Toggle between them using the theme selector in the sidebar.

---

## 🏗️ Project Structure

```
FinJewler/
├── 📁 app.py                 # Main Streamlit application
├── 📁 pages/                 # Individual tool pages
│   ├── 🏠 Welcome.py         # Landing page
│   ├── 🔭 Long_Term_Forecast.py
│   ├── 💰 Emergency_Fund.py
│   ├── 🏖️ Postponement_Consequences.py
│   ├── 🧮 Correlations.py
│   ├── 🏦 Mortgage.py
│   └── 🔜 Coming Soon...
├── 📁 methods/               # Utility functions
│   └── vis_utils.py         # Visualization utilities
├── 📁 proj_consts/          # Project constants
│   ├── consts.py
│   ├── paths_base.py
│   └── paths.py
└── 📄 README.md             # This file
```

---

## 🤝 Contributing

We welcome contributions to make FinJewler even better! Here's how you can help:

### 🐛 Reporting Issues

1. Check existing issues to avoid duplicates
2. Provide detailed descriptions and steps to reproduce
3. Include system information and error messages

### 💻 Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<div align="center">

**Made with ❤️ for better financial decision-making**

*Last updated: July 2025*

</div>