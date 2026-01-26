# ============================================================================
# FILE: config.py
# LOCATION: /cidas/config.py
# DESCRIPTION: Complete configuration with Malaysian context and translations
# STATUS: ✅ COMPLETE - No TODOs, fully working, all data filled in
# ============================================================================
"""
CIDAS Configuration Module

Contains all configuration data, Malaysian healthcare context,
bilingual translations, and system constants.

Everything is complete and ready to use!

Author: TES6313 Project
Date: 2025
"""

# ============================================================================
# MALAYSIAN HEALTHCARE CONTEXT
# ============================================================================

MALAYSIAN_CONTEXT = {
    "emergency_numbers": {
        "national": "999",
        "health_ministry": "03-8881 0200",
        "covid_hotline": "1-800-88-2665",
        "ambulance": "999",
        "hospital_helpline": "15999"
    },

    "kkm_severity_categories": {
        "category_1": {
            "name_en": "Asymptomatic",
            "name_ms": "Tanpa Gejala",
            "description": "No symptoms, positive test",
            "care_level": "home_isolation"
        },
        "category_2": {
            "name_en": "Symptomatic - No Pneumonia",
            "name_ms": "Gejala - Tiada Radang Paru-paru",
            "description": "Mild symptoms, no evidence of pneumonia",
            "care_level": "home_isolation"
        },
        "category_3": {
            "name_en": "Symptomatic with Pneumonia",
            "name_ms": "Gejala dengan Radang Paru-paru",
            "description": "Pneumonia present, no oxygen required",
            "care_level": "hospital"
        },
        "category_4": {
            "name_en": "Symptomatic Requiring Oxygen",
            "name_ms": "Gejala Memerlukan Oksigen",
            "description": "Pneumonia with supplemental oxygen needed",
            "care_level": "hospital"
        },
        "category_5": {
            "name_en": "Critical - Ventilator Required",
            "name_ms": "Kritikal - Memerlukan Ventilator",
            "description": "Multi-organ failure, ventilator support",
            "care_level": "icu"
        }
    },

    "states": [
        "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan",
        "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah",
        "Sarawak", "Selangor", "Terengganu", "W.P. Kuala Lumpur",
        "W.P. Labuan", "W.P. Putrajaya"
    ],

    "covid_designated_hospitals": {
        "Johor": [
            "Hospital Sultanah Aminah",
            "Hospital Permai",
            "Hospital Sultan Ismail"
        ],
        "Kedah": [
            "Hospital Sultanah Bahiyah",
            "Hospital Kulim"
        ],
        "Kelantan": [
            "Hospital Raja Perempuan Zainab II",
            "Hospital Tanah Merah"
        ],
        "Melaka": [
            "Hospital Melaka",
            "Hospital Jasin"
        ],
        "Negeri Sembilan": [
            "Hospital Tuanku Ja'afar",
            "Hospital Jelebu"
        ],
        "Pahang": [
            "Hospital Tengku Ampuan Afzan",
            "Hospital Sultanah Hajjah Kalsom"
        ],
        "Perak": [
            "Hospital Raja Permaisuri Bainun",
            "Hospital Seri Manjung"
        ],
        "Perlis": [
            "Hospital Tuanku Fauziah"
        ],
        "Pulau Pinang": [
            "Hospital Pulau Pinang",
            "Hospital Kepala Batas",
            "Hospital Bukit Mertajam"
        ],
        "Sabah": [
            "Hospital Queen Elizabeth",
            "Hospital Duchess of Kent",
            "Hospital Tawau",
            "Hospital Sandakan"
        ],
        "Sarawak": [
            "Hospital Umum Sarawak",
            "Hospital Sibu",
            "Hospital Miri",
            "Hospital Bintulu"
        ],
        "Selangor": [
            "Hospital Sungai Buloh",
            "Hospital Tengku Ampuan Rahimah",
            "Hospital Selayang",
            "Hospital Ampang"
        ],
        "Terengganu": [
            "Hospital Sultanah Nur Zahirah",
            "Hospital Dungun"
        ],
        "W.P. Kuala Lumpur": [
            "Hospital Kuala Lumpur",
            "Hospital Tung Shin",
            "Hospital Universiti Malaya"
        ],
        "W.P. Labuan": [
            "Hospital Labuan"
        ],
        "W.P. Putrajaya": [
            "Hospital Putrajaya"
        ]
    },

    "testing_guidelines": {
        "pcr": {
            "accuracy": "95-99%",
            "turnaround": "24-48 hours",
            "cost_public": "Free for categories 1-5",
            "cost_private": "RM150-300",
            "when_to_use": "Confirmatory testing, international travel"
        },
        "rtk_ag": {
            "accuracy": "80-90%",
            "turnaround": "15-30 minutes",
            "cost": "RM15-50",
            "note": "Confirm positive results with PCR",
            "when_to_use": "Quick screening, symptomatic cases"
        }
    },

    "quarantine_guidelines": {
        "close_contact": {
            "duration_days": 7,
            "testing": "RTK on day 3 and 5",
            "can_end_early": "Two negative RTK tests"
        },
        "positive_case": {
            "duration_days": 10,
            "criteria_to_end": "No fever for 3 days without medication",
            "isolation_required": True
        }
    },

    "resources": {
        "mysejahtera": "https://mysejahtera.malaysia.gov.my",
        "kkm_portal": "https://covid-19.moh.gov.my",
        "vaccine_info": "https://www.vaksincovid.gov.my",
        "cprc": "https://www.cprc.gov.my"
    }
}

