# New York City Airbnb Market Analysis

## Overview

Welcome to New York City, one of the most-visited cities in the world. With a high demand for temporary lodging, Airbnb provides a vast number of listings ranging from short stays of a few nights to long-term stays of several months. This project aims to analyze the New York Airbnb market by integrating data from multiple file types such as CSV, TSV, and Excel files.

## Data Sources

The analysis is based on three datasets containing information about Airbnb listings in 2019. These files include details on pricing, locations, room types, and review histories.

### 1. **Airbnb Price Data (CSV)**

**File Path:** `data/airbnb_price.csv`

This CSV file provides details on Airbnb listing prices and locations.

- **listing\_id**: Unique identifier of the listing
- **price**: Nightly listing price in USD
- **nbhood\_full**: Name of the borough and neighborhood where the listing is located

### 2. **Airbnb Room Type Data (Excel)**

**File Path:** `data/airbnb_room_type.xlsx`

This Excel file contains descriptions and room type classifications for each Airbnb listing.

- **listing\_id**: Unique identifier of the listing
- **description**: Listing description
- **room\_type**: Room type category (Shared Room, Private Room, Entire Home/Apartment)

### 3. **Airbnb Last Review Data (TSV)**

**File Path:** `data/airbnb_last_review.tsv`

This TSV file includes information on the host name and the date of the last review for each listing.

- **listing\_id**: Unique identifier of the listing
- **host\_name**: Name of the listing host
- **last\_review**: Date of the most recent review

## Objective

The primary goal of this project is to analyze trends in the Airbnb market in New York City, focusing on pricing, room types, and review activity. By merging these datasets, we can gain insights into pricing patterns, preferred room types, and how often listings receive reviews.

## Getting Started

1. Load the data from the CSV, TSV, and Excel files.
2. Merge the datasets using the `listing_id` as a common key.
3. Perform exploratory data analysis (EDA) to identify key insights.
4. Visualize trends and patterns in pricing, room availability, and reviews.

## Tools & Libraries

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Jupyter Notebook or any Python IDE

## Expected Outcomes

- Identify pricing trends across different boroughs and neighborhoods.
- Determine the most common room types listed on Airbnb.
- Analyze review patterns and host activity over time.

---

### Contributors

[Pramod Subedi]

### License

This project is open-source and available for educational and analytical purposes.

