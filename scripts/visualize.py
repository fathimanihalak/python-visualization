import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_revenue_trends(df):
    monthly_sales = df.groupby(pd.Grouper(key="Date", freq="M"))["Revenue"].sum()
    plt.figure(figsize=(10,5))
    plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
    plt.title("Monthly Revenue Trends")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()

def plot_customer_segments(df):
    segments = df.groupby("CustomerID")["Revenue"].sum()
    plt.figure(figsize=(8,6))
    sns.histplot(segments, bins=20, kde=True)
    plt.title("Revenue Distribution per Customer")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.show()

def correlation_heatmap(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("../data/sample_b2b.csv", parse_dates=["Date"])
    plot_revenue_trends(df)
    plot_customer_segments(df)
    correlation_heatmap(df)