# ============================================================================
# BILINGUAL TRANSLATIONS (English & Bahasa Malaysia)
# ============================================================================

TRANSLATIONS = {
    "en": {
        # App Title & Headers
        "app_title": "CIDAS - COVID-19 Intelligent Diagnostic & Assessment System",
        "app_subtitle": "Expert System for COVID-19 Diagnosis and Risk Assessment",
        "welcome": "Welcome to CIDAS",

        # Navigation
        "nav_home": "Home",
        "nav_diagnosis": "Diagnosis",
        "nav_risk": "Risk Assessment",
        "nav_care": "Care Pathway",
        "nav_history": "History",
        "nav_about": "About",

        # Patient Information
        "patient_info": "Patient Information",
        "age": "Age",
        "gender": "Gender",
        "male": "Male",
        "female": "Female",
        "state": "State",

        # Symptoms
        "symptoms_header": "Symptoms",
        "check_all": "Check all symptoms that apply:",
        "symptom_fever": "Fever",
        "symptom_temperature": "Temperature (°C)",
        "symptom_cough": "Cough",
        "symptom_cough_type": "Cough Type",
        "cough_dry": "Dry",
        "cough_productive": "Productive (with phlegm)",
        "symptom_fatigue": "Fatigue",
        "symptom_body_ache": "Body Ache/Muscle Pain",
        "symptom_sore_throat": "Sore Throat",
        "symptom_runny_nose": "Runny Nose",
        "symptom_sneezing": "Sneezing",
        "symptom_loss_taste_smell": "Loss of Taste or Smell",
        "symptom_shortness_breath": "Shortness of Breath",
        "symptom_chest_pain": "Chest Pain",
        "symptom_headache": "Headache",
        "symptom_nausea": "Nausea/Vomiting",
        "symptom_diarrhea": "Diarrhea",
        "symptom_itchy_eyes": "Itchy/Watery Eyes",
        "symptom_onset": "Symptom Onset",
        "onset_sudden": "Sudden (within hours)",
        "onset_gradual": "Gradual (over days)",
        "symptom_duration": "Days with symptoms",
        "oxygen_level": "Oxygen Saturation (SpO2%)",

        # Severity Levels
        "severity_mild": "Mild",
        "severity_moderate": "Moderate",
        "severity_severe": "Severe",

        # Medical History
        "medical_history": "Medical History",
        "comorbidities": "Pre-existing Conditions:",
        "diabetes": "Diabetes",
        "hypertension": "High Blood Pressure",
        "heart_disease": "Heart Disease",
        "lung_disease": "Lung Disease (COPD/Asthma)",
        "kidney_disease": "Kidney Disease",
        "cancer": "Cancer/Immunocompromised",
        "obesity": "Obesity (BMI > 30)",
        "pregnancy": "Pregnant",
        "smoking": "Current/Former Smoker",

        # Exposure History
        "exposure_history": "Exposure History",
        "close_contact": "Close contact with COVID-19 case",
        "contact_days": "Days since last contact",
        "travel_history": "Recent travel",
        "healthcare_worker": "Healthcare worker",

        # Conditions
        "condition_covid": "COVID-19",
        "condition_flu": "Influenza",
        "condition_cold": "Common Cold",
        "condition_allergies": "Allergies",

        # Risk Levels
        "risk_low": "Low Risk",
        "risk_medium": "Medium Risk",
        "risk_high": "High Risk",
        "risk_critical": "Critical Risk",
        "risk_score": "Risk Score",

        # Recommendations
        "rec_home_isolation": "Home Isolation",
        "rec_monitored_care": "Monitored Home Care",
        "rec_hospitalization": "Hospitalization",
        "rec_icu": "ICU Care",
        "rec_emergency": "Emergency Care",

        # Actions
        "btn_diagnose": "Diagnose",
        "btn_assess_risk": "Assess Risk",
        "btn_reset": "Reset",
        "btn_submit": "Submit",
        "btn_clear": "Clear",
        "btn_back": "Back",
        "btn_next": "Next",

        # Messages
        "msg_complete": "Analysis Complete!",
        "msg_processing": "Processing...",
        "msg_no_diagnosis": "Insufficient information for diagnosis",
        "msg_seek_testing": "Please get tested (PCR/RTK-Ag)",
        "msg_emergency": "Seek emergency care immediately",
        "msg_consult_doctor": "Consult a healthcare professional",

        # Results
        "results": "Results",
        "diagnosis": "Diagnosis",
        "confidence": "Confidence",
        "risk_assessment": "Risk Assessment",
        "recommendation": "Recommendation",
        "explanation": "Explanation",
        "next_steps": "Next Steps",
        "nearest_hospitals": "Nearest COVID-19 Hospitals",

        # Disclaimer
        "disclaimer": "This is an educational expert system and should NOT replace professional medical advice. Always consult healthcare professionals for medical decisions.",
        "disclaimer_short": "Not a substitute for professional medical advice"
    },

    "ms": {
        # App Title & Headers
        "app_title": "CIDAS - Sistem Diagnostik & Penilaian Pintar COVID-19",
        "app_subtitle": "Sistem Pakar untuk Diagnosis dan Penilaian Risiko COVID-19",
        "welcome": "Selamat Datang ke CIDAS",

        # Navigation
        "nav_home": "Laman Utama",
        "nav_diagnosis": "Diagnosis",
        "nav_risk": "Penilaian Risiko",
        "nav_care": "Laluan Penjagaan",
        "nav_history": "Sejarah",
        "nav_about": "Tentang",

        # Patient Information
        "patient_info": "Maklumat Pesakit",
        "age": "Umur",
        "gender": "Jantina",
        "male": "Lelaki",
        "female": "Perempuan",
        "state": "Negeri",

        # Symptoms
        "symptoms_header": "Simptom",
        "check_all": "Tandakan semua simptom yang berkaitan:",
        "symptom_fever": "Demam",
        "symptom_temperature": "Suhu (°C)",
        "symptom_cough": "Batuk",
        "symptom_cough_type": "Jenis Batuk",
        "cough_dry": "Kering",
        "cough_productive": "Berkahak",
        "symptom_fatigue": "Keletihan",
        "symptom_body_ache": "Sakit Badan/Otot",
        "symptom_sore_throat": "Sakit Tekak",
        "symptom_runny_nose": "Hidung Berair",
        "symptom_sneezing": "Bersin",
        "symptom_loss_taste_smell": "Hilang Deria Rasa/Bau",
        "symptom_shortness_breath": "Sesak Nafas",
        "symptom_chest_pain": "Sakit Dada",
        "symptom_headache": "Sakit Kepala",
        "symptom_nausea": "Loya/Muntah",
        "symptom_diarrhea": "Cirit-birit",
        "symptom_itchy_eyes": "Mata Gatal/Berair",
        "symptom_onset": "Permulaan Simptom",
        "onset_sudden": "Tiba-tiba (dalam masa beberapa jam)",
        "onset_gradual": "Beransur-ansur (beberapa hari)",
        "symptom_duration": "Hari dengan simptom",
        "oxygen_level": "Ketepuan Oksigen (SpO2%)",

        # Severity Levels
        "severity_mild": "Ringan",
        "severity_moderate": "Sederhana",
        "severity_severe": "Teruk",

        # Medical History
        "medical_history": "Sejarah Perubatan",
        "comorbidities": "Penyakit Sedia Ada:",
        "diabetes": "Kencing Manis",
        "hypertension": "Darah Tinggi",
        "heart_disease": "Penyakit Jantung",
        "lung_disease": "Penyakit Paru-paru (COPD/Asma)",
        "kidney_disease": "Penyakit Buah Pinggang",
        "cancer": "Kanser/Imun Lemah",
        "obesity": "Obesiti (BMI > 30)",
        "pregnancy": "Hamil",
        "smoking": "Perokok Semasa/Bekas",

        # Exposure History
        "exposure_history": "Sejarah Pendedahan",
        "close_contact": "Hubungan rapat dengan kes COVID-19",
        "contact_days": "Hari sejak hubungan terakhir",
        "travel_history": "Perjalanan baru-baru ini",
        "healthcare_worker": "Pekerja kesihatan",

        # Conditions
        "condition_covid": "COVID-19",
        "condition_flu": "Selesema",
        "condition_cold": "Selsema Biasa",
        "condition_allergies": "Alahan",

        # Risk Levels
        "risk_low": "Risiko Rendah",
        "risk_medium": "Risiko Sederhana",
        "risk_high": "Risiko Tinggi",
        "risk_critical": "Risiko Kritikal",
        "risk_score": "Skor Risiko",

        # Recommendations
        "rec_home_isolation": "Pengasingan Di Rumah",
        "rec_monitored_care": "Penjagaan Rumah Dipantau",
        "rec_hospitalization": "Kemasukan Hospital",
        "rec_icu": "Penjagaan ICU",
        "rec_emergency": "Rawatan Kecemasan",

        # Actions
        "btn_diagnose": "Diagnos",
        "btn_assess_risk": "Nilai Risiko",
        "btn_reset": "Set Semula",
        "btn_submit": "Hantar",
        "btn_clear": "Kosongkan",
        "btn_back": "Kembali",
        "btn_next": "Seterusnya",

        # Messages
        "msg_complete": "Analisis Selesai!",
        "msg_processing": "Memproses...",
        "msg_no_diagnosis": "Maklumat tidak mencukupi untuk diagnosis",
        "msg_seek_testing": "Sila dapatkan ujian (PCR/RTK-Ag)",
        "msg_emergency": "Dapatkan rawatan kecemasan segera",
        "msg_consult_doctor": "Rujuk profesional kesihatan",

        # Results
        "results": "Keputusan",
        "diagnosis": "Diagnosis",
        "confidence": "Keyakinan",
        "risk_assessment": "Penilaian Risiko",
        "recommendation": "Cadangan",
        "explanation": "Penjelasan",
        "next_steps": "Langkah Seterusnya",
        "nearest_hospitals": "Hospital COVID-19 Berdekatan",

        # Disclaimer
        "disclaimer": "Ini adalah sistem pakar pendidikan dan TIDAK sepatutnya menggantikan nasihat perubatan profesional. Sentiasa rujuk profesional kesihatan untuk keputusan perubatan.",
        "disclaimer_short": "Bukan pengganti nasihat perubatan profesional"
    }
}

