## COVID-19 Intelligent Diagnostic & Assessment Expert System (CIDAS)

---

## PROJECT OVERVIEW

| Aspect | Decision |
|--------|----------|
| **Approach** | Hybrid Rule-Based + Fuzzy Inference System |
| **Scope** | Comprehensive 3-Module System |
| **UI Framework** | Streamlit |
| **IDE** | PyCharm |
| **Version Control** | GitHub |
| **Language** | Python 3.9+ |

---

## SYSTEM ARCHITECTURE: 3-MODULE DESIGN

Your system will have **three interconnected modules**, making it comprehensive and impressive:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CIDAS - Main Dashboard                           │
│                  (Streamlit Web Interface)                          │
└─────────────────────────────────────────────────────────────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   MODULE 1      │    │   MODULE 2      │    │   MODULE 3      │
│   Differential  │───▶│   Risk          │───▶│   Severity &    │
│   Diagnosis     │    │   Classification│    │   Hospitalization│
│                 │    │                 │    │   Prediction     │
│  (Rule-Based)   │    │    (Fuzzy)      │    │ (Hybrid Rules)   │
│                 │    │                 │    │                  │
│ COVID vs Flu    │    │ Low/Medium/     │    │ Home Care vs     │
│ vs Cold vs      │    │ High/Critical   │    │ Hospital vs ICU  │
│ Allergies       │    │                 │    │                  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                      │                      │
        └──────────────────────┴──────────────────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │   EXPLANATION ENGINE    │
                 │   (Why this diagnosis?) │
                 └─────────────────────────┘
```

### Module Flow Logic:
1. **Module 1 (Differential Diagnosis):** First determines WHAT the patient likely has
2. **Module 2 (Risk Classification):** IF COVID suspected → Calculates risk level using fuzzy logic
3. **Module 3 (Severity & Action):** Based on risk → Recommends hospitalization/home care

---

## KNOWLEDGE REPRESENTATION STRATEGY

### Module 1: Differential Diagnosis (Rule-Based with Certainty Factors)

**Purpose:** Distinguish between COVID-19, Influenza, Common Cold, and Allergies

**Knowledge Source References:**
- Chrimes et al. [30]: 212 decision nodes for COVID assessment
- Shatnawi et al. [13]: 9 symptom parameters with expert validation
- WHO/CDC differential diagnosis guidelines

**Sample Rule Structure:**
```python
"""
Differential Diagnosis Rules
Source: Synthesized from WHO guidelines + Shatnawi et al. (2021)
"""

# Rule DD-001: Strong COVID Indicator
@Rule(
    Symptom(fever=True, temp=P(lambda x: x >= 38.0)),
    Symptom(dry_cough=True),
    Symptom(loss_of_taste_smell=True),  # Highly specific to COVID
    salience=90  # High priority
)
def strong_covid_indicator(self):
    """
    Loss of taste/smell is highly specific to COVID-19 (>95% specificity)
    Combined with fever and dry cough gives high confidence
    CF = 0.92
    """
    self.declare(Diagnosis(condition="COVID-19", cf=0.92))

# Rule DD-002: Flu Pattern
@Rule(
    Symptom(fever=True, temp=P(lambda x: x >= 38.5)),
    Symptom(body_ache=True, severity="severe"),
    Symptom(fatigue=True, severity="severe"),
    Symptom(sudden_onset=True),
    NOT(Symptom(loss_of_taste_smell=True))
)
def influenza_pattern(self):
    """
    Flu characterized by sudden onset, high fever, severe body aches
    Absence of anosmia differentiates from COVID
    CF = 0.85
    """
    self.declare(Diagnosis(condition="Influenza", cf=0.85))

# Rule DD-003: Common Cold Pattern
@Rule(
    Symptom(runny_nose=True),
    Symptom(sneezing=True),
    Symptom(sore_throat=True),
    OR(NOT(Symptom(fever=True)), Symptom(fever=True, temp=P(lambda x: x < 38.0))),
    Symptom(gradual_onset=True)
)
def common_cold_pattern(self):
    """
    Cold: gradual onset, prominent nasal symptoms, mild/no fever
    CF = 0.80
    """
    self.declare(Diagnosis(condition="Common Cold", cf=0.80))

