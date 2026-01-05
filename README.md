# problem-difficulty
📌 Project OverviewAutoJudge is an intelligent machine learning system designed to automatically assess the complexity of programming problems. By analyzing the textual description of a problem (including input/output details), the system predicts:
Difficulty Class: Classifies the problem as Easy, Medium, or Hard.
Complexity Score: Predicts a precise numerical difficulty score.

This project was built to automate the categorization process often found on coding platforms like Codeforces or LeetCode, removing the need for manual tagging.
📂 Dataset
The project uses the TaskComplexity dataset (provided as problems_data.jsonl).
Source: Web-scraped programming problems.
Size: ~4,000 tasks.
Features Used: title, description, input_description, output_description.
Target Variables:problem_class (Categorical: Easy, Medium, Hard)
problem_score (Numerical)

🛠️ Methodology & Approach1.
Data Preprocessing
Raw text from programming problems is noisy. We applied the following cleaning steps:
Text Combination: Merged Title, Description, Input, and Output fields into a single context string.
LaTeX Removal: Stripped mathematical symbols (e.g., $N \le 10^5$) to focus on linguistic complexity.
Normalization: Converted text to lowercase and removed special characters/excess whitespace.
2. Feature Engineering
We used TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical vectors.
Why?
It highlights unique words that differentiate difficulty levels (e.g., "array" might appear in Easy problems, while "dynamic", "graph", or "optimization" appear in Hard ones).
Settings: We limited the vectorizer to the top 3,000–5,000 features to prevent overfitting.
3. Model Selection & Tuning
We did not just pick one model; we ran a Grid Search competition to find the best one.

Classification Task (Easy/Medium/Hard)We compared the following models:
Logistic Regression: A strong baseline for text classification.
Random Forest Classifier: Handles non-linear relationships well.
Support Vector Machine (SVM): Effective in high-dimensional text spaces.

Regression Task (Numerical Score)We compared the following models:
Linear Regression (Ridge): Linear modeling with regularization.
Random Forest Regressor: Ensemble averaging for robust scoring.
Gradient Boosting: Sequential error correction for high precision.The system automatically saves the model with the highest Accuracy (Classification) and lowest Mean Absolute Error (Regression).

📊 Results
After training and hyperparameter tuning, the best performing models were selected based on the test set (20% split).
(Note: Replace the values below with the actual numbers from your train_and_tune.py output)