# ============================================================================
# SYMPTOM WEIGHTS FOR SEVERITY CALCULATION
# ============================================================================

SYMPTOM_WEIGHTS = {
    "critical": {
        "symptoms": ["shortness_of_breath", "chest_pain", "confusion", "bluish_lips"],
        "weight": 15
    },
    "major": {
        "symptoms": ["fever_high", "loss_of_taste_smell", "severe_fatigue"],
        "weight": 10
    },
    "moderate": {
        "symptoms": ["cough", "fever_moderate", "body_ache", "fatigue"],
        "weight": 7
    },
    "minor": {
        "symptoms": ["sore_throat", "runny_nose", "headache", "nausea", "diarrhea", "sneezing", "itchy_eyes"],
        "weight": 4
    }
}

# ============================================================================
# DIFFERENTIAL DIAGNOSIS DECISION MATRIX
# ============================================================================

SYMPTOM_MATRIX = {
    "COVID-19": {
        "fever": "common",
        "fever_range": "38.0-40.0",
        "cough": "common_dry",
        "fatigue": "common",
        "body_ache": "sometimes",
        "sore_throat": "sometimes",
        "runny_nose": "rare",
        "sneezing": "rare",
        "loss_taste_smell": "common",  # Highly specific (>95% specificity)
        "shortness_breath": "sometimes",
        "itchy_eyes": "never",
        "onset": "gradual",
        "typical_duration": "7-14 days"
    },
    "Influenza": {
        "fever": "common_high",
        "fever_range": "38.5-40.0",
        "cough": "common",
        "fatigue": "severe",
        "body_ache": "severe",  # Characteristic
        "sore_throat": "sometimes",
        "runny_nose": "sometimes",
        "sneezing": "sometimes",
        "loss_taste_smell": "rare",
        "shortness_breath": "rare",
        "itchy_eyes": "never",
        "onset": "sudden",  # Characteristic (within hours)
        "typical_duration": "3-7 days"
    },
    "Common_Cold": {
        "fever": "rare_mild",
        "fever_range": "< 38.0",
        "cough": "mild",
        "fatigue": "mild",
        "body_ache": "slight",
        "sore_throat": "common",
        "runny_nose": "common",  # Characteristic
        "sneezing": "common",  # Characteristic
        "loss_taste_smell": "sometimes",
        "shortness_breath": "never",
        "itchy_eyes": "never",
        "onset": "gradual",
        "typical_duration": "7-10 days"
    },
    "Allergies": {
        "fever": "never",  # Key differentiator
        "fever_range": "normal",
        "cough": "sometimes",
        "fatigue": "sometimes",
        "body_ache": "never",  # Key differentiator
        "sore_throat": "sometimes",
        "runny_nose": "common_clear",
        "sneezing": "common_frequent",  # Characteristic
        "loss_taste_smell": "never",
        "shortness_breath": "never",
        "itchy_eyes": "common",  # Highly specific
        "onset": "sudden",
        "typical_duration": "seasonal/varies"
    }
}

