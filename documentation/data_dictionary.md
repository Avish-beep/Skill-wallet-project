# Data Dictionary: Student Mental Health Ecosystem (Epic 1)

This data dictionary audits the fields in the ingested dataset against the 18 expected SkillWallet curriculum variables.

| Column | Actual Column Name | Data Type | Description | Example | Missing Values | Unique Values | Validation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **User ID** | *(Absent in baseline)* | String | Unique identifier assigned to each individual student. | `STD_0001` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Age** | `Age` | Float64 / Int | Chronological age of the student in completed years. | `19.0` | 1 (0.99%) | 7 | **Valid (Range: 18–24; Imputed with median=19).** |
| **Gender** | `Choose your gender` | String | Self-reported gender identity. | `Female` | 0 (0.0%) | 2 | **Valid (`Female`, `Male`).** |
| **Occupation** | `What is your course?` | String | Course, academic major, or professional field. | `Engineering` | 0 (0.0%) | 49 | **Partial (Captures degree program rather than job).** |
| **Stress Level** | *(Absent in baseline)* | String | Measured level of stress (`Low`, `Medium`, `High`). | `High` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Anxiety Score** | `Do you have Anxiety?` | String | Indicator or score reflecting clinical anxiety symptoms. | `Yes` | 0 (0.0%) | 2 | **Partial (Binary `Yes`/`No` vs. numeric score).** |
| **Depression Score** | `Do you have Depression?` | String | Indicator or score reflecting clinical depression severity. | `No` | 0 (0.0%) | 2 | **Partial (Binary `Yes`/`No` vs. numeric score).** |
| **Sleep Quality** | *(Absent in baseline)* | String | Self-reported sleep quality (`Poor`, `Average`, `Good`). | `Average` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Daily Screen Time (hrs)** | *(Absent in baseline)* | Float | Average daily hours spent on digital screens. | `5.5` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Physical Activity Level** | *(Absent in baseline)* | String | Categorical frequency of exercise (`Low`, `Moderate`, `High`). | `Moderate` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Social Interaction Score**| *(Absent in baseline)* | Float / Int | Quantitative score evaluating interpersonal engagement. | `7` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Mental Health History** | *(Absent in baseline)* | String | Prior personal history of psychological conditions (`Yes`/`No`). | `No` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Therapy Type** | *(Absent in baseline)* | String | Modality of therapeutic intervention provided (`CBT`, `Counseling`). | `CBT` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Intervention Duration** | *(Absent in baseline)* | Int | Exposure duration of intervention in weeks. | `8` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Progress Score** | *(Absent in baseline)* | Float / Int | Quantitative improvement score post-intervention. | `6.8` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Medication Usage** | *(Absent in baseline)* | String | Indicator of psychotropic medication use (`Yes`/`No`). | `No` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Support System Strength** | *(Absent in baseline)* | String | Categorical quality of family/peer support (`Low`, `Medium`, `High`). | `Medium` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
| **Work-Life Balance Score** | *(Absent in baseline)* | Float / Int | Metric measuring balance between academic/work and personal life. | `5.2` | N/A | N/A | **Missing in Baseline Survey; Expected by SkillWallet.** |
