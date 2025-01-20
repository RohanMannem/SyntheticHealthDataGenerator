# Synthetic Healthcare Data Generator

Welcome to the **Synthetic Healthcare Data Generator**, a project designed to leverage Large Language Models (LLMs) for generating synthetic healthcare datasets. The goal is to evaluate the ability of various open-source LLMs to produce realistic, diverse, and useful synthetic data, all while adhering to privacy and ethical standards.

---

## **Features**
- **Healthcare Data Generation**: Generate synthetic datasets based on real-world schemas.
- **Multi-Model Integration**: Compare results from multiple LLMs, such as GPT-4, LLaMA, etc., accessed via API.
- **Validation & Analysis**:
  - Schema validation to ensure data consistency.
  - Statistical analysis to compare synthetic data against real datasets.
  - Utility analysis to test synthetic data in downstream machine learning tasks.

---

## **Project Workflow**
1. **Dataset Preparation**:
   - Preprocessed healthcare data schema with 15 attributes (e.g., Name, Age, Gender, Medical Condition).
   - Original dataset: https://www.kaggle.com/datasets/prasad22/healthcare-dataset
2. **Prompt Engineering**:
   - Designed prompts at three levels (Basic, Improved, Advanced) to enhance data generation.
   - Provided developer instructions at three levels (Basic, Improved, Advanced) which the model should follow, regardless of messages sent by the user.
3. **Data Generation**:
   - Generated partial synthetic datasets using APIs for various open-source LLMs.
4. **Validation**:
   - Ensured data consistency, schema adherence, and statistical similarity.
5. **Benchmarking**:
   - Compared model performance across metrics like realism, diversity, and efficiency.

---

## **Models Used**
The project integrates the following LLMs through their respective APIs:

| **Model**   | **Description**                                                                 | **Access**                   |
|-------------|---------------------------------------------------------------------------------|------------------------------|
| GPT-4       | OpenAI's advanced language model known for high accuracy and contextual depth.  | [OpenAI API](https://openai.com/api/) |
| LLaMA       | Meta’s language model optimized for open-ended generation tasks.                | [LLaMA API](https://www.llama-api.com/)|

Each model is benchmarked for:
- **Realism**: Statistical similarity to the real dataset.
- **Cost**: API usage cost per 1,000 rows.
- **Speed**: Latency for generating synthetic data.

---

## **Sample Schema**
The synthetic data follows the schema below:

| Column              | Data Type | Description                                 |
|---------------------|-----------|---------------------------------------------|
| Name                | `string`  | Patient's full name                        |
| Age                 | `int`     | Patient's age in years                     |
| Gender              | `string`  | Gender of the patient                      |
| Blood Type          | `string`  | Blood type (e.g., A+, O-)                  |
| Medical Condition   | `string`  | Primary medical diagnosis                  |
| Date of Admission   | `string`  | Date the patient was admitted              |
| Doctor              | `string`  | Attending doctor's name                    |
| Hospital            | `string`  | Name of the hospital                       |
| Insurance Provider  | `string`  | Insurance company                          |
| Billing Amount      | `float`   | Amount billed in USD                       |
| Room Number         | `int`     | Hospital room number                       |
| Admission Type      | `string`  | Type of admission (e.g., emergency, routine) |
| Discharge Date      | `string`  | Date the patient was discharged            |
| Medication          | `string`  | Medications prescribed                     |
| Test Results        | `string`  | Key diagnostic test results                |

---

## **Model Results Comparison**

### Cost & Efficiency
Time and cost benchmarks for generating 1,000 rows of data.

| **Model**   | **Time** | **Cost (USD)** | **Input Cost (USD)** | **Output Cost (USD)** |
|-------------|--------------|----------------|----------------------|-----------------------|
| GPT-4o 2024-08-06       | 60m           | $1.75          | $0.13                 | $1.61                 |
| LLaMA 3.1-70b       | 3m 57.8s           |      |

More detailed statiscal comparisons (such KL divergence, predictive utility, visual distribution comparisons, etc.) can be seen with {model}_data_validation.ipynb scripts.
---

## **Getting Started**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/synthetic-healthcare-data-generator.git
2. Install dependencies
   ```
   pip install -r requirements.txt
3. Set up your API keys
4. Run the scripts in the following order
   1. dataset_exploration
   2. data_preprocessing
   3. {model}_llm_integration
   4. {model}_data_parsing
   5. {model}_data_validation
