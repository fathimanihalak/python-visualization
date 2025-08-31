# python-visualization
Internship project for data preprocessing & visualization on B2B datasets using Python (Pandas, Matplotlib, Seaborn).
## 📂 Project Details

### 🔹 Onzitr (B2B Complaint Dashboard)
The objective of this project was to build a dashboard that could provide insights into **customer complaints**, enabling the business to reduce response times and improve customer satisfaction.  

**Workflow:**
- Fetched customer complaint data from the Onzitr API using Python (`requests`).
- Normalized nested JSON data into a tabular format using `pandas.json_normalize`.
- Cleaned and stored the data in CSV format for analysis.
- Created a **Power BI dashboard** visualizing:
  - Types of complaints
  - Resolution times
  - Complaint status (open/closed)
- Added interactive features (filters, slicers, tooltips) to enhance usability.

**Tools Used:** Python (`requests`, `pandas`, `json`), Power BI, REST API

---

### 🔹 Practicing Dataset (Alpha Vantage API)
- Extracted historical options data from **Alpha Vantage API** using API key authentication.
- Processed JSON responses with Python `requests` → converted to DataFrame → saved as CSV.
- Prepared structured datasets for visualization and further analysis.

---

### 🔹 B2B Data Visualization Using Python
The objective was to **analyze B2B client transaction data** to identify business insights and support decision-making.  

**Steps Followed:**
1. **Data Exploration:** Imported CSV data into `pandas`, checked schema using `.info()`, `.head()`, `.describe()`.
2. **Preprocessing:**  
   - Handled missing values (imputation).  
   - Removed duplicates & standardized categorical fields.  
   - Visualized outliers using boxplots, applied domain logic to handle them.
3. **Analysis:**  
   - Aggregated revenue per customer, transaction frequency, and purchase categories.  
   - Segmented clients into high-value vs. low-value.  
   - Derived metrics like average order value and seasonal purchase trends.
4. **Visualizations (Matplotlib & Seaborn):**  
   - Line plots → monthly/quarterly revenue trends  
   - Histograms → purchase value distribution  
   - Pie charts → client distribution by region  
   - Heatmaps → correlation between revenue & transaction frequency  
   - Bar plots → transaction counts by product category/time period

**Key Insights:**
- Identified top-performing clients and underperforming regions.  
- Found seasonal spikes in purchases.  
- Suggested inventory optimization during peak demand.  
- Recommended focusing marketing on loyal high-value clients.

**Tools Used:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook  

**Outcome:**  
This project strengthened my **EDA (Exploratory Data Analysis)** skills and demonstrated how **data visualization simplifies complex B2B datasets into actionable insights** for business strategy.

---
              

