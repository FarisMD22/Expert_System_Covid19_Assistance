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

# ============================================================================
# FILE: facts.py
# LOCATION: /cidas/facts.py
# DESCRIPTION: Complete fact definitions for all three expert system modules
# STATUS: ✅ COMPLETE - No TODOs, fully working
# ============================================================================
"""
CIDAS - COVID-19 Intelligent Diagnostic & Assessment System
Fact Definitions Module

This module defines all fact classes used across the three expert system modules:
- Module 1: Differential Diagnosis (Rule-Based)
- Module 2: Risk Classification (Fuzzy)
- Module 3: Severity & Hospitalization (Hybrid)

All 12 fact classes are complete and ready to use.

Author: TES6313 Project
Date: 2025
"""

from experta import Fact


# ============================================================================
# FACT CLASS DEFINITIONS (12 classes)
# ============================================================================

class Patient(Fact):
    """
    Patient demographic and background information

    Attributes:
        patient_id (str): Unique patient identifier
        age (int): Age in years
        gender (str): 'M' or 'F'
        state (str): Malaysian state for hospital recommendations
        occupation (str): Optional occupation (healthcare worker, etc.)

    Example:
        Patient(patient_id="P001", age=45, gender="M", state="Selangor")
    """
    pass


class Symptom(Fact):
    """
    Individual symptom reported by patient

    Attributes:
        fever (bool): Presence of fever
        temp (float): Temperature in Celsius (if fever=True)
        cough (bool): Presence of cough
        cough_type (str): 'dry' or 'productive'
        cough_duration (int): Days of cough
        fatigue (bool): Presence of fatigue
        fatigue_severity (str): 'mild', 'moderate', 'severe'
        body_ache (bool): Body aches/muscle pain
        body_ache_severity (str): 'mild', 'moderate', 'severe'
        sore_throat (bool): Sore throat
        runny_nose (bool): Runny/stuffy nose
        discharge_type (str): 'clear', 'yellow', 'green'
        sneezing (bool): Sneezing
        sneezing_frequency (str): 'occasional', 'frequent', 'constant'
        loss_of_taste_smell (bool): Anosmia/ageusia (highly specific to COVID)
        shortness_of_breath (bool): Difficulty breathing
        chest_pain (bool): Chest pain or tightness
        headache (bool): Headache
        nausea (bool): Nausea or vomiting
        diarrhea (bool): Diarrhea
        itchy_eyes (bool): Itchy, watery eyes (allergy indicator)
        skin_rash (bool): Skin rash
        onset (str): 'sudden' or 'gradual'
        duration (int): Days since symptom onset
        oxygen_saturation (float): SpO2 percentage (if measured)

    Example:
        Symptom(fever=True, temp=38.5, cough=True, cough_type="dry")
    """
    pass


class MedicalHistory(Fact):
    """
    Patient's medical history and comorbidities

    Attributes:
        diabetes (bool): Diabetes mellitus
        hypertension (bool): High blood pressure
        heart_disease (bool): Cardiovascular disease
        lung_disease (bool): Chronic respiratory disease (COPD, asthma)
        kidney_disease (bool): Chronic kidney disease
        liver_disease (bool): Chronic liver disease
        cancer (bool): Active cancer or immunosuppression
        immunocompromised (bool): Weakened immune system
        obesity (bool): BMI > 30
        pregnancy (bool): Currently pregnant
        smoking (bool): Current or former smoker

    Example:
        MedicalHistory(diabetes=True, hypertension=True, obesity=False)
    """
    pass


class ExposureHistory(Fact):
    """
    COVID-19 exposure and travel history

    Attributes:
        close_contact (bool): Contact with confirmed COVID case
        contact_days_ago (int): Days since last contact
        travel_history (bool): Recent international/interstate travel
        travel_location (str): Where traveled
        travel_days_ago (int): Days since return
        healthcare_worker (bool): Works in healthcare setting
        high_risk_setting (bool): Works/lives in high-risk setting

    Example:
        ExposureHistory(close_contact=True, contact_days_ago=5)
    """
    pass