# Rule DD-004: Allergies Pattern  
@Rule(
    Symptom(sneezing=True, frequency="frequent"),
    Symptom(itchy_eyes=True),
    Symptom(runny_nose=True, discharge="clear"),
    NOT(Symptom(fever=True)),
    NOT(Symptom(body_ache=True)),
    Fact(season=P(lambda x: x in ["spring", "fall"]))  # Seasonal context
)
def allergies_pattern(self):
    """
    Allergies: no fever, itchy eyes, clear discharge, seasonal
    CF = 0.88
    """
    self.declare(Diagnosis(condition="Allergies", cf=0.88))
```

**Differential Diagnosis Decision Matrix:**

| Symptom | COVID-19 | Influenza | Cold | Allergies |
|---------|----------|-----------|------|-----------|
| Fever | Common (≥38°C) | Common (High) | Rare/Mild | Never |
| Cough | Common (Dry) | Common | Mild | Sometimes |
| Fatigue | Common | Severe | Mild | Sometimes |
| Body Aches | Sometimes | Severe | Slight | Never |
| Sore Throat | Sometimes | Sometimes | Common | Sometimes |
| Runny Nose | Rare | Sometimes | Common | Common |
| Sneezing | Rare | Sometimes | Common | Common |
| Loss of Taste/Smell | **Common** | Rare | Sometimes | Never |
| Shortness of Breath | Sometimes | Rare | Never | Never |
| Itchy Eyes | Never | Never | Never | **Common** |
| Onset | Gradual | **Sudden** | Gradual | Sudden |

---

### Module 2: Risk Classification (Fuzzy Inference System)

**Purpose:** Calculate COVID-19 risk level with uncertainty handling

**Knowledge Source References:**
- Ozbey et al. [2]: 216 fuzzy rules, Mamdani inference
- Şahin et al. [11]: Type-2 fuzzy with 86.6% accuracy
- Asl et al. [4]: Type-2 fuzzy for ICU prediction

**Fuzzy Variables Design:**

```python
"""
Fuzzy Input Variables
Based on: Ozbey et al. (2021), Mohebbi et al. (2020)
"""

# 1. FEVER LEVEL (Linguistic Variable)
#    Universe: 36.0 - 42.0 °C
fever_level = {
    'normal':     (36.0, 36.5, 37.0, 37.2),  # Trapezoidal
    'low_grade':  (37.0, 37.3, 37.8, 38.0),  # Trapezoidal
    'moderate':   (37.8, 38.2, 38.8, 39.2),  # Trapezoidal
    'high':       (39.0, 39.5, 40.5, 42.0),  # Trapezoidal
}

# 2. SYMPTOM COUNT (Linguistic Variable)
#    Universe: 0 - 15 symptoms
symptom_count = {
    'few':        (0, 0, 2, 4),       # Triangular-ish
    'moderate':   (3, 5, 7, 9),       # Trapezoidal
    'many':       (7, 10, 15, 15),    # Triangular-ish
}

# 3. SYMPTOM SEVERITY SCORE (Linguistic Variable)
#    Universe: 0 - 100 (aggregated severity)
severity_score = {
    'mild':       (0, 0, 25, 40),
    'moderate':   (30, 45, 55, 70),
    'severe':     (60, 75, 100, 100),
}

# 4. AGE RISK FACTOR (Linguistic Variable)
#    Universe: 0 - 100 years
age_risk = {
    'low':        (0, 0, 30, 45),      # Young adults
    'medium':     (40, 50, 55, 65),    # Middle age
    'high':       (60, 70, 100, 100),  # Elderly
}

# 5. COMORBIDITY SCORE (Linguistic Variable)
#    Universe: 0 - 10 (weighted comorbidity count)
comorbidity_score = {
    'none':       (0, 0, 1, 2),
    'some':       (1, 2, 4, 5),
    'multiple':   (4, 6, 10, 10),
}

