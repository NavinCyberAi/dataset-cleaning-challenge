# dataset-cleaning-challenge﻿ ﻿ ﻿ 

I cleaned and prepared 6 raw datasets containing purchase, sales, and inventory data from 2016 and December 2017 for analysis.

# Files Processed:

1. 2017Purchase Prices Dec.csv - Purchase prices for December 2017

2. BegInvFINAL12312016.csv - Beginning inventory (2016)

3. EndInvFINAL12312016.csv - Ending inventory (2016)

4. Invoice Purchases12312016.csv - Invoice purchases (2016)

5. Purchases FINAL12312016.csv Purchases (2016)

6. SalesFINAL12312016.csv - Sales (2016)

# Cleaning Process

   1. Data Loading & Initial Inspection

           Loaded all datasets using Pandas Examined structure, data types, and initial data quality issues.

  2. Common Problems Identified

           Missing values (empty cells) across multiple columns Duplicate records in several datasets Inconsistent formatting in date and numeric fields.

3. Data Cleaning Applied

Removed all duplicate rows from each dataset

# Handled missing values:

           Numeric fields → Replaced with 0 Text fields → Replaced with "Unknown" Standardized date formats across all files Ensured consistent column naming conventions.

# Results

          All datasets are now clean, consistent, and ready for analysis with: No duplicate records Complete data (no missing values) Uniform formatting standards

