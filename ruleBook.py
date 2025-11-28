# Rulebook :
# STEP 1 — Inspect the Dataset (Look Before You Clean) :
# df.head()
# = >
# Shows the first few rows. Helps you see obvious problems:
# weird text
# mixed formats
# missing values
# wrong data types


 df.info()
# =>
# Shows:
# column names
# data types (object, int64, float64, datetime64, etc.)
# how many missing values each column has
# You’ll often see mistakes like:
# numbers stored as strings
# dates stored as objects
# phone numbers as floats
# emails with weird characters