# OUTPUT: RISK LEVEL
#    Universe: 0 - 100
risk_level = {
    'low':        (0, 0, 20, 35),
    'medium':     (25, 40, 50, 65),
    'high':       (55, 70, 80, 90),
    'critical':   (80, 90, 100, 100),
}
```

**Sample Fuzzy Rules:**
```python
"""
Fuzzy Rules for Risk Classification
Source: Adapted from Ozbey et al. (2021), Mohebbi et al. (2020)
"""

fuzzy_rules = [
    # Rule FR-001: Young + Few Symptoms + No Comorbidity = Low Risk
    "IF fever_level IS normal AND symptom_count IS few AND age_risk IS low AND comorbidity IS none THEN risk IS low",
    
    # Rule FR-002: High Fever + Many Symptoms = High Risk
    "IF fever_level IS high AND symptom_count IS many THEN risk IS high",
    
    # Rule FR-003: Elderly + Moderate Symptoms = High Risk
    "IF age_risk IS high AND symptom_count IS moderate THEN risk IS high",
    
    # Rule FR-004: Multiple Comorbidities + Any Fever = High Risk
    "IF comorbidity IS multiple AND fever_level IS NOT normal THEN risk IS high",
    
    # Rule FR-005: Critical combination
    "IF fever_level IS high AND age_risk IS high AND comorbidity IS multiple THEN risk IS critical",
    
    # ... 20+ more rules covering all combinations
]
```

---

### Module 3: Severity & Hospitalization Prediction (Hybrid)

**Purpose:** Recommend appropriate care pathway

**Knowledge Source References:**
- Ahmed et al. [32]: BRBES for severity with 95.4% accuracy
- Almutairi [36]: Multimodal severity grading
- Asl et al. [4]: ICU admission prediction

**Hybrid Approach:** Combines fuzzy risk output with rule-based decision

```python
"""
Hospitalization Decision Rules
Uses fuzzy risk_level output + additional clinical factors
Source: Ahmed et al. (2021), WHO severity guidelines
"""

@Rule(
    RiskAssessment(level="critical"),
    salience=100
)
def immediate_hospitalization(self):
    """Critical risk always requires immediate medical attention"""
    self.declare(Recommendation(
        action="IMMEDIATE_HOSPITALIZATION",
        urgency="EMERGENCY",
        explanation="Critical risk level detected. Immediate medical evaluation required."
    ))

@Rule(
    RiskAssessment(level="high"),
    Symptom(shortness_of_breath=True),
    Symptom(oxygen_saturation=P(lambda x: x < 94))
)
def hospitalization_respiratory(self):
    """
    High risk + respiratory distress = hospitalization
    SpO2 < 94% is WHO threshold for severe COVID
    """
    self.declare(Recommendation(
        action="HOSPITALIZATION",
        urgency="URGENT",
        department="RESPIRATORY_WARD",
        explanation="Respiratory distress with low oxygen saturation requires hospital care."
    ))

@Rule(
    RiskAssessment(level="high"),
    NOT(Symptom(shortness_of_breath=True)),
    Symptom(oxygen_saturation=P(lambda x: x >= 94))
)
def monitored_home_care(self):
    """High risk but stable vitals - can monitor at home with precautions"""
    self.declare(Recommendation(
        action="HOME_CARE_MONITORED",
        urgency="MODERATE",
        follow_up="24_HOURS",
        explanation="Elevated risk but stable. Home isolation with daily monitoring recommended."
    ))

@Rule(
    RiskAssessment(level="medium"),
    Patient(age=P(lambda x: x >= 60))
)
def elderly_medium_risk(self):
    """Elderly with medium risk need closer monitoring"""
    self.declare(Recommendation(
        action="HOME_CARE_MONITORED",
        urgency="MODERATE", 
        follow_up="48_HOURS",
        explanation="Age-related vulnerability requires monitoring despite moderate risk."
    ))

