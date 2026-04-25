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


## 📊 Data Overview

<table>
  <thead>
    <tr>
      <th>Section</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Chaldal</th>
      <th>Shwapno</th>
      <th>Grand Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="17">Food Items</td>
      <td rowspan="7">Beverages & Instant Food</td>
      <td>Beverages</td>
      <td>191</td><td>306</td><td>497</td>
    </tr>
    <tr><td>Breakfast</td><td>71</td><td>73</td><td>144</td></tr>
    <tr><td>Canned Food</td><td>29</td><td>24</td><td>53</td></tr>
    <tr><td>Chocolates & Icecream</td><td>82</td><td>157</td><td>239</td></tr>
    <tr><td>Frozen Snacks</td><td>84</td><td>87</td><td>171</td></tr>
    <tr><td>Sauces & Pickles</td><td>79</td><td>90</td><td>169</td></tr>
    <tr><td>Snacks</td><td>338</td><td>529</td><td>867</td></tr>
    <tr>
      <td rowspan="6">Cooking Essentials & Staples</td>
      <td>Baking & Flour</td><td>111</td><td>79</td><td>190</td>
    </tr>
    <tr><td>Lentils & Pulses</td><td>24</td><td>33</td><td>57</td></tr>
    <tr><td>Oil</td><td>56</td><td>60</td><td>116</td></tr>
    <tr><td>Rice</td><td>41</td><td>44</td><td>85</td></tr>
    <tr><td>Salt & Sugar</td><td>17</td><td>24</td><td>41</td></tr>
    <tr><td>Spices & Ingredients</td><td>160</td><td>278</td><td>438</td></tr>
    <tr>
      <td rowspan="4">Fresh & Perishables</td>
      <td>Dairy & Eggs</td><td>113</td><td>146</td><td>259</td>
    </tr>
    <tr><td>Fruits</td><td>25</td><td>16</td><td>41</td></tr>
    <tr><td>Meat & Fish</td><td>122</td><td>91</td><td>213</td></tr>
    <tr><td>Vegetables</td><td>77</td><td>69</td><td>146</td></tr>
    <tr>
      <td rowspan="5">Non-Food Items</td>
      <td rowspan="3">Home & Lifestyle</td>
      <td>Cleaning Supplies</td><td>304</td><td>150</td><td>454</td>
    </tr>
    <tr><td>Home & Kitchen</td><td>157</td><td>46</td><td>203</td></tr>
    <tr><td>Stationeries</td><td>165</td><td>23</td><td>188</td></tr>
    <tr>
      <td rowspan="2">Personal & Baby Care</td>
      <td>Baby Care</td><td>255</td><td>135</td><td>390</td>
    </tr>
    <tr><td>Personal Care</td><td>836</td><td>1,400</td><td>2,236</td></tr>
    <tr>
      <td colspan="3"><strong>Grand Total</strong></td>
      <td><strong>3,337</strong></td>
      <td><strong>3,860</strong></td>
      <td><strong>7,197</strong></td>
    </tr>
  </tbody>
</table>


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


## 📜 License
This project is licensed under the MIT License.


## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: youremail@gmail.com
