<h1>E-Grocery Insights: Decoding Product Diversity and Savings in Online Groceries.</h1>  

<p>Extracted and analyzed 7,197+ products from two leading Bangladeshi e-grocery platforms, with source-wise data preserved and consistently cleaned across both datasets. The processed data was then analyzed and visualized in Tableau, including brand distribution, promotional offer and savings patterns, price variance comparisons, and key cross-source insights.<p>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![License](https://img.shields.io/github/license/yourusername/yourrepo)
![Last commit](https://img.shields.io/github/last-commit/yourusername/yourrepo)

## 📊 Dashboard Preview

<div align="center">
  <img src="doc/Dashboard.png" alt="Dashboard Preview" width="700"/>
</div>

## 📌 About
This is a dynamic web scraping project that collects real-time grocery data from two online sources. The project aims to help consumers identify savings across categories,explore brand availability, analyze offers by product size and price segment, understand brand dominance, and compare price differences between the two sources.  Instead of direct product matching, this project compares market trends and pricing across sources at the sub-category and brand levels.A structured data table is included to provide a clear overview of the data organization.

## The Challenge — More Than Just Scraping


## 📊 Data Overview
![Product Taxonomy](./doc/product_taxonomy.svg)


## ✨ Features
- 📊 Overview of  Products & Brands (Side by Side Bar Graph) : 
- 🥧 Brand Dominance by Product Count (Pie Chart) :
- 📈 Product Volume & Brand Diversity (Line & Bar Chart) :
- 🫧 Top Sub-Categories by Savings & Free Products (Packed Bubble Chart) :
- 🌡️ Offer Distribution by Product Size & Price Segments (Heat Map) :
- 🔵 Price Variance between Regular and All Products across Sources (Circle Chart) :

## ⚙️ Installation

Quick Start
1. Environment Setup (Windows-friendly)

git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
pip install -r requirements.txt
```
   
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install minimal dependencies
pip install -r requirements.txt


```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python main.py
```


## Project Stucture


```text
E-Grocery Insights/
│
├── data/
│   ├── raw/                                          # Step 1: Scraped raw data
│   │   ├── shwapno_data_1.csv
│   │   └── chaldal_data_2.csv
│   │ 
│   ├── interim/                                       # Step 3: Output after cleaning
│   │   ├── combined_data_BrandName_3.csv
│   │   ├── combined_data_BrandName_cleaned_3.csv
│   │   └── df_combined_all_columns_4.csv
│   │
│   └── processed/                                    
│       └── df_final.csv                               # Step-4 Final Output
│
├── notebook/                                             
│   └── data_cleaning.ipynb                            # Step 2: Cleaning data 
│
├── assets/
│   └── visualization                                  # Step-5 : Deshboard Preview
│   
├── requirements.txt                                   # Step-6 : Required libraries
|
├── .gitignore                                         # Step - 7 : Project Configuration
|
└── README.md                                          # Step-8 : Project Documentation
```

## 📜 License
This project is licensed under the MIT License.


## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: youremail@gmail.com
