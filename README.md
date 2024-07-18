#** Customer_Churn_Analysis_and_Prediction**


**_Objective_**: To retain customers who are likely to churn by accurately identifying their behavior


**_Dataset Link_**: https://www.kaggle.com/datasets/blastchar/telco-customer-churn


**_Features Overview_**:

customerID: Unique customer identifier

gender: Customer's gender

SeniorCitizen: Indicates if the customer is 65 or older

Partner: Indicates if the customer has a partner

Dependents: Indicates if the customer lives with any dependents

tenure: Number of months with the company

PhoneService: Indicates if the customer subscribes to home phone service with the company

MultipleLines: Indicates if the customer subscribes to multiple telephone lines with the company

InternetService: Indicates if the customer subscribes to Internet service with the company

OnlineSecurity: Indicates if the customer subscribes to an additional online security service provided by the company

OnlineBackup: Indicates if the customer subscribes to an additional online backup service provided by the company

DeviceProtection: Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company

TechSupport: Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times

StreamingTV: Indicates if the customer uses their Internet service to stream television programs from a third-party provider

StreamingMovies: Indicates if the customer uses their Internet service to stream movies from a third-party provider

Contract: Indicates the customer’s current contract type

PaperlessBilling: Indicates if the customer has chosen paperless billing

PaymentMethod: Indicates how the customer pays their bill

MonthlyCharges: Indicates the customer’s current total monthly charge for all their services from the company

Churn: Yes = the customer left the company this quarter. No = the customer remained with the company. Directly related to Churn Value


**_Methodology Used_**:

Step 1: 


**_Findings_**:
1. 75% of customers have less than 55 months tenure.

2. Average Monthly charges are USD 64.76 whereas 25% of customers pay more than USD 89.85 monthly.

3. Data is highly imbalanced, not churn-churn ratio = 73:27.

4. Total Charges and Monthly Charges have a direct relationship. As monthly charges increase, total charges increase.

5. Churn is high when monthly charges are high while when monthly charges are low, it is noticed that there is a greater tendency for no churn.

6. There is a higher churn at lower total charges— however, a higher monthly charge at a lower tenure results in a lower total charge. Hence, all three factors - Higher monthly charge, lower tenure, and lower total charge are linked to high churn.

7. High churn was witnessed in the case of month-to-month contracts, no online security, no Tech support, the first year of subscription, and fiber optics internet. Low churn is seen in the case of long-term contracts, subscriptions without internet service, and customers engaged for 5+ years. Factors like gender, availability of phone service, and number of multiple lines have almost no impact on churn.


**_Output_**:
1. 