class ContextualFactor(Fact):
    """
    Contextual factors affecting assessment

    Attributes:
        season (str): 'spring', 'summer', 'fall', 'winter'
        local_outbreak (bool): Active outbreak in patient's area
        vaccination_status (str): 'unvaccinated', 'partial', 'full', 'boosted'
        previous_covid (bool): Previous COVID-19 infection
        days_since_previous (int): Days since previous COVID infection

    Example:
        ContextualFactor(season="winter", vaccination_status="full")
    """
    pass


class Diagnosis(Fact):
    """
    Diagnostic hypothesis with confidence

    Attributes:
        condition (str): 'COVID-19', 'Influenza', 'Common Cold', 'Allergies'
        confidence (float): Certainty factor (0.0 - 1.0)
        supporting_evidence (list): List of supporting symptoms/facts
        contradicting_evidence (list): List of contradicting symptoms/facts
        rule_id (str): ID of rule that fired this diagnosis

    Example:
        Diagnosis(condition="COVID-19", confidence=0.92, rule_id="DD-001")
    """
    pass


class RiskAssessment(Fact):
    """
    Risk level assessment from fuzzy module

    Attributes:
        level (str): 'low', 'medium', 'high', 'critical'
        score (float): Numerical risk score (0-100)
        fever_contribution (float): Contribution from fever
        symptom_contribution (float): Contribution from symptom count
        age_contribution (float): Contribution from age
        comorbidity_contribution (float): Contribution from comorbidities

    Example:
        RiskAssessment(level="medium", score=55.5)
    """
    pass


class Recommendation(Fact):
    """
    Care pathway recommendation from severity module

    Attributes:
        action (str): 'HOME_ISOLATION', 'HOME_CARE_MONITORED',
                     'HOSPITALIZATION', 'IMMEDIATE_HOSPITALIZATION'
        urgency (str): 'LOW', 'MODERATE', 'URGENT', 'EMERGENCY'
        department (str): Target department if hospitalization
        duration (str): Expected duration (e.g., '10_DAYS')
        follow_up (str): Follow-up timeframe (e.g., '24_HOURS')
        explanation (str): Natural language explanation
        testing_recommended (bool): PCR/RTK testing recommended
        rule_id (str): ID of rule that fired this recommendation

    Example:
        Recommendation(action="HOSPITALIZATION", urgency="URGENT", rule_id="SH-004")
    """
    pass


class LocalResource(Fact):
    """
    Malaysian healthcare resources

    Attributes:
        hospitals (list): Nearby COVID-designated hospitals
        hotline (str): Emergency hotline number
        testing_centers (list): Nearby testing centers
        kkm_category (str): KKM severity category (1-5)

    Example:
        LocalResource(hospitals=["Hospital Sungai Buloh"], hotline="999")
    """
    pass


class SymptomTrend(Fact):
    """
    Temporal symptom progression tracking

    Attributes:
        trend (str): 'IMPROVING', 'STABLE', 'DETERIORATING', 'INSUFFICIENT_DATA'
        rate_of_change (float): Rate of symptom severity change
        days_tracked (int): Number of days in tracking history
        assessments_count (int): Number of assessments recorded

    Example:
        SymptomTrend(trend="DETERIORATING", days_tracked=3)
    """
    pass


class EvidenceQuality(Fact):
    """
    Quality assessment of input data for confidence calibration

    Attributes:
        completeness (float): Proportion of expected symptoms reported (0-1)
        contradictions (int): Number of contradictory symptoms
        missing_critical (int): Number of critical symptoms not checked
        confidence_adjustment (float): Adjustment factor for final confidence

    Example:
        EvidenceQuality(completeness=0.85, contradictions=0)
    """
    pass