@Rule(
    RiskAssessment(level="low"),
    Diagnosis(condition="COVID-19")
)
def standard_home_isolation(self):
    """Low risk COVID - standard home isolation"""
    self.declare(Recommendation(
        action="HOME_ISOLATION",
        urgency="LOW",
        duration="10_DAYS",
        explanation="Low risk case. Standard home isolation with symptom monitoring."
    ))
```

**Care Pathway Decision Tree:**
```
                    ┌─────────────────┐
                    │ Risk Assessment │
                    │     Result      │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
   ┌─────────┐          ┌─────────┐          ┌─────────┐
   │CRITICAL │          │  HIGH   │          │LOW/MED  │
   └────┬────┘          └────┬────┘          └────┬────┘
        │                    │                    │
        ▼                    ▼                    │
   ┌─────────┐         ┌──────────┐              │
   │EMERGENCY│         │SpO2 < 94%│              │
   │  ICU    │         │    ?     │              │
   └─────────┘         └────┬─────┘              │
                      Yes   │   No               │
                    ┌───────┴───────┐            │
                    ▼               ▼            ▼
              ┌──────────┐   ┌──────────┐  ┌──────────┐
              │HOSPITAL  │   │MONITORED │  │  HOME    │
              │ADMISSION │   │HOME CARE │  │ISOLATION │
              └──────────┘   └──────────┘  └──────────┘
```

---

## ORIGINALITY STRATEGIES (Truly Unique Features)

### Strategy 1: Malaysian Healthcare Context Integration 🇲🇾

**Why it's unique:** No existing COVID expert system in your literature review specifically targets Malaysian healthcare context.

**Implementation:**
```python
"""
Malaysian Healthcare Integration
Unique Feature: Localized guidelines and resources
"""

MALAYSIAN_CONTEXT = {
    "emergency_numbers": {
        "national": "999",
        "health_ministry": "03-8881 0200",
        "covid_hotline": "03-8881 0200",
    },
    "hospital_categories": {
        "covid_designated": ["Hospital Sungai Buloh", "Hospital Kuala Lumpur", ...],
        "by_state": {...}
    },
    "kkm_severity_categories": {
        # Based on KKM (Kementerian Kesihatan Malaysia) guidelines
        "category_1": "Asymptomatic",
        "category_2": "Mild symptoms, no pneumonia",
        "category_3": "Pneumonia, no oxygen needed",
        "category_4": "Pneumonia + oxygen needed",
        "category_5": "Critical, ventilator needed"
    },
    "mysejahtera_integration": True,  # Reference to national app
    "pkp_guidelines": {...}  # Movement control order rules
}

@Rule(
    Recommendation(action="HOSPITALIZATION"),
    Patient(state=MATCH.state)
)
def recommend_malaysian_hospital(self, state):
    """Recommend nearest COVID-designated hospital by state"""
    hospitals = get_covid_hospitals(state)
    self.declare(LocalResource(
        hospitals=hospitals,
        hotline=MALAYSIAN_CONTEXT["emergency_numbers"]["covid_hotline"]
    ))
```

---

### Strategy 2: Temporal Symptom Progression Tracking ⏱️

**Why it's unique:** Most systems in your review assess single-point-in-time. This tracks symptom evolution.

**Implementation:**
```python
"""
Temporal Symptom Tracker
Unique Feature: Track symptom progression over time
Not found in reviewed literature - novel contribution
"""

class SymptomTimeline:
    """
    Tracks how symptoms change over time
    Helps identify deteriorating vs improving patients
    """
    
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.timeline = []  # List of timestamped assessments
    
    def add_assessment(self, symptoms: dict, timestamp=None):
        """Record symptoms at a point in time"""
        if timestamp is None:
            timestamp = datetime.now()
        self.timeline.append({
            "timestamp": timestamp,
            "symptoms": symptoms,
            "severity_score": self.calculate_severity(symptoms)
        })
    
    def get_trend(self) -> str:
        """Analyze symptom trend over last 3 assessments"""
        if len(self.timeline) < 2:
            return "INSUFFICIENT_DATA"
        
        recent = self.timeline[-3:]
        scores = [a["severity_score"] for a in recent]
        
        if scores[-1] > scores[0] * 1.2:
            return "DETERIORATING"
        elif scores[-1] < scores[0] * 0.8:
            return "IMPROVING"
        else:
            return "STABLE"

