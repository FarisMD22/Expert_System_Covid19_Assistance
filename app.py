# === PYTHON 3.10+ COMPATIBILITY PATCH (MUST BE FIRST) ===
import collections
import collections.abc

for _attr in ['Mapping', 'MutableMapping', 'Iterable', 'Iterator', 'Callable',
              'Set', 'MutableSet', 'Sequence', 'MutableSequence', 'Hashable',
              'Sized', 'Container', 'Collection', 'Reversible', 'Generator',
              'ByteString', 'Awaitable', 'Coroutine', 'AsyncIterable', 'AsyncIterator']:
    if hasattr(collections.abc, _attr) and not hasattr(collections, _attr):
        setattr(collections, _attr, getattr(collections.abc, _attr))
# === END COMPATIBILITY PATCH ===

"""
CIDAS - COVID-19 Intelligent Diagnostic & Assessment System
Streamlit Web Application

A comprehensive expert system for COVID-19 diagnosis, risk assessment,
and care pathway recommendations with Malaysian healthcare integration.

Author: TES6313 Project
Date: 2025
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json

from engine import DifferentialDiagnosisEngine, FuzzyRiskEngine, SeverityEngine, ExplanationEngine
from facts import *
from config import *

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="CIDAS - COVID-19 Expert System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 1rem;
    }
    .info-box {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
    .danger-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #dc3545;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #145a8c;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'language' not in st.session_state:
    st.session_state.language = 'en'

if 'assessment_history' not in st.session_state:
    st.session_state.assessment_history = []

if 'current_assessment' not in st.session_state:
    st.session_state.current_assessment = None


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def t(key):
    """Get translation for current language"""
    return get_translation(key, st.session_state.language)


def save_assessment(patient_data, diagnosis, risk, recommendation):
    """Save assessment to history"""
    assessment = {
        'timestamp': datetime.now(),
        'patient': patient_data,
        'diagnosis': diagnosis,
        'risk': risk,
        'recommendation': recommendation
    }
    st.session_state.assessment_history.append(assessment)
    st.session_state.current_assessment = assessment


def get_risk_color(risk_level):
    """Get color for risk level"""
    colors = {
        'low': '#28a745',
        'medium': '#ffc107',
        'high': '#fd7e14',
        'critical': '#dc3545'
    }
    return colors.get(risk_level, '#6c757d')


# ============================================================================
# SIDEBAR
# ============================================================================

def render_sidebar():
    """Render sidebar with navigation and settings"""
    with st.sidebar:
        st.markdown(f"<h2 style='text-align: center;'>🏥 CIDAS</h2>", unsafe_allow_html=True)
        st.markdown("---")

        # Language selection
        st.subheader("⚙️ " + t("nav_settings"))
        lang_options = {"English": "en", "Bahasa Malaysia": "ms"}
        selected_lang = st.selectbox(
            "Language / Bahasa",
            options=list(lang_options.keys()),
            index=0 if st.session_state.language == 'en' else 1
        )
        st.session_state.language = lang_options[selected_lang]

        st.markdown("---")

        # Navigation
        st.subheader("📍 Navigation")
        page = st.radio(
            "Go to",
            [
                t("nav_home"),
                t("nav_diagnosis"),
                t("nav_risk"),
                t("nav_care"),
                t("nav_history"),
                t("nav_about")
            ],
            label_visibility="collapsed"
        )

        st.markdown("---")

        # Emergency contacts
        st.subheader("🚨 Emergency Contacts")
        st.markdown(f"""
        **National Emergency:** {get_emergency_number('national')}  
        **COVID-19 Hotline:** {get_emergency_number('covid_hotline')}  
        **Health Ministry:** {get_emergency_number('health_ministry')}
        """)

        st.markdown("---")
        st.markdown(
            f"<small>{t('disclaimer_short')}</small>",
            unsafe_allow_html=True
        )

        return page


# ============================================================================
# PAGE 1: HOME
# ============================================================================

def page_home():
    """Home page with system overview"""
    st.markdown(f"<div class='main-header'>{t('app_title')}</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.2rem;'>{t('app_subtitle')}</p>", unsafe_allow_html=True)

    st.markdown("---")

    # System capabilities
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>🔬 Differential Diagnosis</h3>
            <p>27 diagnostic rules</p>
            <p>Distinguishes COVID-19, Influenza, Common Cold, Allergies</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>📊 Risk Assessment</h3>
            <p>20 fuzzy logic rules</p>
            <p>Low, Medium, High, Critical risk classification</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>🏥 Care Pathway</h3>
            <p>15 hospitalization rules</p>
            <p>Evidence-based recommendations with Malaysian integration</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # How to use
    st.subheader("📖 How to Use This System")

    with st.expander("1️⃣ Input Symptoms & Information", expanded=True):
        st.markdown("""
        Navigate to the **Diagnosis** page and enter:
        - Patient demographics (age, gender, state)
        - Current symptoms and their severity
        - Medical history and comorbidities
        - Exposure history (if applicable)
        """)

    with st.expander("2️⃣ Review Diagnosis"):
        st.markdown("""
        The system will analyze symptoms using 27 expert rules and provide:
        - Most likely condition with confidence level
        - Differential diagnosis comparison
        - Clinical reasoning and evidence
        """)

    with st.expander("3️⃣ Check Risk Assessment"):
        st.markdown("""
        Fuzzy logic analysis considering:
        - Fever level and symptom count
        - Symptom severity score
        - Age and comorbidities
        - Overall risk score (0-100)
        """)

    with st.expander("4️⃣ Follow Care Recommendations"):
        st.markdown("""
        Receive personalized care pathway:
        - Home isolation, monitored care, hospitalization, or ICU
        - Nearest COVID-designated hospitals
        - Warning signs to monitor
        - Follow-up timelines
        """)

    st.markdown("---")

    # Disclaimer
    st.markdown(f"""
    <div class='danger-box'>
        <h4>⚠️ Medical Disclaimer</h4>
        <p>{t('disclaimer')}</p>
    </div>
    """, unsafe_allow_html=True)

    # Quick stats
    if st.session_state.assessment_history:
        st.markdown("---")
        st.subheader("📈 Your Usage Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Assessments", len(st.session_state.assessment_history))
        with col2:
            last_assessment = st.session_state.assessment_history[-1]
            st.metric("Last Assessment", last_assessment['timestamp'].strftime("%Y-%m-%d %H:%M"))
        with col3:
            if st.session_state.current_assessment:
                st.metric("Current Risk", st.session_state.current_assessment['risk']['risk_level'].upper())


# ============================================================================
# PAGE 2: DIAGNOSIS
# ============================================================================

def page_diagnosis():
    """Diagnosis page with symptom input and analysis"""
    st.markdown(f"<div class='sub-header'>🔬 {t('nav_diagnosis')}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Patient information
    st.subheader(t('patient_info'))
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(t('age'), min_value=0, max_value=120, value=30)
    with col2:
        gender = st.selectbox(t('gender'), [t('male'), t('female')])
    with col3:
        state = st.selectbox(t('state'), MALAYSIAN_CONTEXT['states'])

    st.markdown("---")

    # Symptoms
    st.subheader(t('symptoms_header'))
    st.markdown(t('check_all'))

    col1, col2 = st.columns(2)

    with col1:
        # Core symptoms
        fever = st.checkbox(t('symptom_fever'))
        temp = 37.0
        if fever:
            temp = st.slider(t('symptom_temperature'), 36.0, 42.0, 38.0, 0.1)

        cough = st.checkbox(t('symptom_cough'))
        cough_type = "dry"
        if cough:
            cough_type = st.radio(t('symptom_cough_type'), [t('cough_dry'), t('cough_productive')])
            cough_type = "dry" if "Dry" in cough_type or "Kering" in cough_type else "productive"

        fatigue = st.checkbox(t('symptom_fatigue'))
        fatigue_severity = "mild"
        if fatigue:
            fatigue_severity = st.select_slider(
                "Severity",
                options=[t('severity_mild'), t('severity_moderate'), t('severity_severe')]
            )
            fatigue_severity = "mild" if "Mild" in fatigue_severity or "Ringan" in fatigue_severity else \
                "moderate" if "Moderate" in fatigue_severity or "Sederhana" in fatigue_severity else "severe"

        body_ache = st.checkbox(t('symptom_body_ache'))
        body_ache_severity = "mild"
        if body_ache:
            body_ache_severity = st.select_slider(
                "Severity ",
                options=[t('severity_mild'), t('severity_moderate'), t('severity_severe')]
            )
            body_ache_severity = "mild" if "Mild" in body_ache_severity or "Ringan" in body_ache_severity else \
                "moderate" if "Moderate" in body_ache_severity or "Sederhana" in body_ache_severity else "severe"

        sore_throat = st.checkbox(t('symptom_sore_throat'))
        runny_nose = st.checkbox(t('symptom_runny_nose'))
        sneezing = st.checkbox(t('symptom_sneezing'))
        sneezing_frequency = "occasional"
        if sneezing:
            sneezing_frequency = st.radio("Frequency", ["Occasional", "Frequent", "Constant"])
            sneezing_frequency = sneezing_frequency.lower()

    with col2:
        loss_of_taste_smell = st.checkbox(t('symptom_loss_taste_smell'))
        shortness_of_breath = st.checkbox(t('symptom_shortness_breath'))
        chest_pain = st.checkbox(t('symptom_chest_pain'))
        headache = st.checkbox(t('symptom_headache'))
        nausea = st.checkbox(t('symptom_nausea'))
        diarrhea = st.checkbox(t('symptom_diarrhea'))
        itchy_eyes = st.checkbox(t('symptom_itchy_eyes'))

        onset = st.radio(t('symptom_onset'), [t('onset_sudden'), t('onset_gradual')])
        onset = "sudden" if "Sudden" in onset or "Tiba" in onset else "gradual"

        duration = st.number_input(t('symptom_duration'), min_value=0, max_value=30, value=3)

        oxygen_saturation = st.number_input(
            t('oxygen_level'),
            min_value=70.0,
            max_value=100.0,
            value=98.0,
            step=0.1,
            help="Normal: ≥95%, Concerning: <94%, Severe: <90%"
        )

    st.markdown("---")

    # Medical history
    st.subheader(t('medical_history'))

    col1, col2, col3 = st.columns(3)

    with col1:
        diabetes = st.checkbox(t('diabetes'))
        hypertension = st.checkbox(t('hypertension'))
        heart_disease = st.checkbox(t('heart_disease'))

    with col2:
        lung_disease = st.checkbox(t('lung_disease'))
        kidney_disease = st.checkbox(t('kidney_disease'))
        cancer = st.checkbox(t('cancer'))

    with col3:
        obesity = st.checkbox(t('obesity'))
        pregnancy = st.checkbox(t('pregnancy'))
        smoking = st.checkbox(t('smoking'))

    st.markdown("---")

    # Exposure history
    with st.expander(t('exposure_history')):
        close_contact = st.checkbox(t('close_contact'))
        contact_days = 0
        if close_contact:
            contact_days = st.number_input(t('contact_days'), min_value=0, max_value=30, value=5)

        travel_history = st.checkbox(t('travel_history'))
        healthcare_worker = st.checkbox(t('healthcare_worker'))

    st.markdown("---")

    # Diagnose button
    if st.button(t('btn_diagnose'), type="primary"):
        with st.spinner(t('msg_processing')):
            # Create facts
            patient = Patient(
                patient_id=f"P{datetime.now().strftime('%Y%m%d%H%M%S')}",
                age=age,
                gender="M" if "Male" in gender or "Lelaki" in gender else "F",
                state=state
            )

            symptom = Symptom(
                fever=fever,
                temp=temp,
                cough=cough,
                cough_type=cough_type,
                fatigue=fatigue,
                fatigue_severity=fatigue_severity,
                body_ache=body_ache,
                body_ache_severity=body_ache_severity,
                sore_throat=sore_throat,
                runny_nose=runny_nose,
                sneezing=sneezing,
                sneezing_frequency=sneezing_frequency,
                loss_of_taste_smell=loss_of_taste_smell,
                shortness_of_breath=shortness_of_breath,
                chest_pain=chest_pain,
                headache=headache,
                nausea=nausea,
                diarrhea=diarrhea,
                itchy_eyes=itchy_eyes,
                onset=onset,
                duration=duration,
                oxygen_saturation=oxygen_saturation
            )

            medical_history = MedicalHistory(
                diabetes=diabetes,
                hypertension=hypertension,
                heart_disease=heart_disease,
                lung_disease=lung_disease,
                kidney_disease=kidney_disease,
                cancer=cancer,
                obesity=obesity,
                pregnancy=pregnancy,
                smoking=smoking
            )

            exposure_history = ExposureHistory(
                close_contact=close_contact,
                contact_days_ago=contact_days,
                travel_history=travel_history,
                healthcare_worker=healthcare_worker
            )

            # Run diagnosis
            engine = DifferentialDiagnosisEngine()
            engine.reset()
            engine.declare(patient)
            engine.declare(symptom)
            engine.declare(medical_history)
            engine.declare(exposure_history)
            engine.run()

            results = engine.get_top_diagnoses()

            if results:
                st.success(t('msg_complete'))

                # Display results
                top_condition, top_confidence, top_rule = results[0]

                st.markdown(f"""
                <div class='success-box'>
                    <h3>🔬 {t('diagnosis')}</h3>
                    <h2>{top_condition}</h2>
                    <p><strong>{t('confidence')}:</strong> {int(top_confidence * 100)}%</p>
                    <p><small>Rule: {top_rule}</small></p>
                </div>
                """, unsafe_allow_html=True)

                # Differential diagnosis table
                if len(results) > 1:
                    st.subheader("Differential Diagnosis")
                    df = pd.DataFrame([
                        {"Condition": c, "Confidence": f"{int(conf * 100)}%", "Rule": r}
                        for c, conf, r in results
                    ])
                    st.dataframe(df, use_container_width=True)

                # Bar chart
                fig = go.Figure(data=[
                    go.Bar(
                        x=[c for c, _, _ in results],
                        y=[conf * 100 for _, conf, _ in results],
                        marker_color=['#28a745', '#ffc107', '#fd7e14', '#6c757d'][:len(results)]
                    )
                ])
                fig.update_layout(
                    title="Diagnosis Confidence Comparison",
                    xaxis_title="Condition",
                    yaxis_title="Confidence (%)",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)

                # Calculate risk for storage
                symptom_data = {
                    'fever': fever, 'temp': temp, 'cough': cough,
                    'fatigue': fatigue, 'body_ache': body_ache,
                    'shortness_of_breath': shortness_of_breath,
                    'loss_of_taste_smell': loss_of_taste_smell,
                    'oxygen_saturation': oxygen_saturation  # CRITICAL for risk calculation
                }

                fuzzy_engine = FuzzyRiskEngine()
                risk = fuzzy_engine.calculate_risk(
                    fever_temp=temp,
                    symptom_cnt=count_symptoms(symptom_data),
                    severity_scr=calculate_symptom_severity(symptom_data),
                    age=age,
                    comorbidity_scr=aggregate_comorbidities({
                        'diabetes': diabetes, 'hypertension': hypertension,
                        'heart_disease': heart_disease, 'lung_disease': lung_disease
                    })
                )

                # Store for other pages
                patient_data = {
                    'age': age, 'gender': gender, 'state': state,
                    'symptoms': symptom_data,
                    'medical_history': {
                        'diabetes': diabetes, 'hypertension': hypertension,
                        'heart_disease': heart_disease, 'lung_disease': lung_disease
                    }
                }

                save_assessment(patient_data, results, risk, None)

                st.info("💡 Navigate to **Risk Assessment** page to see detailed risk analysis")

            else:
                # No diagnosis - provide helpful guidance
                st.warning("⚠️ **Insufficient information for diagnosis**")

                st.markdown("""
                <div class='info-box'>
                    <h4>📋 What We Need to Make a Diagnosis</h4>
                    <p>Your symptom combination doesn't match any specific condition pattern. Here's what we look for:</p>
                </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("""
                    **🦠 For COVID-19 diagnosis, we need:**
                    - ✅ **Loss of taste or smell** (most specific symptom)
                    - OR ✅ **Dry cough + Fever + Fatigue** (classic pattern)
                    - OR ✅ **Dry cough + Fever + Shortness of breath**

                    **💡 If you don't have these symptoms, you probably don't have COVID-19.**
                    """)

                    st.markdown("""
                    **🤧 For Common Cold diagnosis, we need:**
                    - ✅ **Runny nose + Sneezing**
                    - ✅ **NO fever** (or very low <37.5°C)
                    - ✅ Gradual onset
                    """)

                with col2:
                    st.markdown("""
                    **🤒 For Influenza diagnosis, we need:**
                    - ✅ **Sudden onset** (symptoms within hours)
                    - ✅ **Severe body ache** + High fever
                    - ✅ **Severe fatigue**
                    """)

                    st.markdown("""
                    **🌸 For Allergies diagnosis, we need:**
                    - ✅ **Itchy/watery eyes** + Frequent sneezing
                    - ✅ **NO fever** (allergies don't cause fever)
                    - ✅ Sudden onset (exposure to allergen)
                    """)

                st.markdown("---")

                # Analyze what they entered
                symptom_data = {
                    'fever': fever, 'cough': cough, 'loss_of_taste_smell': loss_of_taste_smell,
                    'body_ache': body_ache, 'runny_nose': runny_nose, 'sneezing': sneezing,
                    'itchy_eyes': itchy_eyes
                }

                suggestions = []

                # Check what's missing for each condition
                if fever and not loss_of_taste_smell and not cough:
                    suggestions.append(
                        "💡 You have **fever** but no respiratory symptoms. Try adding **Cough** or check if you have **Loss of taste/smell**.")

                if (runny_nose or sneezing) and fever:
                    suggestions.append(
                        "⚠️ You have **nasal symptoms** (runny nose/sneezing) but also **fever**. This is contradictory - allergies/colds don't usually cause fever. Either uncheck fever or check other symptoms.")

                if itchy_eyes and fever:
                    suggestions.append(
                        "⚠️ You have **itchy eyes** (suggests allergies) but also **fever** (suggests infection). These contradict each other. Allergies don't cause fever.")

                if not fever and not cough and not loss_of_taste_smell and not body_ache:
                    suggestions.append(
                        "💡 Very few symptoms checked. Add more symptoms like **Cough**, **Fever**, or **Body ache** to help us diagnose.")

                if body_ache and fever and onset != "Sudden":
                    suggestions.append(
                        "💡 You have **body ache + fever** but **gradual onset**. Change onset to **Sudden (within hours)** if it's influenza.")

                if suggestions:
                    st.markdown("### 🎯 Suggestions:")
                    for suggestion in suggestions:
                        st.markdown(f"- {suggestion}")
                else:
                    st.markdown("""
                    ### 🎯 What to do:
                    - **Review your symptoms** - Make sure you've checked all that apply
                    - **Check key symptoms** - Loss of taste/smell, Dry cough, Severe body ache, Runny nose
                    - **Verify onset timing** - Sudden (within hours) vs Gradual (over days)
                    - **Remove contradictory symptoms** - No fever with allergies, No sneezing with flu
                    """)

                st.info("🏥 **If symptoms are unclear, consult a healthcare professional for proper evaluation.**")


