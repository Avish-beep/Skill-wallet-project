# Tableau Desktop 2026.1 Setup & Publishing Guide
## Project: Analysing Mental Health in Student Ecosystem

This guide provides the exact sequence of actions to build the workbook in **Tableau Desktop 2026.1** and publish it to **Tableau Public**.

---

### Step 1: Open Tableau Desktop & Connect to Data
1. Launch **Tableau Desktop 2026.1** from the Windows Start menu or navigate to:
   `"C:\Program Files\Tableau\Tableau 2026.1\bin\tableau.exe"`
2. In the left-hand **Connect** panel under *To a File*, select **Text file**.
3. Browse to the cleaned dataset location:
   `C:\Skillwallet\data\processed\student_mental_health_cleaned.csv`
4. Verify the data preview:
   - Total Fields: 23
   - Rows: 101
   - Ensure `student_id` is read as Text, `age` and flag fields as Integers, and `cgpa_midpoint` as Number (decimal).
5. Click **Sheet 1** at the bottom left to enter the authoring workspace.

---

### Step 2: Create the Calculated Fields
In the Data pane, click the small downward arrow next to the Search bar and choose **Create Calculated Field...** for each field:

1. **`Total Students`**:
   `COUNTD([student_id])`
2. **`High Risk Count`**:
   `SUM(IF [mental_health_risk] = 'High Risk' THEN 1 ELSE 0 END)`
3. **`High Risk %`**:
   `[High Risk Count] / [Total Students]`
4. **`Depression Rate %`**:
   `SUM([depression_flag]) / [Total Students]`
5. **`Anxiety Rate %`**:
   `SUM([anxiety_flag]) / [Total Students]`
6. **`Panic Attack Rate %`**:
   `SUM([panic_attack_flag]) / [Total Students]`
7. **`Treatment Gap Rate %`**:
   `SUM(IF [condition_count] > 0 AND [treatment_sought] = 'No' THEN 1 ELSE 0 END) / SUM(IF [condition_count] > 0 THEN 1 ELSE 0 END)`

---

### Step 3: Build the Worksheets
Follow the specifications in `tableau/visualization_plan.md`:
- **Sheet 1: `KPI_TotalStudents`** → Text card with `[Total Students]`
- **Sheet 2: `KPI_HighRisk`** → Text card with `[High Risk Count]` and `[High Risk %]`
- **Sheet 3: `KPI_TreatmentGap`** → Text card with `[Treatment Gap Rate %]`
- **Sheet 4: `Clinical_Burden`** → Measure Names on Rows, Measure Values on Columns (`Depression`, `Anxiety`, `Panic`)
- **Sheet 5: `Risk_Donut`** → Pie chart with `mental_health_risk` on Color, `Total Students` on Angle
- **Sheet 6: `Gender_Disparity`** → `gender` on Rows, `mental_health_risk` on Color, `Total Students` on Columns (Percent of Total)
- **Sheet 7: `Year_Progression`** → `year_of_study` on Columns, `AVG([condition_count])` on Rows
- **Sheet 8: `Academic_CGPA_Risk`** → `cgpa_range` on Columns, `Total Students` on Rows, `mental_health_risk` on Color
- **Sheet 9: `Faculty_Heatmap`** → `faculty` on Rows, Measure Names on Columns, Measure Values on Color
- **Sheet 10: `Comorbidity_Matrix`** → `condition_count` on Columns, `Total Students` on Rows

---

### Step 4: Assemble the Dashboard
1. Click the **New Dashboard** icon at the bottom.
2. Under **Size** in the left sidebar, select **Fixed size** and set to `1400 x 1050 px`.
3. Drag horizontal and vertical containers matching the layout in `tableau/dashboard_design.md`.
4. Add the KPI sheets at the top, followed by 2x2 grids for the visual worksheets.
5. In the top right of each sheet, enable **Use as Filter** for cross-filtering.

---

### Step 5: Create the Story
1. Click the **New Story** icon at the bottom.
2. Set Story size to **Automatic** or `1400 x 950 px`.
3. Create 6 Story Points matching `tableau/story_design.md`:
   - Point 1: Ecosystem Overview
   - Point 2: Clinical Conditions
   - Point 3: Demographic Profiles
   - Point 4: Academic Pressure & CGPA
   - Point 5: The Treatment Gap
   - Point 6: Strategic Interventions
4. Add rich narrative descriptions to each story point's caption card.

---

### Step 6: Save & Publish to Tableau Public
1. Save the local workbook:
   - File → **Save As...**
   - Save to: `C:\Skillwallet\tableau\student_mental_health_analysis.twbx` (Tableau Packaged Workbook).
2. Publish to Tableau Public:
   - In the top navigation menu, click: **Server** → **Tableau Public** → **Save to Tableau Public As...**
   - Enter your friend's Tableau Public credentials when prompted.
   - Set the title: `Analysing Mental Health in Student Ecosystem`.
   - Click **Save**.
3. Once published, Tableau will open the browser link:
   `https://public.tableau.com/views/AnalysingMentalHealthinStudentEcosystem/...`
4. Copy the published URL and insert it into your Flask configuration (`.env`).