# Integrate with rules
@Rule(
    SymptomTrend(trend="DETERIORATING"),
    RiskAssessment(level=P(lambda x: x in ["medium", "high"]))
)
def escalating_case(self):
    """Deteriorating symptoms warrant immediate escalation"""
    self.declare(Recommendation(
        action="ESCALATE_CARE",
        urgency="HIGH",
        explanation="Symptoms showing deteriorating trend. Recommend immediate medical review."
    ))
```

**UI Feature:** Progress chart showing symptom severity over multiple assessments

---

### Strategy 3: Explainable AI (XAI) with Natural Language Generation 💬

**Why it's unique:** Referenced in Malik & Rathee [42] as future direction. Your system implements it.

**Implementation:**
```python
"""
Natural Language Explanation Generator
Unique Feature: Human-readable reasoning explanations
Addresses XAI gap identified in literature (Malik & Rathee, 2024)
"""

class ExplanationEngine:
    """
    Generates natural language explanations for diagnoses
    Makes the "black box" transparent
    """
    
    TEMPLATES = {
        "covid_high_confidence": """
Based on your reported symptoms, the system has identified a **{confidence}% likelihood of COVID-19**.

**Key factors contributing to this assessment:**
{factors}

**Reasoning chain:**
{reasoning_chain}

**Important:** This is an AI-assisted assessment, not a medical diagnosis. 
Please {recommendation}.
""",
        "differential": """
The system analyzed your symptoms against four conditions:

| Condition | Likelihood | Key Matching Symptoms |
|-----------|------------|----------------------|
{comparison_table}

**Most likely condition:** {top_condition} ({top_confidence}%)

**Why not {second_condition}?**
{differentiation_explanation}
""",
    }
    
    def generate_explanation(self, diagnosis_result, fired_rules):
        """Generate human-readable explanation"""
        
        # Collect contributing factors
        factors = []
        for rule in fired_rules:
            factors.append(f"• {rule.human_description}")
        
        # Build reasoning chain
        chain = self.build_reasoning_chain(fired_rules)
        
        # Generate natural language
        explanation = self.TEMPLATES["covid_high_confidence"].format(
            confidence=diagnosis_result.confidence,
            factors="\n".join(factors),
            reasoning_chain=chain,
            recommendation=self.get_recommendation_text(diagnosis_result)
        )
        
        return explanation
    
    def build_reasoning_chain(self, fired_rules):
        """Create step-by-step reasoning narrative"""
        steps = []
        for i, rule in enumerate(fired_rules, 1):
            steps.append(f"{i}. {rule.antecedent_text} → {rule.consequent_text}")
        return "\n".join(steps)
```

**Sample Output:**
```
Based on your reported symptoms, the system has identified a **87% likelihood of COVID-19**.

**Key factors contributing to this assessment:**
• Reported fever of 38.5°C (moderate-high range)
• Presence of dry cough lasting 3+ days
• Loss of taste and smell (highly specific to COVID-19)
• Recent contact with confirmed COVID-19 case

**Reasoning chain:**
1. Fever ≥ 38°C detected → Elevated temperature flag activated
2. Dry cough + fever combination → Respiratory infection pattern matched
3. Anosmia (loss of smell) present → COVID-specific symptom identified (Rule C-007)
4. Contact history confirmed → Exposure risk factored in (Rule C-012)
5. Combined evidence weighted → COVID-19 probability calculated at 87%