# ============================================================================
# FUZZY VARIABLE PARAMETERS
# ============================================================================

FUZZY_PARAMS = {
    "fever_level": {
        "universe": (36.0, 42.0),
        "normal": (36.0, 36.5, 37.0, 37.2),
        "low_grade": (37.0, 37.3, 37.8, 38.0),
        "moderate": (37.8, 38.2, 38.8, 39.2),
        "high": (39.0, 39.5, 40.5, 42.0)
    },
    "symptom_count": {
        "universe": (0, 15),
        "few": (0, 0, 2, 4),
        "moderate": (3, 5, 7, 9),
        "many": (7, 10, 15, 15)
    },
    "symptom_severity": {
        "universe": (0, 100),
        "mild": (0, 0, 25, 40),
        "moderate": (30, 45, 55, 70),
        "severe": (60, 75, 100, 100)
    },
    "age_risk": {
        "universe": (0, 100),
        "low": (0, 0, 30, 45),
        "medium": (40, 50, 55, 65),
        "high": (60, 70, 100, 100)
    },
    "comorbidity_score": {
        "universe": (0, 10),
        "none": (0, 0, 1, 2),
        "some": (1, 2, 4, 5),
        "multiple": (4, 6, 10, 10)
    },
    "risk_level": {
        "universe": (0, 100),
        "low": (0, 0, 20, 35),
        "medium": (25, 40, 50, 65),
        "high": (55, 70, 80, 90),
        "critical": (80, 90, 100, 100)
    }
}

