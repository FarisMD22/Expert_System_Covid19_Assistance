"""
Visualization Generator for CIDAS
Generates figures and charts from diagnosis/assessment results
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from datetime import datetime
import io
import base64

def generate_diagnosis_pie_chart(history_data):
    """Generate pie chart of diagnoses from history"""
    if not history_data:
        return None
    
    # Count diagnoses
    diagnosis_counts = {}
    for entry in history_data:
        diag = entry.get('diagnosis', 'Unknown')
        diagnosis_counts[diag] = diagnosis_counts.get(diag, 0) + 1
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    wedges, texts, autotexts = ax.pie(
        diagnosis_counts.values(),
        labels=diagnosis_counts.keys(),
        autopct='%1.1f%%',
        colors=colors,
        startangle=90
    )
    
    # Style
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)
    
    ax.set_title('Diagnosis Distribution', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    
    return fig

def generate_risk_distribution_chart(history_data):
    """Generate bar chart of risk levels"""
    if not history_data:
        return None
    
    # Count risk levels
    risk_counts = {'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0}
    for entry in history_data:
        risk = entry.get('risk_level', 'Unknown')
        if risk in risk_counts:
            risk_counts[risk] += 1
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'Low': '#4ECDC4', 'Medium': '#FFA07A', 'High': '#FF6B6B', 'Critical': '#D32F2F'}
    bars = ax.bar(risk_counts.keys(), risk_counts.values(), 
                   color=[colors[k] for k in risk_counts.keys()],
                   edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    ax.set_xlabel('Risk Level', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Cases', fontsize=14, fontweight='bold')
    ax.set_title('Risk Assessment Distribution', fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig

def generate_confidence_chart(history_data):
    """Generate histogram of confidence scores"""
    if not history_data:
        return None
    
    confidences = [entry.get('confidence', 0) * 100 for entry in history_data]
    
    if not confidences:
        return None
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    n, bins, patches = ax.hist(confidences, bins=10, color='#4ECDC4', 
                                edgecolor='black', alpha=0.7)
    
    # Color bars by confidence level
    for i, patch in enumerate(patches):
        if bins[i] < 70:
            patch.set_facecolor('#FFA07A')
        elif bins[i] < 85:
            patch.set_facecolor('#FFD93D')
        else:
            patch.set_facecolor('#4ECDC4')
    
    ax.set_xlabel('Confidence Score (%)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=14, fontweight='bold')
    ax.set_title('Diagnostic Confidence Distribution', fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add average line
    avg_conf = np.mean(confidences)
    ax.axvline(avg_conf, color='red', linestyle='--', linewidth=2, 
               label=f'Average: {avg_conf:.1f}%')
    ax.legend(fontsize=12)
    
    plt.tight_layout()
    return fig

def generate_symptom_heatmap(history_data):
    """Generate heatmap of common symptoms"""
    if not history_data:
        return None
    
    # Common symptoms to track
    symptoms = ['Fever', 'Cough', 'Fatigue', 'Shortness of Breath', 
                'Body Ache', 'Headache', 'Loss of Taste/Smell', 'Sore Throat']
    
    # Count symptom occurrences
    symptom_counts = {s: 0 for s in symptoms}
    for entry in history_data:
        symptoms_data = entry.get('symptoms', {})
        if symptoms_data.get('fever'): symptom_counts['Fever'] += 1
        if symptoms_data.get('cough'): symptom_counts['Cough'] += 1
        if symptoms_data.get('fatigue'): symptom_counts['Fatigue'] += 1
        if symptoms_data.get('shortness_of_breath'): symptom_counts['Shortness of Breath'] += 1
        if symptoms_data.get('body_ache'): symptom_counts['Body Ache'] += 1
        if symptoms_data.get('headache'): symptom_counts['Headache'] += 1
        if symptoms_data.get('loss_of_taste_smell'): symptom_counts['Loss of Taste/Smell'] += 1
        if symptoms_data.get('sore_throat'): symptom_counts['Sore Throat'] += 1
    
    # Sort by frequency
    sorted_symptoms = sorted(symptom_counts.items(), key=lambda x: x[1], reverse=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    symptoms_list = [s[0] for s in sorted_symptoms]
    counts = [s[1] for s in sorted_symptoms]
    
    bars = ax.barh(symptoms_list, counts, color='#4ECDC4', edgecolor='black', linewidth=1.5)
    
    # Color gradient
    max_count = max(counts) if counts else 1
    for i, (bar, count) in enumerate(zip(bars, counts)):
        intensity = count / max_count
        bar.set_color(plt.cm.RdYlGn_r(intensity))
        # Add value labels
        ax.text(count + 0.1, i, str(count), va='center', fontweight='bold', fontsize=11)
    
    ax.set_xlabel('Frequency', fontsize=14, fontweight='bold')
    ax.set_title('Most Common Symptoms', fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig

def generate_timeline_chart(history_data):
    """Generate timeline of diagnoses"""
    if not history_data:
        return None
    
    # Extract dates and diagnoses
    dates = []
    diagnoses = []
    for entry in history_data:
        timestamp = entry.get('timestamp', '')
        if timestamp:
            dates.append(timestamp)
            diagnoses.append(entry.get('diagnosis', 'Unknown'))
    
    if not dates:
        return None
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Map diagnoses to colors
    color_map = {
        'COVID-19': '#FF6B6B',
        'Influenza': '#4ECDC4', 
        'Common Cold': '#45B7D1',
        'Allergies': '#98D8C8',
        'Unknown': '#gray'
    }
    
    colors = [color_map.get(d, '#gray') for d in diagnoses]
    
    # Plot
    ax.scatter(range(len(dates)), [1]*len(dates), c=colors, s=200, alpha=0.6, edgecolors='black')
    
    # Add labels
    for i, (date, diag) in enumerate(zip(dates, diagnoses)):
        ax.text(i, 1.1, diag, rotation=45, ha='right', fontsize=9)
        ax.text(i, 0.9, date.split()[0], rotation=45, ha='right', fontsize=8, style='italic')
    
    ax.set_ylim(0.5, 1.5)
    ax.set_xlim(-0.5, len(dates)-0.5)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title('Diagnosis Timeline', fontsize=16, fontweight='bold', pad=20)
    
    # Legend
    legend_elements = [mpatches.Patch(color=color, label=diag) 
                      for diag, color in color_map.items() if diag in diagnoses]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10)
    
    plt.tight_layout()
    return fig

def generate_comprehensive_report(history_data):
    """Generate comprehensive multi-panel report"""
    if not history_data:
        return None
    
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # Panel 1: Diagnosis pie chart
    ax1 = fig.add_subplot(gs[0, 0])
    diagnosis_counts = {}
    for entry in history_data:
        diag = entry.get('diagnosis', 'Unknown')
        diagnosis_counts[diag] = diagnosis_counts.get(diag, 0) + 1
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    ax1.pie(diagnosis_counts.values(), labels=diagnosis_counts.keys(),
            autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.set_title('Diagnosis Distribution', fontweight='bold', fontsize=12)
    
    # Panel 2: Risk distribution
    ax2 = fig.add_subplot(gs[0, 1])
    risk_counts = {'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0}
    for entry in history_data:
        risk = entry.get('risk_level', 'Unknown')
        if risk in risk_counts:
            risk_counts[risk] += 1
    
    risk_colors = {'Low': '#4ECDC4', 'Medium': '#FFA07A', 'High': '#FF6B6B', 'Critical': '#D32F2F'}
    ax2.bar(risk_counts.keys(), risk_counts.values(),
            color=[risk_colors[k] for k in risk_counts.keys()])
    ax2.set_title('Risk Distribution', fontweight='bold', fontsize=12)
    ax2.set_ylabel('Count')
    
    # Panel 3: Confidence histogram
    ax3 = fig.add_subplot(gs[1, :])
    confidences = [entry.get('confidence', 0) * 100 for entry in history_data]
    ax3.hist(confidences, bins=10, color='#4ECDC4', edgecolor='black', alpha=0.7)
    ax3.set_title('Confidence Score Distribution', fontweight='bold', fontsize=12)
    ax3.set_xlabel('Confidence (%)')
    ax3.set_ylabel('Frequency')
    
    # Panel 4: Statistics summary
    ax4 = fig.add_subplot(gs[2, :])
    ax4.axis('off')
    
    total_cases = len(history_data)
    avg_conf = np.mean(confidences) if confidences else 0
    high_conf = sum(1 for c in confidences if c >= 85)
    
    stats_text = f"""
    CIDAS System Statistics
    ═══════════════════════════════════════
    
    Total Cases Analyzed: {total_cases}
    Average Confidence: {avg_conf:.1f}%
    High Confidence Cases (≥85%): {high_conf}
    
    Most Common Diagnosis: {max(diagnosis_counts, key=diagnosis_counts.get)}
    Most Common Risk Level: {max(risk_counts, key=risk_counts.get)}
    
    Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    ax4.text(0.5, 0.5, stats_text, ha='center', va='center',
             fontsize=11, family='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    fig.suptitle('CIDAS - Comprehensive Analysis Report', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    return fig

def fig_to_base64(fig):
    """Convert matplotlib figure to base64 string for download"""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    plt.close(fig)
    return img_base64

def save_figure(fig, filename):
    """Save figure to file"""
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return filename
