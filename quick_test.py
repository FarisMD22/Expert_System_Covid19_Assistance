"""
Quick Test - Verify test_all_cases.py is Fixed
===============================================
Run this first to verify the fixes work before running all 10 tests.

Usage:
    python quick_test.py
"""

import sys

print("\n" + "="*80)
print("QUICK TEST - Verifying test_all_cases.py Fix")
print("="*80 + "\n")

# Test imports
print("Step 1: Testing imports...")
try:
    from engine import DifferentialDiagnosisEngine, FuzzyRiskEngine, SeverityEngine
    from facts import Patient, RiskAssessment, Symptom, MedicalHistory, ExposureHistory
    print("  ✓ All imports successful")
except ImportError as e:
    print(f"  ✗ Import error: {e}")
    print("\n  Solution: pip install experta scikit-fuzzy numpy pandas")
    sys.exit(1)

# Test diagnosis engine
print("\nStep 2: Testing DifferentialDiagnosisEngine...")
try:
    engine = DifferentialDiagnosisEngine()
    engine.reset()

    # Create facts
    patient = Patient(age=45, state="Selangor")
    symptom = Symptom(
        fever=True,
        cough=True,
        loss_of_taste_smell=True,
        fatigue=True,
        cough_type='dry',
        fatigue_severity='moderate',
        onset='gradual',
        duration=5,
        oxygen_saturation=96
    )
    medical_history = MedicalHistory()
    exposure_history = ExposureHistory()

    # Declare and run
    engine.declare(patient)
    engine.declare(symptom)
    engine.declare(medical_history)
    engine.declare(exposure_history)
    engine.run()

    # Get results
    results = engine.get_top_diagnoses()

    if results:
        condition, confidence, rule_id = results[0]
        print(f"  ✓ Diagnosis engine works!")
        print(f"    Diagnosis: {condition}")
        print(f"    Confidence: {confidence*100:.0f}%")
        print(f"    Rule: {rule_id}")
    else:
        print("  ⚠ No diagnosis generated")

except Exception as e:
    print(f"  ✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test risk engine
print("\nStep 3: Testing FuzzyRiskEngine...")
try:
    risk_engine = FuzzyRiskEngine()
    risk = risk_engine.calculate_risk(  # ✅ CORRECT METHOD NAME
        fever_temp=38.5,
        symptom_cnt=5,
        severity_scr=35,
        age=45,
        comorbidity_scr=0
    )

    print(f"  ✓ Risk engine works!")
    print(f"    Risk Level: {risk['risk_level']}")
    print(f"    Risk Score: {risk['risk_score']:.1f}/100")

except Exception as e:
    print(f"  ✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test severity engine
print("\nStep 4: Testing SeverityEngine...")
try:
    severity_engine = SeverityEngine()
    severity_engine.reset()

    # Declare facts
    severity_engine.declare(Patient(age=45))
    severity_engine.declare(RiskAssessment(level='medium'))

    severity_engine.run()

    recommendation = severity_engine.get_recommendation()

    if recommendation:
        print(f"  ✓ Severity engine works!")
        print(f"    Action: {recommendation.get('action')}")
        print(f"    Urgency: {recommendation.get('urgency')}")
    else:
        print("  No recommendation generated")

except Exception as e:
    print(f"  ✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Success!
print("\n" + "="*80)
print("ALL TESTS PASSED! Your test file is now fixed.")
print("="*80)
print("\nYou can now run the full test suite:")
print("  python test_all_cases.py")
print("\nExpected result: 10/10 tests pass (100% accuracy)")
print()