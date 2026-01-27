#!/usr/bin/env python3
"""
Generate Academic Figures for CIDAS Expert System
Creates visualizations for certainty factors, decision trees, fuzzy logic, and knowledge representation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np
import os

# Create output directory
os.makedirs('../figures_academic', exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10


# ============================================================================
# FIGURE 1: CERTAINTY FACTOR CALCULATION
# ============================================================================

def create_certainty_factor_diagram():
    """Shows how confidence/certainty factors are calculated in diagnosis"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.5, 'Certainty Factor Calculation in CIDAS',
            ha='center', fontsize=14, fontweight='bold')

    # Input symptoms box
    input_box = FancyBboxPatch((0.5, 7), 3, 1.5,
                               boxstyle="round,pad=0.1",
                               edgecolor='blue', facecolor='lightblue', linewidth=2)
    ax.add_patch(input_box)
    ax.text(2, 8.2, 'Input Symptoms', ha='center', fontweight='bold', fontsize=11)
    ax.text(2, 7.8, '• Loss of taste/smell', ha='center', fontsize=9)
    ax.text(2, 7.5, '• Dry cough', ha='center', fontsize=9)
    ax.text(2, 7.2, '• Fever', ha='center', fontsize=9)

    # Rule matching box
    rule_box = FancyBboxPatch((0.5, 4.8), 3, 1.8,
                              boxstyle="round,pad=0.1",
                              edgecolor='green', facecolor='lightgreen', linewidth=2)
    ax.add_patch(rule_box)
    ax.text(2, 6.2, 'Rule Matching', ha='center', fontweight='bold', fontsize=11)
    ax.text(2, 5.85, 'Rule DD-01:', ha='center', fontsize=9, style='italic')
    ax.text(2, 5.55, 'IF loss_of_taste_smell', ha='center', fontsize=8)
    ax.text(2, 5.3, 'THEN COVID-19', ha='center', fontsize=8)
    ax.text(2, 5.05, 'CF = 0.88 (88%)', ha='center', fontsize=9, fontweight='bold', color='red')

    # CF adjustment box
    cf_box = FancyBboxPatch((0.5, 2.5), 3, 2,
                            boxstyle="round,pad=0.1",
                            edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax.add_patch(cf_box)
    ax.text(2, 4.1, 'CF Adjustment', ha='center', fontweight='bold', fontsize=11)
    ax.text(2, 3.75, 'Base CF: 0.88', ha='center', fontsize=9)
    ax.text(2, 3.45, '+ Supporting evidence:', ha='center', fontsize=9)
    ax.text(2, 3.2, '  Dry cough (+0.05)', ha='center', fontsize=8)
    ax.text(2, 2.95, '  Fever (+0.03)', ha='center', fontsize=8)
    ax.text(2, 2.7, 'Final CF: 0.95 (95%)', ha='center', fontsize=9,
            fontweight='bold', color='darkgreen')

    # Output box
    output_box = FancyBboxPatch((0.5, 0.5), 3, 1.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='purple', facecolor='lavender', linewidth=2)
    ax.add_patch(output_box)
    ax.text(2, 1.7, 'Diagnosis Output', ha='center', fontweight='bold', fontsize=11)
    ax.text(2, 1.3, 'COVID-19', ha='center', fontsize=10, fontweight='bold')
    ax.text(2, 0.95, 'Confidence: 95%', ha='center', fontsize=9, color='darkgreen')
    ax.text(2, 0.65, 'Rule: DD-01', ha='center', fontsize=8, style='italic')

    # Arrows
    arrow1 = FancyArrowPatch((2, 7), (2, 6.6), arrowstyle='->', lw=2, color='black')
    arrow2 = FancyArrowPatch((2, 4.8), (2, 4.5), arrowstyle='->', lw=2, color='black')
    arrow3 = FancyArrowPatch((2, 2.5), (2, 2), arrowstyle='->', lw=2, color='black')
    ax.add_patch(arrow1)
    ax.add_patch(arrow2)
    ax.add_patch(arrow3)

    # CF Formula box (right side)
    formula_box = FancyBboxPatch((5.5, 5.5), 4, 3,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='navy', facecolor='aliceblue', linewidth=2)
    ax.add_patch(formula_box)
    ax.text(7.5, 8.2, 'Certainty Factor Formula', ha='center',
            fontweight='bold', fontsize=11)

    # Formula
    ax.text(7.5, 7.6, 'CF(H,E) = CF(H) × CF(E)', ha='center', fontsize=10,
            family='monospace', style='italic')
    ax.text(7.5, 7.2, 'Where:', ha='center', fontsize=9)
    ax.text(7.5, 6.9, 'H = Hypothesis (diagnosis)', ha='center', fontsize=8)
    ax.text(7.5, 6.6, 'E = Evidence (symptoms)', ha='center', fontsize=8)
    ax.text(7.5, 6.3, 'CF(H) = Base confidence', ha='center', fontsize=8)
    ax.text(7.5, 6.0, 'CF(E) = Evidence strength', ha='center', fontsize=8)

    # Combining rules
    ax.text(7.5, 5.5, 'Combining Multiple CFs:', ha='center', fontsize=9, fontweight='bold')
    ax.text(7.5, 5.2, 'CF_combined = CF₁ + CF₂(1 - CF₁)', ha='center',
            fontsize=9, family='monospace')

    # Example calculation
    calc_box = FancyBboxPatch((5.5, 1.5), 4, 3.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='darkred', facecolor='mistyrose', linewidth=2)
    ax.add_patch(calc_box)
    ax.text(7.5, 4.7, 'Example Calculation', ha='center', fontweight='bold', fontsize=11)
    ax.text(7.5, 4.3, 'Symptom: Loss of taste/smell', ha='center', fontsize=9)
    ax.text(7.5, 4.0, 'Rule CF: 0.88', ha='center', fontsize=9)
    ax.text(7.5, 3.7, '+ Dry cough (0.70)', ha='center', fontsize=8)
    ax.text(7.5, 3.45, 'Combined:', ha='center', fontsize=9, fontweight='bold')
    ax.text(7.5, 3.15, '0.88 + 0.70(1-0.88)', ha='center', fontsize=9, family='monospace')
    ax.text(7.5, 2.85, '= 0.88 + 0.084', ha='center', fontsize=9, family='monospace')
    ax.text(7.5, 2.55, '= 0.964 ≈ 0.95', ha='center', fontsize=9, family='monospace',
            fontweight='bold', color='darkgreen')
    ax.text(7.5, 2.2, 'Final Confidence: 95%', ha='center', fontsize=10,
            fontweight='bold', color='darkgreen')
    ax.text(7.5, 1.85, '(High confidence diagnosis)', ha='center', fontsize=8, style='italic')

    plt.tight_layout()
    plt.savefig('figures_academic/01_certainty_factor_calculation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: 01_certainty_factor_calculation.png")


# ============================================================================
# FIGURE 2: DECISION TREE FOR DIAGNOSIS
# ============================================================================

def create_decision_tree():
    """Creates decision tree showing diagnostic logic"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Decision Tree for COVID-19 Diagnosis',
            ha='center', fontsize=14, fontweight='bold')

    # Root node
    root = FancyBboxPatch((5.5, 8.5), 3, 0.6,
                          boxstyle="round,pad=0.05",
                          edgecolor='black', facecolor='lightgray', linewidth=2)
    ax.add_patch(root)
    ax.text(7, 8.8, 'Patient Symptoms?', ha='center', fontweight='bold')

    # Level 1: Loss of taste/smell
    # Yes branch
    taste_yes = FancyBboxPatch((0.5, 7), 2.5, 0.6,
                               boxstyle="round,pad=0.05",
                               edgecolor='darkgreen', facecolor='lightgreen', linewidth=2)
    ax.add_patch(taste_yes)
    ax.text(1.75, 7.3, 'Loss of taste/smell?', ha='center', fontsize=9, fontweight='bold')

    # No branch
    taste_no = FancyBboxPatch((4, 7), 2.5, 0.6,
                              boxstyle="round,pad=0.05",
                              edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax.add_patch(taste_no)
    ax.text(5.25, 7.3, 'Dry cough?', ha='center', fontsize=9, fontweight='bold')

    # Other symptoms branch
    other = FancyBboxPatch((7.5, 7), 2.5, 0.6,
                           boxstyle="round,pad=0.05",
                           edgecolor='blue', facecolor='lightblue', linewidth=2)
    ax.add_patch(other)
    ax.text(8.75, 7.3, 'Itchy eyes?', ha='center', fontsize=9, fontweight='bold')

    # Sneezing branch
    sneeze = FancyBboxPatch((11, 7), 2.5, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor='purple', facecolor='lavender', linewidth=2)
    ax.add_patch(sneeze)
    ax.text(12.25, 7.3, 'Runny nose?', ha='center', fontsize=9, fontweight='bold')

    # Arrows from root
    ax.plot([6.5, 1.75], [8.5, 7.6], 'k-', lw=1.5)
    ax.plot([7, 5.25], [8.5, 7.6], 'k-', lw=1.5)
    ax.plot([7.5, 8.75], [8.5, 7.6], 'k-', lw=1.5)
    ax.plot([8, 12.25], [8.5, 7.6], 'k-', lw=1.5)

    ax.text(4, 8, 'YES', fontsize=8, style='italic', color='green')
    ax.text(6, 8, 'NO', fontsize=8, style='italic', color='red')
    ax.text(8, 8, 'NO', fontsize=8, style='italic', color='red')
    ax.text(10, 8, 'NO', fontsize=8, style='italic', color='red')

    # Level 2: Outcomes
    # COVID-19
    covid = FancyBboxPatch((0.5, 5.5), 2.5, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor='darkred', facecolor='lightcoral', linewidth=3)
    ax.add_patch(covid)
    ax.text(1.75, 6.1, 'COVID-19', ha='center', fontsize=10, fontweight='bold')
    ax.text(1.75, 5.8, 'CF: 88-95%', ha='center', fontsize=8, color='darkred')

    # Fever check for cough branch
    fever = FancyBboxPatch((4, 5.5), 2.5, 0.6,
                           boxstyle="round,pad=0.05",
                           edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax.add_patch(fever)
    ax.text(5.25, 5.8, 'Fever + SOB?', ha='center', fontsize=9)

    # Allergies
    allergy = FancyBboxPatch((7.5, 5.5), 2.5, 0.8,
                             boxstyle="round,pad=0.05",
                             edgecolor='blue', facecolor='lightblue', linewidth=3)
    ax.add_patch(allergy)
    ax.text(8.75, 6.1, 'Allergies', ha='center', fontsize=10, fontweight='bold')
    ax.text(8.75, 5.8, 'CF: 70-80%', ha='center', fontsize=8, color='darkblue')

    # Common Cold
    cold = FancyBboxPatch((11, 5.5), 2.5, 0.8,
                          boxstyle="round,pad=0.05",
                          edgecolor='purple', facecolor='lavender', linewidth=3)
    ax.add_patch(cold)
    ax.text(12.25, 6.1, 'Common Cold', ha='center', fontsize=10, fontweight='bold')
    ax.text(12.25, 5.8, 'CF: 70-85%', ha='center', fontsize=8, color='purple')

    # Arrows to outcomes
    ax.plot([1.75, 1.75], [7, 6.3], 'k-', lw=1.5)
    ax.plot([5.25, 5.25], [7, 6.1], 'k-', lw=1.5)
    ax.plot([8.75, 8.75], [7, 6.3], 'k-', lw=1.5)
    ax.plot([12.25, 12.25], [7, 6.3], 'k-', lw=1.5)

    # Level 3: Fever branch outcomes
    # COVID possible
    covid2 = FancyBboxPatch((3, 4), 1.5, 0.7,
                            boxstyle="round,pad=0.05",
                            edgecolor='darkred', facecolor='lightcoral', linewidth=2)
    ax.add_patch(covid2)
    ax.text(3.75, 4.5, 'COVID-19', ha='center', fontsize=9, fontweight='bold')
    ax.text(3.75, 4.2, 'CF: 70-85%', ha='center', fontsize=7)

    # Influenza
    flu = FancyBboxPatch((5.5, 4), 1.5, 0.7,
                         boxstyle="round,pad=0.05",
                         edgecolor='darkorange', facecolor='peachpuff', linewidth=2)
    ax.add_patch(flu)
    ax.text(6.25, 4.5, 'Influenza', ha='center', fontsize=9, fontweight='bold')
    ax.text(6.25, 4.2, 'CF: 75-90%', ha='center', fontsize=7)

    # Arrows
    ax.plot([4.75, 3.75], [5.5, 4.7], 'k-', lw=1.5)
    ax.plot([5.75, 6.25], [5.5, 4.7], 'k-', lw=1.5)
    ax.text(4, 5, 'YES', fontsize=7, style='italic', color='green')
    ax.text(6, 5, 'NO+\nBody ache', fontsize=7, style='italic', color='orange')

    # Legend
    legend_box = FancyBboxPatch((0.5, 0.5), 13, 2.8,
                                boxstyle="round,pad=0.1",
                                edgecolor='gray', facecolor='whitesmoke', linewidth=1)
    ax.add_patch(legend_box)

    ax.text(7, 3, 'Decision Rules & Certainty Factors', ha='center',
            fontsize=11, fontweight='bold')

    ax.text(2, 2.5, 'High Certainty (CF > 85%):', fontsize=9, fontweight='bold')
    ax.text(2, 2.2, '• Anosmia (loss of taste/smell) → COVID-19', fontsize=8)
    ax.text(2, 1.95, '• Signature symptoms present', fontsize=8)

    ax.text(7, 2.5, 'Medium Certainty (CF 70-85%):', fontsize=9, fontweight='bold')
    ax.text(7, 2.2, '• Classic symptom patterns', fontsize=8)
    ax.text(7, 1.95, '• Dry cough + fever + fatigue', fontsize=8)
    ax.text(7, 1.7, '• Body ache + sudden onset → Flu', fontsize=8)

    ax.text(12, 2.5, 'Lower Certainty (CF < 70%):', fontsize=9, fontweight='bold')
    ax.text(12, 2.2, '• Minimal symptoms', fontsize=8)
    ax.text(12, 1.95, '• Contradictory patterns', fontsize=8)
    ax.text(12, 1.7, '• Insufficient information', fontsize=8)

    ax.text(7, 1.2, 'Abbreviations: SOB = Shortness of Breath, CF = Certainty Factor',
            ha='center', fontsize=8, style='italic')
    ax.text(7, 0.9, 'Note: Multiple evidence can increase CF through combination formula',
            ha='center', fontsize=8, style='italic')

    plt.tight_layout()
    plt.savefig('figures_academic/02_decision_tree_diagnosis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: 02_decision_tree_diagnosis.png")


# ============================================================================
# FIGURE 3: FUZZY MEMBERSHIP FUNCTIONS
# ============================================================================

def create_fuzzy_membership_functions():
    """Display fuzzy knowledge - membership functions"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle('Fuzzy Membership Functions in CIDAS', fontsize=14, fontweight='bold')

    # Temperature
    ax = axes[0, 0]
    temp = np.linspace(36, 42, 100)
    ax.plot(temp, np.maximum(0, np.minimum(1, (38 - temp) / 2)), 'b-', label='Normal', linewidth=2)
    ax.plot(temp, np.maximum(0, np.minimum((temp - 37) / 1, (39 - temp) / 1)), 'g-', label='Mild', linewidth=2)
    ax.plot(temp, np.maximum(0, np.minimum((temp - 38) / 1, (40 - temp) / 1)), 'orange', label='Moderate', linewidth=2)
    ax.plot(temp, np.maximum(0, (temp - 39) / 2), 'r-', label='Severe', linewidth=2)
    ax.set_xlabel('Temperature (°C)', fontweight='bold')
    ax.set_ylabel('Membership Degree', fontweight='bold')
    ax.set_title('Fever Temperature', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.1, 1.1)

    # Symptom Count
    ax = axes[0, 1]
    symp = np.linspace(0, 10, 100)
    ax.plot(symp, np.maximum(0, (3 - symp) / 3), 'b-', label='Few', linewidth=2)
    ax.plot(symp, np.maximum(0, np.minimum((symp - 2) / 2, (6 - symp) / 2)), 'g-', label='Moderate', linewidth=2)
    ax.plot(symp, np.maximum(0, (symp - 5) / 5), 'r-', label='Many', linewidth=2)
    ax.set_xlabel('Number of Symptoms', fontweight='bold')
    ax.set_ylabel('Membership Degree', fontweight='bold')
    ax.set_title('Symptom Count', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.1, 1.1)

    # Age Risk
    ax = axes[0, 2]
    age = np.linspace(0, 100, 100)
    ax.plot(age, np.maximum(0, (45 - age) / 45), 'b-', label='Low', linewidth=2)
    ax.plot(age, np.maximum(0, np.minimum((age - 30) / 30, (70 - age) / 30)), 'g-', label='Medium', linewidth=2)
    ax.plot(age, np.maximum(0, (age - 60) / 40), 'r-', label='High', linewidth=2)
    ax.set_xlabel('Age (years)', fontweight='bold')
    ax.set_ylabel('Membership Degree', fontweight='bold')
    ax.set_title('Age Risk Factor', fontweight='bold')
    ax.legend(loc='upper left', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.1, 1.1)

    # Severity Score
    ax = axes[1, 0]
    sev = np.linspace(0, 100, 100)
    ax.plot(sev, np.maximum(0, (30 - sev) / 30), 'b-', label='Mild', linewidth=2)
    ax.plot(sev, np.maximum(0, np.minimum((sev - 20) / 30, (60 - sev) / 20)), 'g-', label='Moderate', linewidth=2)
    ax.plot(sev, np.maximum(0, np.minimum((sev - 50) / 20, (80 - sev) / 15)), 'orange', label='Severe', linewidth=2)
    ax.plot(sev, np.maximum(0, (sev - 75) / 25), 'r-', label='Critical', linewidth=2)
    ax.set_xlabel('Severity Score', fontweight='bold')
    ax.set_ylabel('Membership Degree', fontweight='bold')
    ax.set_title('Symptom Severity', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.1, 1.1)

    # Risk Level Output
    ax = axes[1, 1]
    risk = np.linspace(0, 100, 100)
    ax.plot(risk, np.maximum(0, (35 - risk) / 35), 'b-', label='Low', linewidth=2)
    ax.plot(risk, np.maximum(0, np.minimum((risk - 25) / 20, (70 - risk) / 20)), 'g-', label='Medium', linewidth=2)
    ax.plot(risk, np.maximum(0, np.minimum((risk - 60) / 15, (85 - risk) / 10)), 'orange', label='High', linewidth=2)
    ax.plot(risk, np.maximum(0, (risk - 80) / 20), 'r-', label='Critical', linewidth=2)
    ax.set_xlabel('Risk Score', fontweight='bold')
    ax.set_ylabel('Membership Degree', fontweight='bold')
    ax.set_title('Overall Risk Level', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.1, 1.1)

    # Oxygen Saturation
    ax = axes[1, 2]
    o2 = np.linspace(70, 100, 100)
    ax.plot(o2, np.maximum(0, (90 - o2) / 20), 'r-', label='Critical', linewidth=2)
    ax.plot(o2, np.maximum(0, np.minimum((o2 - 85) / 5, (94 - o2) / 4)), 'orange', label='Low', linewidth=2)
    ax.plot(o2, np.maximum(0, np.minimum((o2 - 92) / 3, (96 - o2) / 2)), 'g-', label='Borderline', linewidth=2)
    ax.plot(o2, np.maximum(0, (o2 - 95) / 5), 'b-', label='Normal', linewidth=2)
    ax.set_xlabel('SpO2 (%)', fontweight='bold')
    ax.set_ylabel('Membership Degree', fontweight='bold')
    ax.set_title('Oxygen Saturation', fontweight='bold')
    ax.legend(loc='upper left', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.1, 1.1)

    plt.tight_layout()
    plt.savefig('figures_academic/03_fuzzy_membership_functions.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: 03_fuzzy_membership_functions.png")


# ============================================================================
# FIGURE 4: RDF/CLASS HIERARCHY
# ============================================================================

def create_rdf_class_diagram():
    """RDF/Ontology-style class diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Knowledge Representation - Class Hierarchy (RDF-style)',
            ha='center', fontsize=14, fontweight='bold')

    # Top level - Fact
    fact_box = FancyBboxPatch((5.5, 8.5), 3, 0.6,
                              boxstyle="round,pad=0.05",
                              edgecolor='black', facecolor='lightgray', linewidth=3)
    ax.add_patch(fact_box)
    ax.text(7, 8.8, 'Fact (Base Class)', ha='center', fontweight='bold', fontsize=11)

    # Level 1 - Main Classes
    # Patient
    patient_box = FancyBboxPatch((0.5, 7), 2, 0.7,
                                 boxstyle="round,pad=0.05",
                                 edgecolor='blue', facecolor='lightblue', linewidth=2)
    ax.add_patch(patient_box)
    ax.text(1.5, 7.5, 'Patient', ha='center', fontweight='bold', fontsize=10)
    ax.text(1.5, 7.2, 'rdf:type Fact', ha='center', fontsize=7, style='italic')

    # Symptom
    symptom_box = FancyBboxPatch((3, 7), 2, 0.7,
                                 boxstyle="round,pad=0.05",
                                 edgecolor='green', facecolor='lightgreen', linewidth=2)
    ax.add_patch(symptom_box)
    ax.text(4, 7.5, 'Symptom', ha='center', fontweight='bold', fontsize=10)
    ax.text(4, 7.2, 'rdf:type Fact', ha='center', fontsize=7, style='italic')

    # MedicalHistory
    med_box = FancyBboxPatch((5.5, 7), 2.5, 0.7,
                             boxstyle="round,pad=0.05",
                             edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax.add_patch(med_box)
    ax.text(6.75, 7.5, 'MedicalHistory', ha='center', fontweight='bold', fontsize=10)
    ax.text(6.75, 7.2, 'rdf:type Fact', ha='center', fontsize=7, style='italic')

    # ExposureHistory
    exp_box = FancyBboxPatch((8.5, 7), 2.2, 0.7,
                             boxstyle="round,pad=0.05",
                             edgecolor='purple', facecolor='lavender', linewidth=2)
    ax.add_patch(exp_box)
    ax.text(9.6, 7.5, 'ExposureHistory', ha='center', fontweight='bold', fontsize=10)
    ax.text(9.6, 7.2, 'rdf:type Fact', ha='center', fontsize=7, style='italic')

    # Diagnosis
    diag_box = FancyBboxPatch((11.2, 7), 2, 0.7,
                              boxstyle="round,pad=0.05",
                              edgecolor='red', facecolor='lightcoral', linewidth=2)
    ax.add_patch(diag_box)
    ax.text(12.2, 7.5, 'Diagnosis', ha='center', fontweight='bold', fontsize=10)
    ax.text(12.2, 7.2, 'rdf:type Fact', ha='center', fontsize=7, style='italic')

    # Arrows from Fact
    ax.plot([6.5, 1.5], [8.5, 7.7], 'k-', lw=1.5)
    ax.plot([7, 4], [8.5, 7.7], 'k-', lw=1.5)
    ax.plot([7, 6.75], [8.5, 7.7], 'k-', lw=1.5)
    ax.plot([7.5, 9.6], [8.5, 7.7], 'k-', lw=1.5)
    ax.plot([8, 12.2], [8.5, 7.7], 'k-', lw=1.5)

    # Instance level - Patient attributes
    patient_attr = FancyBboxPatch((0.2, 5.5), 2.6, 1.2,
                                  boxstyle="round,pad=0.05",
                                  edgecolor='blue', facecolor='aliceblue', linewidth=1)
    ax.add_patch(patient_attr)
    ax.text(1.5, 6.5, 'Patient Attributes:', ha='center', fontsize=8, fontweight='bold')
    ax.text(1.5, 6.2, '• patient_id: String', ha='left', fontsize=7)
    ax.text(1.5, 6.0, '• age: Integer', ha='left', fontsize=7)
    ax.text(1.5, 5.8, '• gender: String', ha='left', fontsize=7)
    ax.text(1.5, 5.6, '• state: String', ha='left', fontsize=7)

    # Symptom attributes
    symptom_attr = FancyBboxPatch((3, 5.2), 2, 1.5,
                                  boxstyle="round,pad=0.05",
                                  edgecolor='green', facecolor='honeydew', linewidth=1)
    ax.add_patch(symptom_attr)
    ax.text(4, 6.5, 'Symptom Attributes:', ha='center', fontsize=8, fontweight='bold')
    ax.text(4, 6.25, '• fever: Boolean', ha='left', fontsize=7)
    ax.text(4, 6.05, '• temp: Float', ha='left', fontsize=7)
    ax.text(4, 5.85, '• cough: Boolean', ha='left', fontsize=7)
    ax.text(4, 5.65, '• cough_type: String', ha='left', fontsize=7)
    ax.text(4, 5.45, '• loss_of_taste_smell', ha='left', fontsize=7)
    ax.text(4, 5.25, '• oxygen_saturation', ha='left', fontsize=7)

    # MedicalHistory attributes
    med_attr = FancyBboxPatch((5.5, 5.5), 2.5, 1.2,
                              boxstyle="round,pad=0.05",
                              edgecolor='orange', facecolor='cornsilk', linewidth=1)
    ax.add_patch(med_attr)
    ax.text(6.75, 6.5, 'MedicalHistory Attrs:', ha='center', fontsize=8, fontweight='bold')
    ax.text(6.75, 6.2, '• diabetes: Boolean', ha='left', fontsize=7)
    ax.text(6.75, 6.0, '• hypertension: Boolean', ha='left', fontsize=7)
    ax.text(6.75, 5.8, '• heart_disease: Boolean', ha='left', fontsize=7)
    ax.text(6.75, 5.6, '• lung_disease: Boolean', ha='left', fontsize=7)

    # ExposureHistory attributes
    exp_attr = FancyBboxPatch((8.5, 5.5), 2.2, 1.2,
                              boxstyle="round,pad=0.05",
                              edgecolor='purple', facecolor='lavenderblush', linewidth=1)
    ax.add_patch(exp_attr)
    ax.text(9.6, 6.5, 'Exposure Attrs:', ha='center', fontsize=8, fontweight='bold')
    ax.text(9.6, 6.2, '• close_contact: Bool', ha='left', fontsize=7)
    ax.text(9.6, 6.0, '• contact_days_ago', ha='left', fontsize=7)
    ax.text(9.6, 5.8, '• travel_history: Bool', ha='left', fontsize=7)
    ax.text(9.6, 5.6, '• healthcare_worker', ha='left', fontsize=7)

    # Diagnosis attributes
    diag_attr = FancyBboxPatch((11.2, 5.5), 2, 1.2,
                               boxstyle="round,pad=0.05",
                               edgecolor='red', facecolor='mistyrose', linewidth=1)
    ax.add_patch(diag_attr)
    ax.text(12.2, 6.5, 'Diagnosis Attrs:', ha='center', fontsize=8, fontweight='bold')
    ax.text(12.2, 6.2, '• condition: String', ha='left', fontsize=7)
    ax.text(12.2, 6.0, '• confidence: Float', ha='left', fontsize=7)
    ax.text(12.2, 5.8, '• rule_id: String', ha='left', fontsize=7)
    ax.text(12.2, 5.6, '• timestamp', ha='left', fontsize=7)

    # Arrows to attributes
    ax.plot([1.5, 1.5], [7, 6.7], 'k--', lw=1, alpha=0.5)
    ax.plot([4, 4], [7, 6.7], 'k--', lw=1, alpha=0.5)
    ax.plot([6.75, 6.75], [7, 6.7], 'k--', lw=1, alpha=0.5)
    ax.plot([9.6, 9.6], [7, 6.7], 'k--', lw=1, alpha=0.5)
    ax.plot([12.2, 12.2], [7, 6.7], 'k--', lw=1, alpha=0.5)

    # Instance examples
    instance_box = FancyBboxPatch((0.5, 0.5), 13, 4.5,
                                  boxstyle="round,pad=0.1",
                                  edgecolor='navy', facecolor='aliceblue', linewidth=2)
    ax.add_patch(instance_box)

    ax.text(7, 4.7, 'Example Instances (RDF Triples)', ha='center', fontsize=11, fontweight='bold')

    # Patient instance
    ax.text(2, 4.2, 'patient:P001', ha='left', fontsize=9, fontweight='bold', color='blue')
    ax.text(2, 3.95, '  rdf:type        cidas:Patient', ha='left', fontsize=8, family='monospace')
    ax.text(2, 3.7, '  cidas:age       "45"', ha='left', fontsize=8, family='monospace')
    ax.text(2, 3.45, '  cidas:gender    "Male"', ha='left', fontsize=8, family='monospace')
    ax.text(2, 3.2, '  cidas:state     "Selangor"', ha='left', fontsize=8, family='monospace')

    # Symptom instance
    ax.text(7, 4.2, 'symptom:S001', ha='left', fontsize=9, fontweight='bold', color='green')
    ax.text(7, 3.95, '  rdf:type                cidas:Symptom', ha='left', fontsize=8, family='monospace')
    ax.text(7, 3.7, '  cidas:fever             "true"', ha='left', fontsize=8, family='monospace')
    ax.text(7, 3.45, '  cidas:temperature       "38.5"', ha='left', fontsize=8, family='monospace')
    ax.text(7, 3.2, '  cidas:loss_taste_smell  "true"', ha='left', fontsize=8, family='monospace')

    # Diagnosis instance
    ax.text(2, 2.7, 'diagnosis:D001', ha='left', fontsize=9, fontweight='bold', color='red')
    ax.text(2, 2.45, '  rdf:type          cidas:Diagnosis', ha='left', fontsize=8, family='monospace')
    ax.text(2, 2.2, '  cidas:condition   "COVID-19"', ha='left', fontsize=8, family='monospace')
    ax.text(2, 1.95, '  cidas:confidence  "0.95"', ha='left', fontsize=8, family='monospace')
    ax.text(2, 1.7, '  cidas:rule_id     "DD-01"', ha='left', fontsize=8, family='monospace')

    # Relationships
    ax.text(7, 2.7, 'Relationships (Object Properties):', ha='left', fontsize=9, fontweight='bold')
    ax.text(7, 2.45, '  patient:P001  cidas:hasSymptom     symptom:S001', ha='left', fontsize=8, family='monospace')
    ax.text(7, 2.2, '  patient:P001  cidas:hasDiagnosis   diagnosis:D001', ha='left', fontsize=8, family='monospace')
    ax.text(7, 1.95, '  symptom:S001  cidas:leadsToDiag    diagnosis:D001', ha='left', fontsize=8, family='monospace')
    ax.text(7, 1.7, '  diagnosis:D001 cidas:certaintyFactor "0.95"', ha='left', fontsize=8, family='monospace')

    # Namespace
    ax.text(7, 1.2, 'Namespaces: cidas = http://cidas.expert/ontology#', ha='center',
            fontsize=8, style='italic')
    ax.text(7, 0.9, '           rdf = http://www.w3.org/1999/02/22-rdf-syntax-ns#', ha='center',
            fontsize=8, style='italic')

    plt.tight_layout()
    plt.savefig('figures_academic/04_rdf_class_hierarchy.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: 04_rdf_class_hierarchy.png")


# ============================================================================
# FIGURE 5: CONFIDENCE PROPAGATION
# ============================================================================

def create_confidence_propagation():
    """Show how confidence/certainty propagates through the system"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Confidence/Certainty Factor Propagation in Expert System',
            ha='center', fontsize=14, fontweight='bold')

    # Stage 1: Input Evidence
    stage1_box = FancyBboxPatch((0.5, 7.5), 3, 1.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='blue', facecolor='lightblue', linewidth=2)
    ax.add_patch(stage1_box)
    ax.text(2, 8.7, 'Stage 1: Evidence Collection', ha='center', fontweight='bold', fontsize=10)
    ax.text(2, 8.4, 'Symptoms Observed:', ha='center', fontsize=9)
    ax.text(2, 8.1, '• Loss of taste (CF=1.0)', ha='center', fontsize=8)
    ax.text(2, 7.85, '• Dry cough (CF=1.0)', ha='center', fontsize=8)
    ax.text(2, 7.6, '• Fever 38.5°C (CF=0.8)', ha='center', fontsize=8)

    # Arrow 1
    arrow1 = FancyArrowPatch((3.5, 8.25), (5, 8.25), arrowstyle='->',
                             lw=3, color='black', mutation_scale=20)
    ax.add_patch(arrow1)
    ax.text(4.25, 8.5, 'Match', ha='center', fontsize=8, fontweight='bold')

    # Stage 2: Rule Activation
    stage2_box = FancyBboxPatch((5, 7.5), 3.5, 1.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='green', facecolor='lightgreen', linewidth=2)
    ax.add_patch(stage2_box)
    ax.text(6.75, 8.7, 'Stage 2: Rule Activation', ha='center', fontweight='bold', fontsize=10)
    ax.text(6.75, 8.4, 'Rule DD-01 fires:', ha='center', fontsize=9)
    ax.text(6.75, 8.1, 'IF loss_of_taste_smell', ha='center', fontsize=8, style='italic')
    ax.text(6.75, 7.85, 'THEN COVID-19', ha='center', fontsize=8, style='italic')
    ax.text(6.75, 7.6, 'Base CF = 0.88', ha='center', fontsize=9, fontweight='bold', color='darkgreen')

    # Arrow 2
    arrow2 = FancyArrowPatch((8.5, 8.25), (10, 8.25), arrowstyle='->',
                             lw=3, color='black', mutation_scale=20)
    ax.add_patch(arrow2)
    ax.text(9.25, 8.5, 'Combine', ha='center', fontsize=8, fontweight='bold')

    # Stage 3: CF Combination
    stage3_box = FancyBboxPatch((10, 7.5), 3.5, 1.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax.add_patch(stage3_box)
    ax.text(11.75, 8.7, 'Stage 3: CF Combination', ha='center', fontweight='bold', fontsize=10)
    ax.text(11.75, 8.35, 'CF₁ = 0.88 (anosmia)', ha='center', fontsize=8)
    ax.text(11.75, 8.1, 'CF₂ = 0.70 (dry cough)', ha='center', fontsize=8)
    ax.text(11.75, 7.85, 'Combined:', ha='center', fontsize=9)
    ax.text(11.75, 7.6, '0.88 + 0.70(1-0.88) = 0.964', ha='center', fontsize=8, family='monospace')

    # Arrow 3 (down)
    arrow3 = FancyArrowPatch((6.75, 7.5), (6.75, 6.8), arrowstyle='->',
                             lw=3, color='black', mutation_scale=20)
    ax.add_patch(arrow3)

    # Stage 4: Risk Assessment
    stage4_box = FancyBboxPatch((4, 5.5), 5.5, 1.2,
                                boxstyle="round,pad=0.1",
                                edgecolor='purple', facecolor='lavender', linewidth=2)
    ax.add_patch(stage4_box)
    ax.text(6.75, 6.4, 'Stage 4: Risk Assessment (Fuzzy Logic)', ha='center', fontweight='bold', fontsize=10)
    ax.text(6.75, 6.05, 'Inputs: Fever=38.5, Symptoms=3, Age=45, O2=96%', ha='center', fontsize=8)
    ax.text(6.75, 5.75, 'Fuzzy Risk Score: 62/100 → Medium Risk', ha='center', fontsize=9,
            fontweight='bold', color='purple')

    # Arrow 4 (down)
    arrow4 = FancyArrowPatch((6.75, 5.5), (6.75, 4.8), arrowstyle='->',
                             lw=3, color='black', mutation_scale=20)
    ax.add_patch(arrow4)

    # Stage 5: Care Pathway
    stage5_box = FancyBboxPatch((4, 3.5), 5.5, 1.2,
                                boxstyle="round,pad=0.1",
                                edgecolor='red', facecolor='lightcoral', linewidth=2)
    ax.add_patch(stage5_box)
    ax.text(6.75, 4.4, 'Stage 5: Care Pathway Recommendation', ha='center', fontweight='bold', fontsize=10)
    ax.text(6.75, 4.05, 'Medium Risk + Age 45 → HOME_CARE_MONITORED', ha='center', fontsize=9)
    ax.text(6.75, 3.75, 'Follow-up: 48 hours', ha='center', fontsize=8)

    # Final output box
    output_box = FancyBboxPatch((3.5, 0.5), 6.5, 2.8,
                                boxstyle="round,pad=0.1",
                                edgecolor='darkgreen', facecolor='lightgreen', linewidth=3)
    ax.add_patch(output_box)
    ax.text(6.75, 3, 'Final Output with Confidence Scores', ha='center',
            fontweight='bold', fontsize=11)
    ax.text(6.75, 2.6, 'Diagnosis: COVID-19', ha='center', fontsize=10, fontweight='bold')
    ax.text(6.75, 2.3, 'Diagnostic Confidence (CF): 96.4%', ha='center', fontsize=9, color='darkgreen')
    ax.text(6.75, 2.0, 'Risk Level: Medium (Score: 62/100)', ha='center', fontsize=9)
    ax.text(6.75, 1.7, 'Care Plan: HOME_CARE_MONITORED', ha='center', fontsize=9)
    ax.text(6.75, 1.4, 'Urgency: MODERATE', ha='center', fontsize=9)
    ax.text(6.75, 1.1, 'Explanation: Moderate risk with typical COVID symptoms', ha='center', fontsize=8,
            style='italic')
    ax.text(6.75, 0.8, 'requires home monitoring with 48-hour follow-up', ha='center', fontsize=8, style='italic')

    # Confidence flow sidebar
    flow_box = FancyBboxPatch((0.5, 0.5), 2.5, 6.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='navy', facecolor='aliceblue', linewidth=2)
    ax.add_patch(flow_box)

    ax.text(1.75, 6.7, 'CF Flow', ha='center', fontweight='bold', fontsize=11)
    ax.text(1.75, 6.4, 'Through System', ha='center', fontweight='bold', fontsize=11)

    # Flow stages
    ax.text(1.75, 5.9, '1. Evidence', ha='center', fontsize=9, fontweight='bold')
    ax.text(1.75, 5.65, 'CF = 1.0', ha='center', fontsize=8)
    ax.text(1.75, 5.45, '(Observable)', ha='center', fontsize=7, style='italic')

    ax.arrow(1.75, 5.3, 0, -0.3, head_width=0.15, head_length=0.1, fc='black', ec='black')

    ax.text(1.75, 4.8, '2. Rule CF', ha='center', fontsize=9, fontweight='bold')
    ax.text(1.75, 4.55, 'CF = 0.88', ha='center', fontsize=8)
    ax.text(1.75, 4.35, '(Rule strength)', ha='center', fontsize=7, style='italic')

    ax.arrow(1.75, 4.2, 0, -0.3, head_width=0.15, head_length=0.1, fc='black', ec='black')

    ax.text(1.75, 3.7, '3. Combined', ha='center', fontsize=9, fontweight='bold')
    ax.text(1.75, 3.45, 'CF = 0.964', ha='center', fontsize=8)
    ax.text(1.75, 3.25, '(Multi-evidence)', ha='center', fontsize=7, style='italic')

    ax.arrow(1.75, 3.1, 0, -0.3, head_width=0.15, head_length=0.1, fc='black', ec='black')

    ax.text(1.75, 2.6, '4. Risk Fuzzy', ha='center', fontsize=9, fontweight='bold')
    ax.text(1.75, 2.35, 'Score = 62', ha='center', fontsize=8)
    ax.text(1.75, 2.15, '(Defuzzified)', ha='center', fontsize=7, style='italic')

    ax.arrow(1.75, 2.0, 0, -0.3, head_width=0.15, head_length=0.1, fc='black', ec='black')

    ax.text(1.75, 1.5, '5. Decision', ha='center', fontsize=9, fontweight='bold')
    ax.text(1.75, 1.25, 'Action: Care', ha='center', fontsize=8)
    ax.text(1.75, 1.05, '(Rule-based)', ha='center', fontsize=7, style='italic')
    ax.text(1.75, 0.75, 'Output', ha='center', fontsize=9, fontweight='bold', color='darkgreen')

    # Legend box on right
    legend_box = FancyBboxPatch((10.5, 0.5), 3, 6.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='gray', facecolor='whitesmoke', linewidth=2)
    ax.add_patch(legend_box)

    ax.text(12, 6.7, 'CF Propagation', ha='center', fontweight='bold', fontsize=11)
    ax.text(12, 6.4, 'Rules', ha='center', fontweight='bold', fontsize=11)

    ax.text(12, 5.9, 'Rule 1: Single Evidence', ha='center', fontsize=9, fontweight='bold')
    ax.text(12, 5.65, 'CF(H,E) = CF_rule', ha='center', fontsize=8, family='monospace')
    ax.text(12, 5.45, 'Example: 0.88', ha='center', fontsize=7, style='italic')

    ax.text(12, 5.05, 'Rule 2: Multiple Evidence', ha='center', fontsize=9, fontweight='bold')
    ax.text(12, 4.8, 'CF = CF₁ + CF₂(1-CF₁)', ha='center', fontsize=8, family='monospace')
    ax.text(12, 4.6, 'Increases confidence', ha='center', fontsize=7, style='italic')

    ax.text(12, 4.2, 'Rule 3: Contradictory', ha='center', fontsize=9, fontweight='bold')
    ax.text(12, 3.95, 'CF_new = CF₁ + CF₂', ha='center', fontsize=8, family='monospace')
    ax.text(12, 3.75, 'if both negative', ha='center', fontsize=7, style='italic')

    ax.text(12, 3.35, 'Thresholds:', ha='center', fontsize=9, fontweight='bold')
    ax.text(12, 3.1, 'High: CF > 0.85', ha='center', fontsize=8)
    ax.text(12, 2.9, 'Medium: 0.70-0.85', ha='center', fontsize=8)
    ax.text(12, 2.7, 'Low: CF < 0.70', ha='center', fontsize=8)

    ax.text(12, 2.3, 'Uncertainty Handling:', ha='center', fontsize=9, fontweight='bold')
    ax.text(12, 2.05, 'CF < 0.65:', ha='center', fontsize=8)
    ax.text(12, 1.85, 'Request more info', ha='center', fontsize=7, style='italic')
    ax.text(12, 1.65, 'CF 0.65-0.70:', ha='center', fontsize=8)
    ax.text(12, 1.45, 'Possible diagnosis', ha='center', fontsize=7, style='italic')
    ax.text(12, 1.25, 'CF > 0.85:', ha='center', fontsize=8)
    ax.text(12, 1.05, 'Confident diagnosis', ha='center', fontsize=7, style='italic')

    plt.tight_layout()
    plt.savefig('figures_academic/05_confidence_propagation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: 05_confidence_propagation.png")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Generating Academic Figures for CIDAS Expert System")
    print("=" * 70)
    print()

    print("Creating figures...")
    create_certainty_factor_diagram()
    create_decision_tree()
    create_fuzzy_membership_functions()
    create_rdf_class_diagram()
    create_confidence_propagation()

    print()
    print("=" * 70)
    print("SUCCESS! All 5 academic figures generated")
    print("=" * 70)
    print()
    print("Generated files in 'figures_academic/' directory:")
    print("  1. 01_certainty_factor_calculation.png - CF formula & examples")
    print("  2. 02_decision_tree_diagnosis.png - Decision flow with CFs")
    print("  3. 03_fuzzy_membership_functions.png - Fuzzy logic variables")
    print("  4. 04_rdf_class_hierarchy.png - Knowledge representation")
    print("  5. 05_confidence_propagation.png - CF flow through system")
    print()
    print("All figures are high-resolution (300 DPI) suitable for academic reports.")
    print("=" * 70)