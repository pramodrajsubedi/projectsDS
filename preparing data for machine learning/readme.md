# Optimizing Customer Data Storage

## Overview
This dataset, `customer_train.csv`, contains anonymized student information and indicates whether a student is looking for a new job. Efficient storage is crucial to enable fast model predictions without reducing dataset size.

## Dataset Description
The dataset contains the following columns:

| Column                 | Description |
|------------------------|-------------|
| `student_id`          | Unique ID for each student. |
| `city`                | Code for the city where the student lives. |
| `city_development_index` | Scaled development index for the city. |
| `gender`              | The student's gender. |
| `relevant_experience` | Indicator of relevant work experience. |
| `enrolled_university` | Type of university course enrolled in (if any). |
| `education_level`     | Student's education level. |
| `major_discipline`    | Educational discipline of the student. |
| `experience`         | Total work experience (in years). |
| `company_size`       | Number of employees at the student's current employer. |
| `company_type`       | Type of company employing the student. |
| `last_new_job`       | Number of years since the student's last job. |
| `training_hours`     | Number of training hours completed. |
| `job_change`         | Indicator of whether the student is looking for a new job (1) or not (0). |

## Optimization Strategy
To improve storage efficiency while preserving data integrity, the following strategies are applied:

### 1. **Data Type Optimization**
- Categorical columns are converted to optimized data types.
- Integer and float columns use reduced precision where applicable.

### 2. **Efficient File Format**
- The dataset is stored in a format that minimizes storage size and improves performance.

### 3. **Handling Missing Data**
- Missing values are managed appropriately to maintain data consistency.

## Benefits of Optimization
- **Reduced Storage**: More efficient data storage format.
- **Faster Read/Write**: Improved data access speeds.
- **Better Scalability**: Optimized for large-scale processing.

---
### Author
[Pramod Subedi]

### License
This project is open-source and available for educational and analytical purposes.