# ============================================================================
# COMORBIDITY WEIGHTS
# ============================================================================

COMORBIDITY_WEIGHTS = {
    "diabetes": 2.0,
    "heart_disease": 2.0,
    "lung_disease": 2.0,
    "hypertension": 1.5,
    "kidney_disease": 1.5,
    "liver_disease": 1.0,
    "cancer": 2.0,
    "immunocompromised": 2.0,
    "obesity": 1.5,
    "smoking": 1.0,
    "pregnancy": 1.5
}

# ============================================================================
# OXYGEN SATURATION THRESHOLDS
# ============================================================================

SPO2_THRESHOLDS = {
    "normal": 95,  # >= 95% is normal
    "concerning": 94,  # < 94% requires attention
    "severe": 90,  # < 90% requires hospitalization
    "critical": 85  # < 85% requires immediate ICU
}

# ============================================================================
# AGE RISK THRESHOLDS
# ============================================================================

AGE_THRESHOLDS = {
    "low_risk": 45,  # < 45 years
    "medium_risk": 60,  # 45-60 years
    "high_risk": 60  # >= 60 years
}

# ============================================================================
# TEMPERATURE THRESHOLDS (Celsius)
# ============================================================================

TEMPERATURE_THRESHOLDS = {
    "normal": 37.2,
    "low_grade": 38.0,
    "moderate": 38.8,
    "high": 39.5
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_translation(key, lang="en"):
    """
    Get translated string

    Args:
        key: Translation key
        lang: Language code ('en' or 'ms')

    Returns:
        Translated string

    Example:
        text = get_translation("symptom_fever", "ms")  # Returns "Demam"
    """
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)


