#!/usr/bin/env python3
"""
Quick Integration Script for CIDAS Visualizations
Automatically adds visualization buttons to app.py
"""

import os
import sys

def integrate_visualizations():
    """Integrate visualization code into app.py"""
    
    print("=" * 70)
    print("CIDAS VISUALIZATION INTEGRATION")
    print("=" * 70)
    print()
    
    # Check if visualizations.py exists
    if not os.path.exists('visualizations.py'):
        print("❌ Error: visualizations.py not found!")
        print("   Please make sure visualizations.py is in the current directory")
        return False
    
    print("✅ Found visualizations.py")
    
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found!")
        print("   Please run this script from your cidas_complete directory")
        return False
    
    print("✅ Found app.py")
    
    # Read app.py
    with open('app.py', 'r', encoding='utf-8') as f:
        app_content = f.read()
    
    # Check if already integrated
    if 'import visualizations as viz' in app_content:
        print("⚠️  Visualizations already integrated in app.py")
        print("   No changes needed!")
        return True
    
    # Add imports
    print()
    print("📝 Adding imports...")
    
    import_section = """# Visualization imports
import visualizations as viz
import io
"""
    
    # Find where to insert (after other imports)
    import_index = app_content.find('import streamlit as st')
    if import_index != -1:
        # Find end of import block
        next_blank = app_content.find('\n\n', import_index)
        if next_blank != -1:
            app_content = app_content[:next_blank] + '\n' + import_section + app_content[next_blank:]
    
    print("✅ Imports added")
    
    # Add visualization section to page_history
    print("📝 Adding visualization section to History page...")
    
    viz_code = '''
    # ========================================================================
    # VISUALIZATION SECTION - Auto-generated
    # ========================================================================
    st.markdown("---")
    st.subheader("📊 Generate Figures & Analytics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📈 Generate All Figures", type="primary"):
            if not st.session_state.history:
                st.warning("No history data. Complete at least one diagnosis first.")
            else:
                with st.spinner("Generating visualizations..."):
                    fig = viz.generate_comprehensive_report(st.session_state.history)
                    
                    if fig:
                        st.pyplot(fig)
                        
                        buf = io.BytesIO()
                        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                        buf.seek(0)
                        
                        st.download_button(
                            label="💾 Download Report (PNG)",
                            data=buf,
                            file_name=f"CIDAS_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                            mime="image/png"
                        )
                        st.success("✅ Report generated successfully!")
    
    with col2:
        if st.button("🥧 Diagnosis Distribution"):
            if st.session_state.history:
                with st.spinner("Generating chart..."):
                    fig = viz.generate_diagnosis_pie_chart(st.session_state.history)
                    if fig:
                        st.pyplot(fig)
                        
                        buf = io.BytesIO()
                        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                        buf.seek(0)
                        
                        st.download_button(
                            label="💾 Download Chart",
                            data=buf,
                            file_name=f"diagnosis_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                            mime="image/png"
                        )
    
    with col3:
        if st.button("📊 Risk Analysis"):
            if st.session_state.history:
                with st.spinner("Generating chart..."):
                    fig = viz.generate_risk_distribution_chart(st.session_state.history)
                    if fig:
                        st.pyplot(fig)
                        
                        buf = io.BytesIO()
                        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                        buf.seek(0)
                        
                        st.download_button(
                            label="💾 Download Chart",
                            data=buf,
                            file_name=f"risk_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                            mime="image/png"
                        )
    # ========================================================================
'''
    
    # Find end of page_history function
    history_func = 'def page_history():'
    if history_func in app_content:
        # Find the end of the function (before next function or end of file)
        start_pos = app_content.find(history_func)
        
        # Look for next function definition
        next_func = app_content.find('\ndef ', start_pos + len(history_func))
        
        if next_func == -1:
            # Insert at end
            app_content = app_content.rstrip() + '\n' + viz_code + '\n'
        else:
            # Insert before next function
            app_content = app_content[:next_func] + viz_code + '\n' + app_content[next_func:]
        
        print("✅ Visualization section added to History page")
    else:
        print("⚠️  Warning: Could not find page_history() function")
        print("   You'll need to add the visualization code manually")
    
    # Backup original
    print()
    print("💾 Creating backup...")
    with open('app.py.backup', 'w', encoding='utf-8') as f:
        with open('app.py', 'r', encoding='utf-8') as orig:
            f.write(orig.read())
    print("✅ Backup saved as app.py.backup")
    
    # Write updated app.py
    print("💾 Saving updated app.py...")
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(app_content)
    print("✅ app.py updated successfully!")
    
    print()
    print("=" * 70)
    print("✅ INTEGRATION COMPLETE!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Run: streamlit run app.py")
    print("2. Go to History page")
    print("3. After doing some diagnoses, scroll down")
    print("4. Click buttons to generate figures!")
    print()
    print("Note: If something goes wrong, restore from app.py.backup")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    except:
        pass
    
    success = integrate_visualizations()
    
    if not success:
        print()
        print("❌ Integration failed!")
        print("   Please check the error messages above and try again")
        sys.exit(1)
    
    sys.exit(0)
