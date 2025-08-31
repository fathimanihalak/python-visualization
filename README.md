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

---<img width="978" height="559" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/bc8604a4-97b2-40a0-8215-deb3237eeb38" />


<img width="862" height="494" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/7de71c25-7165-4d81-8ad0-c69817d49f02" />


<img width="1040" height="578" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/74833958-6d09-4b5f-8a54-9c56e2b5c804" />
<img width="924" height="542" alt="Screenshot (52)" src="https://github.com/user-attachments/assets/24478a7c-232b-4616-a513-1d1a424246bd" />
<img width="1163" height="564" alt="Screenshot (53)" src="https://github.com/user-attachments/assets/3c04a3f6-1cc5-4b23-815e-b5201f90427a" />
