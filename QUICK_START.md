# 🚀 CIDAS Quick Start Guide

**Get up and running in 5 minutes!**

---

## ⚡ Super Quick Start (Copy-Paste)

```bash
# Copy and paste these commands one by one:

git clone https://github.com/FarisMD22/Expert_System_Covid19_Assistance.git
cd Expert_System_Covid19_Assistance
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

**Done!** Your browser will open automatically at http://localhost:8501

---

## 📝 Step-by-Step Instructions

### 1️⃣ **Clone the Repository**

**Windows / Mac / Linux:**
```bash
git clone https://github.com/FarisMD22/Expert_System_Covid19_Assistance.git
```

**Don't have Git?** [Download as ZIP](https://github.com/FarisMD22/Expert_System_Covid19_Assistance/archive/refs/heads/main.zip) and extract.

---

### 2️⃣ **Navigate to Project**

```bash
cd Expert_System_Covid19_Assistance
```

---

### 3️⃣ **Create Virtual Environment**

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**✅ Success:** You should see `(.venv)` at the start of your command line.

---

### 4️⃣ **Install Requirements**

```bash
pip install -r requirements.txt
```

**⏱️ This takes 1-2 minutes.** You'll see packages being installed.

**✅ Success:** Should end with "Successfully installed..."

---

### 5️⃣ **Verify Installation**

```bash
python config.py
```

**Expected output:**
```
✓ ALL TESTS PASSED - config.py is working correctly!
```

---

### 6️⃣ **Run the Application**

```bash
streamlit run app.py
```

**✅ Success:** Browser opens automatically to http://localhost:8501

**If browser doesn't open:** Manually go to http://localhost:8501

---

## 🎯 First Time Using CIDAS

### Try Your First Diagnosis

1. **Click "Diagnosis"** in the left sidebar
2. **Fill in patient info:**
   - Patient ID: `TEST001`
   - Age: `45`
   - Gender: `Male`

3. **Select symptoms:**
   - ✅ Fever (Temperature: 38.5°C)
   - ✅ Cough (Type: Dry)
   - ✅ Fatigue (Severity: Moderate)
   - ✅ Loss of taste/smell
   - Oxygen: `96%`

4. **Click "Analyze Patient"**

5. **See Results:**
   - Diagnosis: COVID-19 (95% confidence)
   - Risk: Medium
   - Recommendation: Monitored Home Care

**Congratulations!** 🎉 You've completed your first diagnosis!

---

## 📊 Generate Your First Chart

1. **Go to "History"** page (left sidebar)
2. **Scroll down** to "Generate Figures & Analytics"
3. **Click "📈 Generate All Figures"**
4. **Wait 2-3 seconds**
5. **See your chart!**
6. **Click "💾 Download Report (PNG)"**
7. **Check your Downloads folder** ✅

---

## 🧪 Run Tests

Verify everything works:

```bash
python evaluation.py
```

**Expected results:**
```
Test Cases: 10/10 ✓
Diagnosis Accuracy: 100%
Overall Accuracy: 80%
✓ Evaluation complete!
```

---

## ⚠️ Common Issues

### Issue: "streamlit: command not found"

**Fix:**
```bash
# Make sure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Then try again
streamlit run app.py
```

### Issue: "ModuleNotFoundError"

**Fix:**
```bash
pip install -r requirements.txt
```

### Issue: Port already in use

**Fix:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: Visualization buttons don't work

**Fix:**
1. Complete at least one diagnosis first
2. Make sure `visualizations.py` exists in project folder
3. Refresh the page (F5)

---

## 📚 What's Next?

### Learn More

- **Full Documentation:** See [README.md](README.md)
- **User Guide:** Click "About" in the app
- **Technical Details:** Check code comments in `engine.py`

### Try Different Scenarios

**COVID-19 (High Risk):**
- Age: 75, Multiple comorbidities, Low O2

**Influenza:**
- Body ache, Sudden onset, No loss of taste

**Common Cold:**
- Runny nose, Sneezing, No fever

**Allergies:**
- Itchy eyes, Seasonal, No fever

### Advanced Features

**Generate Analytics:**
- History page → Generate figures → Download charts

**Run Jupyter Notebook:**
```bash
jupyter notebook CIDAS_Analysis.ipynb
```

**Explore Code:**
- `engine.py` - 67 expert rules
- `config.py` - Knowledge base
- `app.py` - Web interface

---

## 💡 Pro Tips

### For Demos

1. **Prepare 3-5 diverse test cases** before demo
2. **Show History page** with visualizations
3. **Download figures** to present
4. **Explain XAI** reasoning for academic credit

### For Development

1. **Always use virtual environment** (.venv)
2. **Test after changes:** `python evaluation.py`
3. **Keep browser console open** (F12) for debugging
4. **Commit frequently** if modifying code

### For Reports

1. **Run Jupyter notebook** for publication-quality figures
2. **Use 300 DPI exports** for academic papers
3. **Include confusion matrix** to show 100% diagnosis accuracy
4. **Compare with literature** (Shatnawi, Ahmed, Ozbey)

---

## 🎓 For Team Members

### Getting Latest Changes

```bash
git pull origin main
pip install -r requirements.txt  # In case dependencies changed
streamlit run app.py
```

### Testing Your Changes

```bash
# Always test before committing
python config.py      # Verify config
python engine.py      # Verify rules
python evaluation.py  # Run full tests
streamlit run app.py  # Test UI
```

### Sharing Figures

All generated figures are in:
- **Streamlit:** Downloads folder (after clicking download)
- **Jupyter:** Project root folder (*.png files)

---

## 🆘 Need Help?

### Quick Checks

- [ ] Python 3.9+ installed? `python --version`
- [ ] Virtual environment activated? See `(.venv)` in terminal?
- [ ] Requirements installed? `pip list | grep streamlit`
- [ ] In correct directory? `dir app.py` (Windows) / `ls app.py` (Mac/Linux)

### Resources

1. **README.md** - Complete documentation
2. **GitHub Issues** - Report bugs
3. **Team Members** - Ask for help
4. **In-App Help** - Click "About" page

---

## ✅ Success Checklist

After setup, you should be able to:

- [ ] Open app at http://localhost:8501
- [ ] Complete a diagnosis
- [ ] See results with confidence scores
- [ ] View history of assessments
- [ ] Generate and download figures
- [ ] Run tests (80% accuracy)
- [ ] No errors in terminal

**All checked?** You're ready! 🎉

---

## 📞 Contact

- **Repository:** https://github.com/FarisMD22/Expert_System_Covid19_Assistance
- **Issues:** [Create an issue](https://github.com/FarisMD22/Expert_System_Covid19_Assistance/issues)

---

**Last Updated:** January 2026  
**Version:** 1.0.0  
**Status:** Production Ready ✅

---

<div align="center">

**[📖 Full Documentation](README.md)** • **[🐛 Report Issue](https://github.com/FarisMD22/Expert_System_Covid19_Assistance/issues)** • **[⬆ Back to Top](#-cidas-quick-start-guide)**

</div>