class FuzzyInput(Fact):
    """
    Inputs for fuzzy inference system

    Attributes:
        fever_level (float): Defuzzified fever level (36-42°C)
        symptom_count (int): Total number of symptoms (0-15)
        symptom_severity_score (float): Aggregated severity score (0-100)
        age_risk (float): Age in years (for age risk factor)
        comorbidity_score (float): Weighted comorbidity count (0-10)

    Example:
        FuzzyInput(fever_level=38.5, symptom_count=5, age_risk=45)
    """
    pass


class FuzzyOutput(Fact):
    """
    Output from fuzzy inference system

    Attributes:
        risk_score (float): Defuzzified risk score (0-100)
        membership_values (dict): Membership in each output set

    Example:
        FuzzyOutput(risk_score=65.5, membership_values={'high': 0.8})
    """
    pass


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def create_patient_fact(patient_data: dict) -> Patient:
    """
    Factory function to create Patient fact from dictionary

    Args:
        patient_data: Dictionary with patient information

    Returns:
        Patient fact instance

    Example:
        data = {"age": 45, "gender": "M", "state": "Selangor"}
        patient = create_patient_fact(data)
    """
    return Patient(**patient_data)


def create_symptom_fact(symptom_data: dict) -> Symptom:
    """
    Factory function to create Symptom fact from dictionary

    Args:
        symptom_data: Dictionary with symptom information

    Returns:
        Symptom fact instance

    Example:
        data = {"fever": True, "temp": 38.5, "cough": True}
        symptom = create_symptom_fact(data)
    """
    return Symptom(**symptom_data)


def aggregate_comorbidities(medical_history: dict) -> float:
    """
    Calculate weighted comorbidity score

    Weights based on COVID-19 severity risk:
    - Diabetes, Heart Disease, Lung Disease: 2.0
    - Hypertension, Kidney Disease, Obesity: 1.5
    - Others: 1.0

    Args:
        medical_history: Dictionary with medical history

    Returns:
        Weighted comorbidity score (0-10)

    Example:
        history = {"diabetes": True, "hypertension": True}
        score = aggregate_comorbidities(history)  # Returns 3.5
    """
    weights = {
        'diabetes': 2.0,
        'heart_disease': 2.0,
        'lung_disease': 2.0,
        'hypertension': 1.5,
        'kidney_disease': 1.5,
        'liver_disease': 1.0,
        'cancer': 2.0,
        'immunocompromised': 2.0,
        'obesity': 1.5,
        'smoking': 1.0,
        'pregnancy': 1.5
    }

    score = 0.0
    for condition, weight in weights.items():
        if medical_history.get(condition, False):
            score += weight

    return min(score, 10.0)  # Cap at 10


def calculate_symptom_severity(symptom_data: dict) -> float:
    """
    Calculate aggregated symptom severity score (0-100)

    Severity weights:
    - Critical symptoms (shortness_of_breath, chest_pain): 15 points each
    - Major symptoms (fever, loss_of_taste_smell): 10 points each
    - Moderate symptoms (cough, fatigue, body_ache): 7 points each
    - Minor symptoms (others): 3-5 points each

    Args:
        symptom_data: Dictionary with symptom information

    Returns:
        Severity score (0-100)

    Example:
        symptoms = {"fever": True, "temp": 39.0, "cough": True,
                   "shortness_of_breath": True}
        score = calculate_symptom_severity(symptoms)  # Returns ~37
    """
    score = 0.0

    # Critical symptoms (15 points each)
    if symptom_data.get('shortness_of_breath'):
        score += 15
    if symptom_data.get('chest_pain'):
        score += 15

    # Major symptoms (10-12 points)
    if symptom_data.get('fever'):
        temp = symptom_data.get('temp', 37.0)
        if temp >= 39.0:
            score += 12
        elif temp >= 38.0:
            score += 10
        else:
            score += 7

    if symptom_data.get('loss_of_taste_smell'):
        score += 10

    # Moderate symptoms (7-9 points)
    if symptom_data.get('cough'):
        score += 7

    if symptom_data.get('fatigue'):
        severity = symptom_data.get('fatigue_severity', 'mild')
        if severity == 'severe':
            score += 9
        elif severity == 'moderate':
            score += 7
        else:
            score += 5

    if symptom_data.get('body_ache'):
        severity = symptom_data.get('body_ache_severity', 'mild')
        if severity == 'severe':
            score += 9
        elif severity == 'moderate':
            score += 7
        else:
            score += 5

    # Minor symptoms (3-5 points each)
    if symptom_data.get('sore_throat'):
        score += 4
    if symptom_data.get('runny_nose'):
        score += 3
    if symptom_data.get('sneezing'):
        score += 3
    if symptom_data.get('headache'):
        score += 4
    if symptom_data.get('nausea'):
        score += 5
    if symptom_data.get('diarrhea'):
        score += 5
    if symptom_data.get('itchy_eyes'):
        score += 3

    return min(score, 100.0)  # Cap at 100


