test_developer_message = """
"""
basic_developer_message = """
You are generating synthetic healthcare data for a project. The goal is to create data that adheres to the following schema and includes realistic values for each attribute:

Schema:
- Name: string (e.g., "John Doe")
- Age: integer (0-100)
- Gender: categorical (e.g., "male", "female", "other")
- Blood Type: categorical (e.g., "A", "B", "AB", "O")
- Medical Condition: string (e.g., "diabetes", "hypertension")
- Date of Admission: string (e.g., "2023-01-01")
- Doctor: string (e.g., "Dr. Smith")
- Hospital: string (e.g., "General Hospital")
- Insurance Provider: string (e.g., "Blue Cross")
- Billing Amount: float (100.0–10,000.0)
- Room Number: integer
- Admission Type: categorical (e.g., "emergency", "elective", "urgent")
- Discharge Date: string (e.g., "2023-01-07")
- Medication: string (e.g., "aspirin", "insulin")
- Test Results: string (e.g., "positive", "negative")

Respond to the prompt by generating data as rows in this format. Provide the data in a JSON-like structure, one object per row.
"""
improved_developer_message = """
You are generating synthetic healthcare data for a project focused on data realism and statistical similarity to real-world healthcare data. The data must strictly adhere to the following schema:

Schema:
- Name: string (e.g., "Jane Doe")
- Age: integer (0-100; realistic distribution based on typical patient demographics)
- Gender: categorical (values: "male", "female", "other")
- Blood Type: categorical (values: "A", "B", "AB", "O"; realistic distribution)
- Medical Condition: string (e.g., "diabetes", "flu", "hypertension"; common illnesses should have more occurrences)
- Date of Admission: string (format: "YYYY-MM-DD"; ensure logical temporal relations)
- Doctor: string (e.g., "Dr. Jones"; consider specialization based on the medical condition)
- Hospital: string (e.g., "City General Hospital"; maintain consistency with regional naming)
- Insurance Provider: string (e.g., "Aetna", "Blue Cross")
- Billing Amount: float (range: 100.0–10,000.0; realistic variation)
- Room Number: integer (e.g., 101, 202)
- Admission Type: categorical (values: "emergency", "elective", "urgent")
- Discharge Date: string (format: "YYYY-MM-DD"; logically after the Date of Admission)
- Medication: string (e.g., "aspirin", "insulin"; relevant to Medical Condition)
- Test Results: string (e.g., "positive", "negative"; relevant to Medical Condition)

Provide the generated data in a JSON-like format, one object per row, ensuring consistency, diversity, and realism. Validate logical relationships, such as ensuring Discharge Date occurs after Admission Date and Medication aligns with Medical Condition.
"""
advanced_developer_message = """
You are generating synthetic healthcare data for a research project aiming to evaluate the realism and utility of synthetic datasets. The data must adhere to the following schema and meet the highest standards of quality, diversity, and logical coherence:

Schema:
- Name: string (e.g., "Alex Smith"; ensure diversity across names)
- Age: integer (0-100; follow a realistic demographic distribution, e.g., more adults than children)
- Gender: categorical (values: "male", "female", "other"; reflect real-world proportions)
- Blood Type: categorical (values: "A", "B", "AB", "O"; realistic distribution based on population statistics)
- Medical Condition: string (e.g., "diabetes", "flu", "hypertension"; include a mix of common and rare conditions)
- Date of Admission: string (format: "YYYY-MM-DD"; ensure temporal coherence)
- Doctor: string (e.g., "Dr. Patel"; match specialization to Medical Condition)
- Hospital: string (e.g., "Metropolitan Health Center"; maintain logical variety in hospital names)
- Insurance Provider: string (e.g., "Cigna", "United Healthcare")
- Billing Amount: float (range: 100.0–50,000.0; introduce realistic outliers and variability)
- Room Number: integer (ensure logical sequencing within hospitals)
- Admission Type: categorical (values: "emergency", "elective", "urgent"; ensure realistic distributions based on Medical Condition)
- Discharge Date: string (format: "YYYY-MM-DD"; ensure coherence with Admission Date)
- Medication: string (e.g., "metformin", "antibiotics"; specific to Medical Condition)
- Test Results: string (e.g., "HbA1c high", "viral test positive"; ensure relevance to Medical Condition)

Your response must:
1. Maintain diversity and realism across all attributes.
2. Ensure logical relationships between attributes (e.g., higher Billing Amount for emergency cases).
3. Introduce outliers and edge cases (e.g., patients over 90 years old with complex medical histories).
4. Present the data in a clean JSON-like format, one object per row.

Focus on making the data statistically similar to real-world healthcare datasets and suitable for training machine learning models.
"""

basic_prompts = [
    "Generate 10 rows of synthetic healthcare data.",
    "Generate 50 rows of data with the following schema: Name, Age, Gender, Blood Type, Medical Condition, Date of Admission, Doctor, Hospital, Insurance Provider, Billing Amount, Room Number, Admission Type, Discharge Date, Medication, Test Results."
    """
    Create 25 rows of data where:
        - Name is a string.
        - Age is an integer.
        - Gender is "male" or "female".
    """,
    "Generate 10 rows of healthcare data including only Name, Age, and Medical Condition."
    """Generate 15 rows of data for patients admitted with "flu"."""
]

improved_prompt = [
    """
    Generate 100 rows of synthetic data following this schema:
        - Name: string
        - Age: integer (0-100)
        - Gender: "male", "female", or "other"
        - Blood Type: "A", "B", "AB", "O"
        - Billing Amount: float (range: 100.0–10,000.0)
    """,
    """
    Create 50 rows of data where:
        - Patients aged 65 or older have higher billing amounts (minimum: 5,000.0).
        - Admission Type includes "emergency," "elective," or "urgent."
    """,
    """
    Generate 30 rows of healthcare data where:
        - Date of Admission is between "2023-01-01" and "2023-12-31."
        - Discharge Date is within 7 days of admission.
    """,
    """
    Generate 20 rows of data where:
        - Medical Condition is "diabetes."
        - Doctors specialize in endocrinology.
    """,
    """
    Create 40 rows where:
        - Insurance Provider is "Blue Cross" or "Aetna."
        - Hospitals include "General Hospital" or "City Care."
    """
]

advanced_prompt = [
    """
    Generate 100 rows of synthetic data where:
        - Patients with "diabetes" have medications like "insulin" or "metformin."
        - Blood Type influences Medical Condition probabilities.
    """,
    """
    Generate 50 rows of data with:
        - 10% of patients having unusually high billing amounts (above 50,000.0).
        - Age ranging from 0 to 100, with a focus on outliers (e.g., 100 years old).
    """,
    """
    Generate 200 rows of data ensuring:
        - Equal distribution of Blood Types ("A," "B," "AB," "O").
        - Even representation of Admission Types ("emergency," "elective," "urgent").
    """,
    """
    Create 75 rows of healthcare data where:
        - Admission dates span across weekends and weekdays.
        - Patients admitted on weekends are more likely to have longer discharge times.
    """,
    """
    Generate 50 rows of data where:
        - Each patient has a unique Name and Room Number.
        - Test Results reflect the Medical Condition (e.g., "diabetes: HbA1c test high," "flu: positive viral test").
        - Billing Amount includes additional charges for medications or extended stays.
    """

]