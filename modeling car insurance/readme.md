# On the Road Car Insurance Claim Prediction

## Project Overview
The goal is to identify the **single best feature** for predicting whether a customer will file a claim during the insurance policy period.

The focus is on building a **simple, interpretable model** using just one feature that gives the best prediction accuracy.

---

## Dataset

The dataset is provided in `car_insurance.csv` and includes customer demographic, vehicle, and driving history details.

### Column Descriptions:

| Column              | Description |
|---------------------|-------------|
| `id`                | Unique client identifier |
| `age`               | Client's age group: <br> 0: 16–25, 1: 26–39, 2: 40–64, 3: 65+ |
| `gender`            | 0: Female, 1: Male |
| `driving_experience`| Driving experience in years: <br> 0: 0–9, 1: 10–19, 2: 20–29, 3: 30+ |
| `education`         | Education level: <br> 0: No education, 1: High school, 2: University |
| `income`            | Income level: <br> 0: Poverty, 1: Working class, 2: Middle class, 3: Upper class |
| `credit_score`      | Credit score (float between 0 and 1) |
| `vehicle_ownership` | 0: Does not own vehicle, 1: Owns vehicle |
| `vehcile_year`      | 0: Before 2015, 1: 2015 or later |
| `married`           | 0: Not married, 1: Married |
| `children`          | Number of children |
| `postal_code`       | Client’s postal code |
| `annual_mileage`    | Annual mileage in miles |
| `vehicle_type`      | 0: Sedan, 1: Sports car |
| `speeding_violations`| Number of speeding violations |
| `duis`              | Number of DUI offenses |
| `past_accidents`    | Number of past accidents |
| `outcome`           | 0: No claim, 1: Made a claim (Target Variable) |

---

## Objective

- Evaluate models built using **one feature at a time**.
- Select the feature that gives the **highest prediction accuracy**.
- Deliver a simple and explainable model using that feature.

---

## Requirements

- Python 3.x
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `statsmodels`

Install them using:

```bash
pip install numpy pandas statsmodels
