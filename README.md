# 🛒 E-Grocery Insights: Decoding Product Diversity and Savings in Online Groceries

Extracted and analyzed **7,197 product listings** from **Chaldal** and **Shwapno** — two leading Bangladeshi e-grocery platforms — uncovering brand distribution, 
promotional savings, offer patterns, and price variance through data-driven analysis and Tableau visualizations.

![Python](https://img.shields.io/badge/Python-3.13.1-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.41.0x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0.1-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

<br>

## 📊 Dashboard Preview
 **[View Interactive Dashboard](https://public.tableau.com/app/profile/bithi.nath/viz/visualization_1_17772762990980/Dashboard)**
<br>
<div align="center">
  <img src="doc/Dashboard.png" alt="Dashboard Preview" width="1100"/>
</div>

## 📌 About

Bangladesh's e-grocery sector is experiencing rapid growth, driven by factors such as bulk purchase discounts, exclusive product offers, free delivery above certain order thresholds, and the convenience of time-saving shopping. These incentives are reshaping how urban consumers purchase daily essentials. However, with multiple platforms offering varying prices, brands, and deals, consumers often struggle to identify where they can save the most. This project bridges that gap by scraping real-time grocery data from two major e-grocery sources in Bangladesh, enabling a data-driven comparison at the sub-category and brand level.
Rather than direct product matching, this project focuses on market-level trends to uncover:
- Which platform and product sub-categories offer the most savings
- How brand availability differs across platforms
- How offers vary by product size and price segment
- Which top 10 brands dominate by product listing on each platform
- Which platform offers lower prices across all products and regularly purchased items of common brands, analyzed by price segment and category

### 🔍 Scope
- Platforms covered: [Chaldal](https://chaldal.com/) and [Shwapno](https://www.shwapno.com/)
- Data collection method: **Dynamic web scraping** using Selenium
- Total product listings: **7,197** (Chaldal: 3,337 | Shwapno: 3,860)
- Total unique brands identified: **~700**
- Data collected: **Late March 2026**

### ⚠️ Limitations
- **~890 duplicate** entries, including a few null values, were removed during cleaning.
- **~350 products** appearing in multiple sub-categories were cleaned by retaining only the listing under their most relevant sub-category.
- The same product may appear with different prices or unit sizes, as pricing and packaging vary across platforms.
- Brand names were extracted from product titles using keyword frequency analysis, followed by manual correction — resulting in **~700 unique brands** identified.
- **~4,000 products** had generic units (pcs, each, pack, etc.), so an `Extra_info` column was extracted from titles to determine actual unit, `offer_status`, `Total_savings`, `Actual_unit_price`, and `Market_price`.
- Out-of-stock status on Chaldal could not be scraped, so such few products remain in the dataset and may slightly bias the results.

<br>

## 📊 Data Overview

<div align="center">
  <h2>Product Taxonomy</h2>
  <h3>Section → Category → Sub-Category</h3>
  <img src="./doc/product_taxonomy.svg" width="800" alt="Product Taxonomy"/>
</div>

<br>

## ✨ Features

- 📊 **Overview of Products & Brands (Side by Side Bar Graph) :** Compares total product listings and unique brand counts across Chaldal and Shwapno by section, category, and sub-category.
  
- 🥧 **Brand Dominance by Product Share Chart (Pie chart) :** Shows which top 10 brands hold the largest share of products within each category per platform.
  
- 📈 **Product Volume & Brand Diversity (Line & Bar Chart) :** Visualizes the relationship between number of products and brand variety across section, category and sub-categories.
  
- 🫧 **Top Sub-Categories by Savings & Free Products (Packed Bubble Chart) :** Highlights which sub-categories have the highest concentration of total savings percentage,  and where free products are most available across both platforms.
  
- 🌡️ **Offer Distribution by Product Size & Price Segments (Heat Map) :** Reveals which size and price segment combinations have the highest offer concentration on each
   platform.
  
- 🔵 **Price Variance between Regular and All Products across Sources (Circle Chart) :** Compares price differences between all products and regularly purchased food items,
  focusing on common brands within the same sub-category, segmented by price range across both platforms.

<br>

## ⚙️ Quick Start

1. 🔽 Clone Repository
   
   ```
     git clone https://github.com/bithiNath/E-Grocery-Insights-BD.git
     cd E-Grocery-Insights-BD
   ```

2. 🐍 Setup Environment (Windows-friendly)
   
   ```
    python -m venv venv
    venv\Scripts\activate
   ```
   
3. 📦 Install minimal dependencies
   
   ```
    pip install -r requirements.txt
   ```
   
4. ▶️ Run Data collection Script
   
    ```
      python src/data_Scraping_chaldal.py
      python src/data_scraping_shwapno.py
    ```
   
5. 🧹 Run Data Cleaning (Notebook)
    
    ```
      data_cleaning.ipynb
    ```
   
 6. 📂 Data Information
    
    ```
      - Raw data is excluded (.gitignore)
      - Available required data: `data/interim/combined_data_BrandName_cleaned_3.csv`
      - Generate other data using scripts and notebook
    ```

 7. 📊 Open Tableau Dashboard : [Click here for Tableau public view](https://public.tableau.com/app/profile/bithi.nath/viz/visualization_1_17772762990980/Dashboard)

<br>

## Project Stucture

```text
E-Grocery Insights/
│
├── data/
│   ├── raw/                                           # Step 1: Scraped raw data
│   │   ├── shwapno_data_1.csv
│   │   └── chaldal_data_2.csv
│   │
│   ├── interim/  
|   |   ├── combined_data_BrandName_3.csv              # Step 3: Generated after cleaning, used for brand name identification
│   │   └── combined_data_BrandName_cleaned_3.csv      # Step 4: Manually reviewed and used to extract brand names
│   │   
│   └── processed/
│       └── df_final.csv                               # Step-5 Final Output
│
├── notebook/
│   └── data_cleaning.ipynb                            # Step 2: Cleaning data
│
├── assets/
│   └── visualization                                  # Step-6 : Deshboard Preview
│
├── requirements.txt                                   # Step-7 : Required libraries
|
├── .gitignore                                         # Step - 8 : Project Configuration
|
└── README.md                                          # Step-9 : Project Documentation
```

<br>

## 🎯 Future Goals
- Incorporate statistical analysis on the existing dataset
- Automate scraping with scheduled runs to track price changes over time
- Conduct seasonal analysis (e.g., Ramadan, Eid effects) and visualize through Power BI
- Expand to more e-grocery platforms for broader market comparison


## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.


## ⚠️ Disclaimer
This project is created for educational purposes to practice data analysis and visualization. The data used was collected from publicly available sources. This project does not aim to harm, misuse, or violate the terms of any platform.


## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.


## 📬 Contact

- **GitHub:** [@bithiNath](https://github.com/bithiNath)
- **LinkedIn:** [Bithi Nath](https://linkedin.com/in/bithinath)

---

<br>

<p align="center">Developed by <a href="https://github.com/bithiNath">@bithiNath</a> ⚡</p>
