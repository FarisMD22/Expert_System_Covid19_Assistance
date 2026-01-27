"""
Quick test for SeverityEngine to verify rules fire correctly
"""

from facts import RiskAssessment, Patient, MedicalHistory
from engine import SeverityEngine


def test_medium_risk_young():
    """Test medium risk, age 45, no comorbidities"""
    print("\n" + "=" * 70)
    print("TEST 1: Medium Risk, Age 45, No Comorbidities")
    print("=" * 70)

    engine = SeverityEngine()
    engine.reset()

    # Declare facts
    engine.declare(RiskAssessment(level="medium", score=45.0))
    engine.declare(Patient(age=45))

    # Run engine
    engine.run()

    # Get recommendation
    recommendation = engine.get_recommendation()

    if recommendation:
        print(f"✓ Recommendation generated!")
        print(f"  Action: {recommendation['action']}")
        print(f"  Urgency: {recommendation['urgency']}")
        print(f"  Rule: {recommendation['rule_id']}")
        print(f"  Explanation: {recommendation['explanation']}")
    else:
        print("✗ No recommendation generated")
        print(f"  Facts in working memory: {list(engine.facts.values())}")
        print(f"  Fired rules: {engine.fired_rules}")


def test_medium_risk_elderly():
    """Test medium risk, age 70, no comorbidities"""
    print("\n" + "=" * 70)
    print("TEST 2: Medium Risk, Age 70, No Comorbidities")
    print("=" * 70)

    engine = SeverityEngine()
    engine.reset()

    # Declare facts
    engine.declare(RiskAssessment(level="medium", score=45.0))
    engine.declare(Patient(age=70))

    # Run engine
    engine.run()

    # Get recommendation
    recommendation = engine.get_recommendation()

    if recommendation:
        print(f"✓ Recommendation generated!")
        print(f"  Action: {recommendation['action']}")
        print(f"  Urgency: {recommendation['urgency']}")
        print(f"  Rule: {recommendation['rule_id']}")
        print(f"  Explanation: {recommendation['explanation']}")
    else:
        print("✗ No recommendation generated")


def test_low_risk():
    """Test low risk"""
    print("\n" + "=" * 70)
    print("TEST 3: Low Risk, Age 30")
    print("=" * 70)

    engine = SeverityEngine()
    engine.reset()

    # Declare facts
    engine.declare(RiskAssessment(level="low", score=25.0))
    engine.declare(Patient(age=30))

    # Run engine
    engine.run()

    # Get recommendation
    recommendation = engine.get_recommendation()

    if recommendation:
        print(f"✓ Recommendation generated!")
        print(f"  Action: {recommendation['action']}")
        print(f"  Urgency: {recommendation['urgency']}")
        print(f"  Rule: {recommendation['rule_id']}")
        print(f"  Explanation: {recommendation['explanation']}")
    else:
        print("✗ No recommendation generated")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SEVERITY ENGINE TESTS")
    print("=" * 70)

    test_medium_risk_young()
    test_medium_risk_elderly()
    test_low_risk()

    print("\n" + "=" * 70)
    print("TESTS COMPLETE")
    print("=" * 70)
    print()