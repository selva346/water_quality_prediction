# 💧 Water Quality Prediction using Machine Learning

This project is part of the **AICTE Virtual Internship Program**.  
It aims to classify water as **safe** or **unsafe** based on chemical parameter limits using a machine learning model.

---

## 📊 Parameters Used
- NH₄ (Ammonium)
- BSK5 (Biochemical Oxygen Demand)
- Suspended Solids
- O₂ (Dissolved Oxygen)
- NO₃ (Nitrate)
- NO₂ (Nitrite)
- SO₄ (Sulfate)
- PO₄ (Phosphate)
- Cl (Chloride)

---

## 🗓️ Milestone Progress

### ✅ Week 1
- Loaded and cleaned the dataset
- Removed missing values
- Dropped unnecessary columns (`id`, `date`)
- Saved clean dataset for further use

### ✅ Week 2
- Performed **Exploratory Data Analysis (EDA)**
- Created a new column `Quality` based on safe limits
- Plotted:
  - Safe vs Unsafe water sample count
  - Histograms of all features
  - Correlation heatmap
  - Boxplots for outlier detection
- Uploaded Jupyter Notebook (`Week2_EDA_Water_Quality.ipynb`)

---

## ▶️ How to Run
```bash
pip install pandas matplotlib seaborn
python main.py  # for .py file