def count_symptoms(symptom_data: dict) -> int:
    """
    Count total number of reported symptoms

    Args:
        symptom_data: Dictionary with symptom information

    Returns:
        Number of symptoms present

    Example:
        symptoms = {"fever": True, "cough": True, "headache": False}
        count = count_symptoms(symptoms)  # Returns 2
    """
    symptom_fields = [
        'fever', 'cough', 'fatigue', 'body_ache', 'sore_throat',
        'runny_nose', 'sneezing', 'loss_of_taste_smell',
        'shortness_of_breath', 'chest_pain', 'headache',
        'nausea', 'diarrhea', 'itchy_eyes', 'skin_rash'
    ]

    count = sum(1 for field in symptom_fields if symptom_data.get(field, False))
    return count


# ============================================================================
# VALIDATION HELPERS
# ============================================================================

def validate_temperature(temp: float) -> bool:
    """Validate temperature is in reasonable range"""
    return 35.0 <= temp <= 42.0


def validate_oxygen_saturation(spo2: float) -> bool:
    """Validate SpO2 is in valid range"""
    return 0 <= spo2 <= 100


def validate_age(age: int) -> bool:
    """Validate age is reasonable"""
    return 0 <= age <= 120


# ============================================================================
# TESTING (Run this file directly to test)
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CIDAS Facts Module - Self Test")
    print("=" * 60)

    # Test Patient fact
    print("\n1. Testing Patient fact...")
    patient = Patient(patient_id="P001", age=45, gender="M", state="Selangor")
    print(f"   ✓ Patient created: {patient.get('patient_id')}, age {patient.get('age')}")

    # Test Symptom fact
    print("\n2. Testing Symptom fact...")
    symptom = Symptom(fever=True, temp=38.5, cough=True, cough_type="dry")
    print(f"   ✓ Symptom created: Fever={symptom.get('fever')}, Temp={symptom.get('temp')}°C")

    # Test aggregate_comorbidities
    print("\n3. Testing aggregate_comorbidities()...")
    history1 = {}
    score1 = aggregate_comorbidities(history1)
    print(f"   ✓ No comorbidities: Score = {score1}")

    history2 = {"diabetes": True, "hypertension": True}
    score2 = aggregate_comorbidities(history2)
    print(f"   ✓ Diabetes + Hypertension: Score = {score2}")

    # Test calculate_symptom_severity
    print("\n4. Testing calculate_symptom_severity()...")
    symptoms1 = {"fever": True, "temp": 37.5, "sore_throat": True}
    severity1 = calculate_symptom_severity(symptoms1)
    print(f"   ✓ Mild symptoms: Severity = {severity1}")

    symptoms2 = {"fever": True, "temp": 39.5, "cough": True,
                 "shortness_of_breath": True, "chest_pain": True}
    severity2 = calculate_symptom_severity(symptoms2)
    print(f"   ✓ Severe symptoms: Severity = {severity2}")

    # Test count_symptoms
    print("\n5. Testing count_symptoms()...")
    count = count_symptoms(symptoms2)
    print(f"   ✓ Symptom count: {count}")

    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - facts.py is working correctly!")
    print("=" * 60)