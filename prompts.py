basic_prompts = [
    "Generate 100 rows of synthetic healthcare data.",
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