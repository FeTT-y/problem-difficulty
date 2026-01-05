import streamlit as st
import joblib
import re

# 1. Page Configuration
st.set_page_config(
    page_title="AutoJudge - Difficulty Predictor",
    page_icon="⚖️",
    layout="centered"
)

# 2. Load the Trained Models
@st.cache_resource
def load_models():
    try:
        # Load the models saved from the previous step
        clf = joblib.load('best_classifier.pkl')
        reg = joblib.load('best_regressor.pkl')
        return clf, reg
    except FileNotFoundError:
        return None, None

clf_model, reg_model = load_models()

# 3. Preprocessing Function 
# (MUST match the cleaning logic used during training)
def clean_input_text(text):
    text = str(text).lower()
    text = re.sub(r'\$.*?\$', '', text)      # Remove LaTeX math
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special chars
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra spaces
    return text

# 4. Title and Header
st.title("⚖️ AutoJudge AI")
st.markdown("### Predict Programming Problem Difficulty")
st.markdown("Paste the problem details below to analyze its complexity.")

# 5. Input Form
with st.form("prediction_form"):
    # [cite_start]Text Boxes for Inputs [cite: 41, 42, 43, 44]
    problem_desc = st.text_area("Problem Description", height=200, placeholder="Paste the main problem statement here...")
    input_desc = st.text_area("Input Description", height=100, placeholder="Describe the input format...")
    output_desc = st.text_area("Output Description", height=100, placeholder="Describe the output format...")
    
    # Submit Button
    submit_button = st.form_submit_button("Predict Complexity")

# 6. Prediction Logic
if submit_button:
    if clf_model is None or reg_model is None:
        st.error("🚨 Models not found! Please run the training script first to generate .pkl files.")
    elif not problem_desc.strip():
        st.warning("⚠️ Please enter at least a Problem Description.")
    else:
        with st.spinner("Analyzing..."):
            # [cite_start]Combine and Clean Inputs [cite: 50]
            raw_text = f"{problem_desc} {input_desc} {output_desc}"
            processed_text = clean_input_text(raw_text)
            
            # [cite_start]Predict [cite: 75, 76]
            predicted_class = clf_model.predict([processed_text])[0]
            predicted_score = reg_model.predict([processed_text])[0]

            # Display Results
            st.divider()
            col1, col2 = st.columns(2)

            # Class Prediction with Color Coding
            with col1:
                st.subheader("Predicted Class")
                if predicted_class.lower() == "easy":
                    st.success(f"**{predicted_class.upper()}**")
                elif predicted_class.lower() == "medium":
                    st.warning(f"**{predicted_class.upper()}**")
                else: # Hard
                    st.error(f"**{predicted_class.upper()}**")

            # Score Prediction
            with col2:
                st.subheader("Difficulty Score")
                st.metric(label="Calculated Complexity", value=f"{predicted_score:.2f}")