**Important:** This is an AI-assisted assessment, not a medical diagnosis.
Please seek PCR/RTK testing and self-isolate pending results.
```

---

### Strategy 4: Multi-Language Support (English + Bahasa Malaysia) 🌐

**Why it's unique:** None of the 40 systems in your review offer Malaysian language support.

**Implementation:**
```python
"""
Bilingual Interface Support
Unique Feature: English and Bahasa Malaysia
"""

TRANSLATIONS = {
    "en": {
        "title": "COVID-19 Diagnostic Expert System",
        "symptoms": {
            "fever": "Fever",
            "cough": "Cough",
            "fatigue": "Fatigue",
            "loss_of_smell": "Loss of Smell/Taste",
            "shortness_of_breath": "Shortness of Breath",
        },
        "risk_levels": {
            "low": "Low Risk",
            "medium": "Medium Risk", 
            "high": "High Risk",
            "critical": "Critical Risk",
        },
        "recommendations": {
            "home_isolation": "Home isolation recommended",
            "seek_testing": "Please get tested (PCR/RTK-Ag)",
            "emergency": "Seek emergency care immediately",
        }
    },
    "ms": {
        "title": "Sistem Pakar Diagnostik COVID-19",
        "symptoms": {
            "fever": "Demam",
            "cough": "Batuk",
            "fatigue": "Keletihan",
            "loss_of_smell": "Hilang Deria Bau/Rasa",
            "shortness_of_breath": "Sesak Nafas",
        },
        "risk_levels": {
            "low": "Risiko Rendah",
            "medium": "Risiko Sederhana",
            "high": "Risiko Tinggi", 
            "critical": "Risiko Kritikal",
        },
        "recommendations": {
            "home_isolation": "Kuarantin di rumah disyorkan",
            "seek_testing": "Sila dapatkan ujian (PCR/RTK-Ag)",
            "emergency": "Dapatkan rawatan kecemasan segera",
        }
    }
}

# In Streamlit UI
language = st.sidebar.selectbox("Language / Bahasa", ["English", "Bahasa Malaysia"])
lang_code = "en" if language == "English" else "ms"
t = TRANSLATIONS[lang_code]  # Translation dictionary

st.title(t["title"])
```

---

### Strategy 5: Confidence Calibration with Uncertainty Visualization 📊

**Why it's unique:** Addresses the "overconfidence" problem identified in Hasan et al. [41].

**Implementation:**
```python
"""
Confidence Calibration & Uncertainty Visualization
Addresses limitation from Hasan et al. (2022) on model overconfidence
"""

def calculate_calibrated_confidence(raw_confidence, evidence_quality):
    """
    Calibrate confidence based on input quality
    Prevents overconfident predictions from limited data
    """
    # Penalize if few symptoms reported
    symptom_penalty = max(0, 1 - (symptoms_reported / 8))  # Expect ~8 symptoms checked
    
    # Penalize if contradictory symptoms
    contradiction_penalty = count_contradictions() * 0.05
    
    # Penalize if missing critical symptoms (not checked, not explicitly "no")
    missing_penalty = count_unchecked_critical() * 0.03
    
    calibrated = raw_confidence * (1 - symptom_penalty - contradiction_penalty - missing_penalty)
    
    return {
        "calibrated_confidence": round(calibrated * 100, 1),
        "raw_confidence": round(raw_confidence * 100, 1),
        "uncertainty_factors": {
            "incomplete_data": symptom_penalty > 0,
            "contradictions_found": contradiction_penalty > 0,
            "missing_critical_info": missing_penalty > 0
        }
    }
```

**UI Visualization:**
```python
# In Streamlit
st.subheader("Confidence Analysis")

col1, col2 = st.columns(2)
with col1:
    # Gauge chart for confidence
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=result["calibrated_confidence"],
        title={"text": "Calibrated Confidence"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkblue"},
            "steps": [
                {"range": [0, 50], "color": "lightgray"},
                {"range": [50, 75], "color": "yellow"},
                {"range": [75, 100], "color": "green"}
            ],
        }
    ))
    st.plotly_chart(fig)