# ============================================================================
# PAGE 3: RISK ASSESSMENT
# ============================================================================

def page_risk_assessment():
    """Risk assessment page with fuzzy logic analysis"""
    st.markdown(f"<div class='sub-header'>📊 {t('nav_risk')}</div>", unsafe_allow_html=True)

    if not st.session_state.current_assessment:
        st.info("👈 Please complete a diagnosis first")
        return

    assessment = st.session_state.current_assessment
    risk = assessment['risk']

    st.markdown("---")

    # Risk level display
    risk_level = risk['risk_level']
    risk_score = risk['risk_score']
    risk_color = get_risk_color(risk_level)

    # Show warning if there was an error in calculation
    if 'error' in risk:
        st.warning(
            f"⚠️ Note: Risk calculation encountered an issue. Showing conservative medium risk estimate. ({risk['error']})")

    st.markdown(f"""
    <div style='background-color: {risk_color}; padding: 2rem; border-radius: 1rem; color: white; text-align: center;'>
        <h1>{t(f'risk_{risk_level}')}</h1>
        <h2>{risk_score:.1f} / 100</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Risk factors breakdown
    st.subheader("Contributing Factors")

    # Get inputs safely (may not exist if there was an error)
    inputs = risk.get('inputs', {
        'fever': 37.0,
        'symptoms': 0,
        'severity': 0,
        'age': 0,
        'comorbidity': 0
    })

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("🌡️ Fever", f"{inputs.get('fever', 0):.1f}°C")
    with col2:
        st.metric("📋 Symptoms", inputs.get('symptoms', 0))
    with col3:
        st.metric("⚠️ Severity", f"{inputs.get('severity', 0):.0f}/100")
    with col4:
        st.metric("👤 Age", f"{inputs.get('age', 0)} yrs")
    with col5:
        st.metric("🏥 Comorbidity", f"{inputs.get('comorbidity', 0):.1f}/10")

    # Gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=risk_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risk Score"},
        delta={'reference': 50},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': risk_color},
            'steps': [
                {'range': [0, 35], 'color': "lightgreen"},
                {'range': [35, 65], 'color': "lightyellow"},
                {'range': [65, 90], 'color': "orange"},
                {'range': [90, 100], 'color': "lightcoral"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Risk interpretation
    st.subheader("Risk Level Interpretation")

    if risk_level == 'critical':
        st.markdown("""
        <div class='danger-box'>
            <h4>🚨 CRITICAL RISK (80-100)</h4>
            <ul>
                <li>Immediate medical evaluation required</li>
                <li>High risk of severe complications</li>
                <li>Hospital or ICU care likely needed</li>
                <li>Close monitoring essential</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    elif risk_level == 'high':
        st.markdown("""
        <div class='warning-box'>
            <h4>⚠️ HIGH RISK (65-80)</h4>
            <ul>
                <li>Urgent medical consultation recommended</li>
                <li>Increased risk of complications</li>
                <li>May require hospitalization</li>
                <li>Daily monitoring advised</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    elif risk_level == 'medium':
        st.markdown("""
        <div class='info-box'>
            <h4>ℹ️ MEDIUM RISK (35-65)</h4>
            <ul>
                <li>Medical consultation recommended</li>
                <li>Moderate risk of complications</li>
                <li>Home care with close monitoring</li>
                <li>Follow-up within 48 hours</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='success-box'>
            <h4>✅ LOW RISK (0-35)</h4>
            <ul>
                <li>Standard home care appropriate</li>
                <li>Low risk of severe complications</li>
                <li>Self-monitoring of symptoms</li>
                <li>Seek care if symptoms worsen</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 Navigate to **Care Pathway** page for personalized recommendations")


# ============================================================================
# PAGE 4: CARE PATHWAY
# ============================================================================

def page_care_pathway():
    """Care pathway recommendations with hospital finder"""
    st.markdown(f"<div class='sub-header'>🏥 {t('nav_care')}</div>", unsafe_allow_html=True)

    if not st.session_state.current_assessment:
        st.markdown("---")
        st.markdown("""
        <div class='info-box'>
            <h3>📋 How to Get Your Care Recommendation</h3>
            <p><strong>Follow these 3 steps:</strong></p>
            <ol>
                <li><strong>Go to Diagnosis page</strong> → Enter your symptoms and medical information</li>
                <li><strong>Click "Diagnose"</strong> → Get your diagnosis result</li>
                <li><strong>Navigate to Risk Assessment</strong> → View your risk level</li>
                <li><strong>Return to this page</strong> → Your care recommendation will appear automatically!</li>
            </ol>
            <p style='margin-top: 1rem;'><em>💡 Tip: Complete the diagnosis first, then your care pathway will be ready here.</em></p>
        </div>
        """, unsafe_allow_html=True)

        # Quick start button
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔬 Go to Diagnosis Page", type="primary", use_container_width=True):
                st.info("👈 Use the sidebar to navigate to Diagnosis page")

        return

    assessment = st.session_state.current_assessment
    risk = assessment.get('risk')
    patient = assessment.get('patient')

    # Check if risk assessment exists
    if not risk:
        st.warning("⚠️ Risk assessment not found. Please complete the Risk Assessment page first.")
        return

    st.markdown("---")

    # Generate recommendation
    try:
        severity_engine = SeverityEngine()
        severity_engine.reset()

        # Declare facts
        severity_engine.declare(RiskAssessment(
            level=risk['risk_level'],
            score=risk['risk_score']
        ))

        # Add medical history if available
        medical_history = patient.get('medical_history', {})
        if medical_history:
            if medical_history.get('diabetes'):
                severity_engine.declare(MedicalHistory(diabetes=True))
            if medical_history.get('heart_disease'):
                severity_engine.declare(MedicalHistory(heart_disease=True))
            if medical_history.get('lung_disease'):
                severity_engine.declare(MedicalHistory(lung_disease=True))
            if medical_history.get('pregnancy'):
                severity_engine.declare(MedicalHistory(pregnancy=True))

        # Add patient age
        severity_engine.declare(Patient(age=patient.get('age', 30)))

        # Add diagnosis if available
        diagnosis = assessment.get('diagnosis')
        if diagnosis and len(diagnosis) > 0:
            diagnosis_condition = diagnosis[0][0]  # Get top diagnosis
            # Only declare if it's COVID-19 (for COVID-specific rules)
            if 'COVID' in diagnosis_condition:
                severity_engine.declare(Symptom(fever=True))  # Trigger COVID rules

        # Run engine
        severity_engine.run()

        recommendation = severity_engine.get_recommendation()

    except Exception as e:
        st.error(f"Error generating recommendation: {str(e)}")
        st.info("Please try completing the diagnosis again.")
        return

    if recommendation:
        action = recommendation.get('action', 'UNKNOWN')
        urgency = recommendation.get('urgency', 'UNKNOWN')

        # Display recommendation
        if urgency == "EMERGENCY":
            box_class = 'danger-box'
            icon = "🚨"
        elif urgency == "URGENT":
            box_class = 'warning-box'
            icon = "⚠️"
        else:
            box_class = 'info-box'
            icon = "ℹ️"

        st.markdown(f"""
        <div class='{box_class}'>
            <h2>{icon} {action.replace('_', ' ').title()}</h2>
            <h4>Urgency: {urgency}</h4>
            <p>{recommendation.get('explanation', '')}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # What to do
        st.subheader("📋 What To Do")

        if action == "IMMEDIATE_HOSPITALIZATION":
            st.markdown("""
            ### IMMEDIATE ACTION REQUIRED

            1. **Call 999** or go to nearest hospital immediately
            2. Do NOT drive yourself if experiencing severe symptoms
            3. Bring ID and medical records
            4. Inform hospital of suspected COVID-19

            **Warning Signs:**
            - Severe difficulty breathing
            - Persistent chest pain
            - Confusion or inability to stay awake
            - Bluish lips or face
            - Oxygen saturation < 90%
            """)

        elif action == "HOSPITALIZATION":
            st.markdown("""
            ### Hospitalization Recommended

            1. Contact healthcare provider within 24 hours
            2. Prepare overnight bag with essentials
            3. Bring list of current medications
            4. Arrange for family notification

            **You May Need:**
            - Oxygen therapy
            - Intravenous fluids
            - Close medical monitoring
            - Specialist consultation
            """)

        elif action == "HOME_CARE_MONITORED":
            st.markdown("""
            ### Monitored Home Care

            1. Self-isolate at home
            2. Monitor temperature twice daily
            3. Monitor oxygen saturation if available
            4. Keep symptom diary
            5. Schedule follow-up consultation within 48 hours

            **Warning Signs - Seek Care If:**
            - Worsening shortness of breath
            - Persistent fever > 3 days
            - Inability to keep fluids down
            - Confusion or extreme fatigue
            - Oxygen saturation < 94%
            """)

        else:  # HOME_ISOLATION
            st.markdown("""
            ### Standard Home Isolation

            1. Isolate in separate room if possible
            2. Monitor temperature daily
            3. Rest and stay hydrated
            4. Take OTC medications for symptom relief
            5. Maintain communication with healthcare provider

            **Self-Care Tips:**
            - Get plenty of rest
            - Drink lots of fluids
            - Eat nutritious foods
            - Avoid close contact with others
            - Wear mask if must interact
            """)

        st.markdown("---")

        # Hospital finder
        if action in ["IMMEDIATE_HOSPITALIZATION", "HOSPITALIZATION"]:
            st.subheader(f"🏥 {t('nearest_hospitals')}")

            state = patient['state']
            hospitals = get_hospitals_by_state(state)

            if hospitals:
                st.markdown(f"**COVID-19 Designated Hospitals in {state}:**")
                for i, hospital in enumerate(hospitals, 1):
                    st.markdown(f"{i}. {hospital}")
            else:
                st.warning(f"No hospitals found for {state}")

            st.markdown("---")

            # Emergency contacts
            st.subheader("📞 Emergency Contacts")
            st.markdown(f"""
            - **Emergency:** {get_emergency_number('national')}
            - **COVID-19 Hotline:** {get_emergency_number('covid_hotline')}
            - **Health Ministry:** {get_emergency_number('health_ministry')}
            - **Hospital Helpline:** {get_emergency_number('hospital_helpline')}
            """)

    else:
        st.markdown("---")
        st.markdown("""
        <div class='warning-box'>
            <h3>⚠️ Unable to Generate Specific Recommendation</h3>
            <p>We couldn't generate a detailed care recommendation based on your current data.</p>
            <p><strong>Possible reasons:</strong></p>
            <ul>
                <li>Incomplete risk assessment data</li>
                <li>Missing required information</li>
                <li>System needs more input to make a recommendation</li>
            </ul>
            <p><strong>What to do:</strong></p>
            <ol>
                <li>Go back to <strong>Diagnosis</strong> page</li>
                <li>Ensure all required fields are filled</li>
                <li>Complete the diagnosis again</li>
                <li>Return to this page</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Show current risk level at least
        if risk:
            st.subheader("Your Current Risk Level")
            risk_level = risk['risk_level']
            risk_score = risk['risk_score']
            risk_color = get_risk_color(risk_level)

            st.markdown(f"""
            <div style='background-color: {risk_color}; padding: 1rem; border-radius: 0.5rem; color: white; text-align: center;'>
                <h3>{t(f'risk_{risk_level}').upper()}</h3>
                <h4>{risk_score:.1f} / 100</h4>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # General guidance based on risk level
            st.subheader("General Care Guidance")
            if risk_level == 'critical' or risk_level == 'high':
                st.error(
                    "🚨 **High/Critical Risk:** Please seek medical attention immediately. Call 999 or go to nearest hospital.")
            elif risk_level == 'medium':
                st.warning(
                    "⚠️ **Medium Risk:** Consult a healthcare provider within 24-48 hours. Monitor symptoms closely.")
            else:
                st.info("ℹ️ **Low Risk:** Self-monitor at home. Seek care if symptoms worsen.")

        # Emergency contacts always shown
        st.markdown("---")
        st.subheader("📞 Emergency Contacts")
        st.markdown(f"""
        - **Emergency:** {get_emergency_number('national')}
        - **COVID-19 Hotline:** {get_emergency_number('covid_hotline')}
        - **Health Ministry:** {get_emergency_number('health_ministry')}
        """)


# ============================================================================
# PAGE 5: HISTORY
# ============================================================================

def page_history():
    """Assessment history tracking"""
    st.markdown(f"<div class='sub-header'>📈 {t('nav_history')}</div>", unsafe_allow_html=True)

    if not st.session_state.assessment_history:
        st.info("No assessment history yet. Complete a diagnosis to start tracking.")
        return

    st.markdown("---")

    # Statistics
    total_assessments = len(st.session_state.assessment_history)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Assessments", total_assessments)
    with col2:
        first_date = st.session_state.assessment_history[0]['timestamp']
        st.metric("First Assessment", first_date.strftime("%Y-%m-%d"))
    with col3:
        last_date = st.session_state.assessment_history[-1]['timestamp']
        st.metric("Last Assessment", last_date.strftime("%Y-%m-%d"))

    st.markdown("---")

    # Timeline
    st.subheader("Assessment Timeline")

    df = pd.DataFrame([
        {
            'Date': a['timestamp'].strftime("%Y-%m-%d %H:%M"),
            'Diagnosis': a['diagnosis'][0][0] if a['diagnosis'] else 'N/A',
            'Confidence': f"{int(a['diagnosis'][0][1] * 100)}%" if a['diagnosis'] else 'N/A',
            'Risk Level': a['risk']['risk_level'].upper(),
            'Risk Score': f"{a['risk']['risk_score']:.1f}"
        }
        for a in st.session_state.assessment_history
    ])

    st.dataframe(df, use_container_width=True)

    # Risk trend chart
    if total_assessments > 1:
        st.subheader("Risk Score Trend")

        dates = [a['timestamp'] for a in st.session_state.assessment_history]
        scores = [a['risk']['risk_score'] for a in st.session_state.assessment_history]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=scores,
            mode='lines+markers',
            name='Risk Score',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=10)
        ))

        # Add risk level zones
        fig.add_hrect(y0=0, y1=35, fillcolor="green", opacity=0.1, line_width=0)
        fig.add_hrect(y0=35, y1=65, fillcolor="yellow", opacity=0.1, line_width=0)
        fig.add_hrect(y0=65, y1=90, fillcolor="orange", opacity=0.1, line_width=0)
        fig.add_hrect(y0=90, y1=100, fillcolor="red", opacity=0.1, line_width=0)

        fig.update_layout(
            title="Risk Score Over Time",
            xaxis_title="Date",
            yaxis_title="Risk Score",
            height=400,
            yaxis_range=[0, 100]
        )

        st.plotly_chart(fig, use_container_width=True)

    # Clear history button
    if st.button("🗑️ Clear History", type="secondary"):
        st.session_state.assessment_history = []
        st.session_state.current_assessment = None
        st.rerun()


# ============================================================================
# PAGE 6: ABOUT
# ============================================================================

def page_about():
    """About page with system information"""
    st.markdown(f"<div class='sub-header'>ℹ️ {t('nav_about')}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # System overview
    st.subheader("About CIDAS")

    st.markdown("""
    **CIDAS (COVID-19 Intelligent Diagnostic & Assessment System)** is an expert system 
    developed for TES6313 Expert Systems course. It combines rule-based reasoning, 
    fuzzy logic, and explainable AI to provide comprehensive COVID-19 assessment.

    ### Key Features

    - **Differential Diagnosis**: Distinguishes COVID-19 from Influenza, Common Cold, and Allergies
    - **Fuzzy Risk Classification**: Nuanced risk assessment using fuzzy logic
    - **Care Pathway Recommendations**: Evidence-based hospitalization decisions
    - **Malaysian Healthcare Integration**: KKM guidelines, local hospitals, bilingual support
    - **Explainable AI**: Transparent reasoning for all decisions

    ### Technical Architecture

    **Module 1: Differential Diagnosis (Rule-Based)**
    - 27 diagnostic rules with certainty factors
    - Forward chaining inference
    - Based on WHO/CDC clinical guidelines

    **Module 2: Risk Classification (Fuzzy Logic)**
    - 20 fuzzy inference rules
    - 5 input variables (fever, symptoms, severity, age, comorbidity)
    - Mamdani fuzzy inference method

    **Module 3: Severity Assessment (Hybrid)**
    - 15 hospitalization rules
    - Combines rule-based and fuzzy reasoning
    - Aligned with WHO severity guidelines

    ### Knowledge Sources

    - WHO COVID-19 Clinical Management Guidelines
    - CDC Influenza vs COVID-19 Comparison
    - KKM (Malaysia) Severity Categories
    - Chrimes et al. [30]: Decision node architecture
    - Ozbey et al. [2]: Fuzzy inference for risk assessment
    - Ahmed et al. [32]: BRBES for severity prediction
    """)

    st.markdown("---")

    # System statistics
    st.subheader("System Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Rules", "62")
        st.caption("27 diagnosis + 20 fuzzy + 15 severity")

    with col2:
        st.metric("Fuzzy Variables", "6")
        st.caption("5 inputs + 1 output")

    with col3:
        st.metric("Supported Languages", "2")
        st.caption("English + Bahasa Malaysia")

    st.markdown("---")

    # Disclaimer
    st.markdown(f"""
    <div class='danger-box'>
        <h4>⚠️ Important Disclaimer</h4>
        <p>{t('disclaimer')}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Credits
    st.subheader("Credits")
    st.markdown("""
    **Developed by:** TES6313 Expert Systems Project Team  
    **Course:** TES6313 Expert Systems  
    **Date:** 2025  
    **Technology Stack:** Python, Experta, scikit-fuzzy, Streamlit  

    **Special Thanks:**
    - Ministry of Health Malaysia (KKM) for clinical guidelines
    - WHO for COVID-19 management protocols
    - Research community for open-access COVID-19 data
    """)


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point"""

    # Render sidebar and get selected page
    page = render_sidebar()

    # Route to appropriate page
    if "Home" in page or "Utama" in page:
        page_home()
    elif "Diagnosis" in page:
        page_diagnosis()
    elif "Risk" in page or "Risiko" in page:
        page_risk_assessment()
    elif "Care" in page or "Penjagaan" in page:
        page_care_pathway()
    elif "History" in page or "Sejarah" in page:
        page_history()
    elif "About" in page or "Tentang" in page:
        page_about()


if __name__ == "__main__":
    main()