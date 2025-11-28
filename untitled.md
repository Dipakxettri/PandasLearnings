# Rulebook :
<!-- # STEP 1 — Inspect the Dataset (Look Before You Clean) : -->

## Step 1 : Inspect the Dataset (Look Before You Clean)

###  df.head()
<!-- =>
# Shows the first few rows. Helps you see obvious problems:
# weird text
# mixed formats
# missing values
# wrong data types -->


### df.info()
<!-- =>
# Shows:
# column names
# data types (object, int64, float64, datetime64, etc.)
# how many missing values each column has
# You’ll often see mistakes like:
# numbers stored as strings
# dates stored as objects
# phone numbers as floats
# emails with weird characters -->


### df.describe(include='all')
<!-- 
👉 Shows:
min/max
unique values
top frequent values
distribution
This helps you find:
outliers (age = 400 🤡)
invalid entries
unexpected categories -->

### df.isna().sum()
<!-- Shows how much data is missing per column.
Very important for deciding:
Should you fill missing values?
Should you drop rows?
Should you replace them? -->

## Step 2 - Understand Data Types (Correct Types = Power)
<!-- How to check  -->
<!-- df.dtypes
How to fix numbers:
python
Copy code
df["age"] = pd.to_numeric(df["age"], errors="coerce")
How to fix dates:
python
Copy code
df["date"] = pd.to_datetime(df["date"], errors="coerce")
👉 Always fix data types early
because later operations will break if types are wrong. -->