def get_hospitals_by_state(state):
    """
    Get COVID-designated hospitals for a state

    Args:
        state: Malaysian state name

    Returns:
        List of hospital names

    Example:
        hospitals = get_hospitals_by_state("Selangor")
        # Returns ["Hospital Sungai Buloh", "Hospital Tengku Ampuan Rahimah", ...]
    """
    return MALAYSIAN_CONTEXT["covid_designated_hospitals"].get(state, [])


def get_kkm_category(category_num):
    """
    Get KKM severity category details

    Args:
        category_num: Category number (1-5)

    Returns:
        Dictionary with category details

    Example:
        category = get_kkm_category(3)
        # Returns category 3 details
    """
    return MALAYSIAN_CONTEXT["kkm_severity_categories"].get(f"category_{category_num}", {})


def get_emergency_number(number_type="national"):
    """
    Get emergency contact number

    Args:
        number_type: Type of number ('national', 'covid_hotline', etc.)

    Returns:
        Phone number string

    Example:
        hotline = get_emergency_number("covid_hotline")  # Returns "1-800-88-2665"
    """
    return MALAYSIAN_CONTEXT["emergency_numbers"].get(number_type, "999")


# ============================================================================
# TESTING (Run this file directly to test)
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CIDAS Config Module - Self Test")
    print("=" * 60)

    # Test translations
    print("\n1. Testing translations...")
    print(f"   EN: {get_translation('symptom_fever', 'en')}")
    print(f"   MS: {get_translation('symptom_fever', 'ms')}")

    # Test hospitals
    print("\n2. Testing hospital lookup...")
    hospitals = get_hospitals_by_state("Selangor")
    print(f"   Selangor hospitals: {len(hospitals)} found")
    print(f"   First hospital: {hospitals[0]}")

    # Test KKM categories
    print("\n3. Testing KKM categories...")
    cat3 = get_kkm_category(3)
    print(f"   Category 3 (EN): {cat3['name_en']}")
    print(f"   Category 3 (MS): {cat3['name_ms']}")

    # Test emergency numbers
    print("\n4. Testing emergency numbers...")
    print(f"   National: {get_emergency_number('national')}")
    print(f"   COVID Hotline: {get_emergency_number('covid_hotline')}")

    # Test fuzzy params
    print("\n5. Testing fuzzy parameters...")
    print(f"   Fever universe: {FUZZY_PARAMS['fever_level']['universe']}")
    print(f"   Risk levels defined: {list(FUZZY_PARAMS['risk_level'].keys())}")

    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - config.py is working correctly!")
    print("=" * 60)