with col2:
    # Uncertainty factors
    st.write("**Uncertainty Factors:**")
    if result["uncertainty_factors"]["incomplete_data"]:
        st.warning("⚠️ Some symptoms were not reported")
    if result["uncertainty_factors"]["contradictions_found"]:
        st.warning("⚠️ Contradictory symptoms detected")
    if result["uncertainty_factors"]["missing_critical_info"]:
        st.info("ℹ️ Consider reporting additional symptoms for better accuracy")
```

---

## UPDATED PROJECT STRUCTURE

```
cidas/                              # COVID-19 Intelligent Diagnostic & Assessment System
│
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
│
├── app/
│   ├── __init__.py
│   ├── main.py                     # Streamlit entry point
│   ├── pages/
│   │   ├── 1_🏠_Home.py
│   │   ├── 2_🔍_Diagnosis.py       # Module 1: Differential Diagnosis
│   │   ├── 3_📊_Risk_Assessment.py # Module 2: Fuzzy Risk Classification
│   │   ├── 4_🏥_Care_Pathway.py    # Module 3: Hospitalization Recommendation
│   │   ├── 5_📈_History.py         # Temporal tracking feature
│   │   └── 6_ℹ️_About.py
│   │
│   ├── components/
│   │   ├── symptom_input.py        # Reusable symptom input component
│   │   ├── result_display.py       # Result visualization component
│   │   └── explanation_card.py     # XAI explanation component
│   │
│   └── localization/
│       ├── __init__.py
│       ├── en.py                   # English translations
│       └── ms.py                   # Bahasa Malaysia translations
│
├── engine/
│   ├── __init__.py
│   ├── facts.py                    # Fact definitions (Patient, Symptom, etc.)
│   │
│   ├── differential/               # Module 1
│   │   ├── __init__.py
│   │   ├── rules.py                # Differential diagnosis rules
│   │   └── engine.py               # Rule engine for differential
│   │
│   ├── fuzzy/                      # Module 2
│   │   ├── __init__.py
│   │   ├── variables.py            # Fuzzy variable definitions
│   │   ├── rules.py                # Fuzzy rules
│   │   └── engine.py               # Fuzzy inference engine
│   │
│   ├── severity/                   # Module 3
│   │   ├── __init__.py
│   │   ├── rules.py                # Hospitalization rules
│   │   └── engine.py               # Severity assessment engine
│   │
│   └── explanation/
│       ├── __init__.py
│       ├── generator.py            # NLG explanation generator
│       └── templates.py            # Explanation templates
│
├── data/
│   ├── malaysian_context.json      # Malaysian healthcare data
│   ├── symptom_weights.json        # Symptom severity weights
│   └── test_cases/
│       ├── covid_cases.json
│       ├── flu_cases.json
│       └── validation_set.json
│
├── evaluation/
│   ├── __init__.py
│   ├── verification.py             # Rule consistency checks
│   ├── validation.py               # Literature-based validation
│   ├── metrics.py                  # Performance metrics
│   └── reports/                    # Generated evaluation reports
│
├── tests/
│   ├── __init__.py
│   ├── test_differential.py
│   ├── test_fuzzy.py
│   ├── test_severity.py
│   └── test_integration.py
│
└── docs/
    ├── screenshots/                # For report
    ├── diagrams/                   # Architecture diagrams
    └── user_guide.md
```



## GITHUB WORKFLOW

```bash
# Initial setup
git init
git remote add origin https://github.com/YOUR_USERNAME/cidas.git

# Branch strategy
main          # Production-ready code only
├── develop   # Integration branch
├── feature/module1-differential
├── feature/module2-fuzzy  
├── feature/module3-severity
├── feature/streamlit-ui
└── feature/originality

# Commit message format
git commit -m "feat(module1): add 15 differential diagnosis rules"
git commit -m "fix(fuzzy): correct membership function for fever"
git commit -m "docs: add screenshots for report"

   pip install streamlit experta scikit-fuzzy pandas numpy plotly
   ```
4. **Start with `engine/facts.py`** - Define your fact classes

Would you like me to generate the starter code for any specific module?
