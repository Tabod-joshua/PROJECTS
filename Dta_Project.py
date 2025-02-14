#!/usr/bin/env python
# coding: utf-8

# In[145]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **Checking for Null Values**

# In[157]:


set=pd.read_csv(r"C:\Users\JAY\Documents\sales_data_17000.csv.xls")
df=pd.DataFrame(set)
df.isnull().sum()


# **Checking for Value Inconsistent Columns**

# In[5]:


set=pd.read_csv(r"C:\Users\JAY\Documents\sales_data_17000.csv.xls")
df=pd.DataFrame(set)
obj_col=df.select_dtypes(include={"object"}).columns
for col in obj_col:
    print(f"the unique values for '{col}' are:",df[col].unique(),"\n")


# **Summary Statistics**

# In[7]:


df.describe()
df.info()


# **Insights on Customer Demographics and Purchasing Behavior**

# In[9]:


gender_counts=df['Gender'].value_counts()
plt.bar(gender_counts.index,gender_counts.values,color=["orange","blue","grey"])
plt.xlabel("Category")
plt.ylabel("Counts")
plt.title("Gender Distribution")
plt.show()
print(df['Gender'].value_counts())


# In[10]:


prod_plot=df.groupby(["Product Category","Gender"]).size().unstack()
prod_plot.plot(kind="bar")
plt.ylabel("Counts")
plt.legend(bbox_to_anchor=(1,1))
plt.title("Gender Category Vs Product Category")


# In[11]:


prod_plot=df["Product Category"].value_counts()
plt.bar(prod_plot.index,prod_plot.values)
plt.xlabel("Categories")
plt.ylabel("counts")
plt.xticks(rotation=45)
plt.title("Product Category Distribution")


# In[12]:


sns.boxplot(x="Product Category", y="Price per Unit",hue="Product Category",palette="muted",data=df)
plt.xticks(rotation=45)
plt.title(" Price Per Unit Vs Product Category")


# **TIME SERIES ANALISIS**

# In[312]:


df['Revenue']=df["Price per Unit"]*df["Quantity"]
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year']=df['Date'].dt.year
total_rev=df.groupby('Year')['Revenue'].mean()
plt.plot(total_rev.index,total_rev.values)
plt.ylabel("Revenue")
plt.xlabel("Year")
plt.title("TRENDS IN TOTAL REVENUE WITH RESPECT TO YEARS")
plt.xticks(rotation=45)
plt.show()


# In[314]:


get_ipython().run_line_magic('matplotlib', 'inline')
df['month']=df['Date'].dt.month
total_sales_months=df.groupby(['month'])['Revenue'].mean()
plt.plot(total_sales_months.index,total_sales_months.values)
plt.xticks(total_sales_months.index)
plt.title("TRENDS IN TOTAL SALES WITH RESPECT TO MONTHS")
plt.xlabel('Months')
plt.ylabel('Total Sales Value')
plt.show()


# In[298]:


df['Week']=df['Date'].dt.isocalendar().week
week_ticks = [1, 5, 10, 15, 20, 25, 30,35,40,45,50]
total_sales_Weeks=df.groupby(['Week'])['Total Sale Value'].mean()
plt.figure(figsize=(10,6))
plt.plot(total_sales_Weeks.index,total_sales_Weeks.values)
plt.title("TRENDS IN TOTAL SALES WITH RESPECT TO WEEKS")
plt.xlabel('Weeks')
plt.ylabel('Total Sales Value')
plt.xticks(week_ticks) 
plt.show()


# In[302]:


df['Days']=df['Date'].dt.isocalendar().day
total_sales_Weeks=df.groupby(['Days'])['Total Sale Value'].mean()
plt.plot(total_sales_Weeks.index,total_sales_Weeks.values)
plt.title("TRENDS IN TOTAL SALES WITH RESPECT TO WEEKS")
plt.xlabel('Weeks')
plt.ylabel('Total Sales Value')
plt.show()


# In[360]:


revenue_region = df.groupby("Region")["Revenue"].mean()
explode = [0.1] * len(revenue_region)
plt.pie(revenue_region.values, labels=revenue_region.index, autopct='%1.1f%%', startangle=140,explode=explode)
plt.title("Average Revenue Distribution by Region")
plt.show()


# In[344]:


print(revenue_region.dtypes)
revenue_region.isnull().sum

