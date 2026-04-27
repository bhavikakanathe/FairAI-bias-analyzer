# FairAI: Unbiased AI Bias Analyzer ⚖️🤖

**FairAI** is an AI governance platform designed to ensure fairness, transparency, and accountability in machine learning models. It identifies demographic biases in datasets, provides AI-driven explanations using Google Gemini, and simulates mitigation strategies to help developers build more equitable AI systems.

---

## 🌟 Key Features

- **📊 Automated Bias Auditing:** Instantly calculates selection rates and **Disparate Impact Scores** to identify unfair outcomes across demographic groups.
- **🧠 AI-Powered Insights:** Integrates with **Google Gemini 2.0 Flash** to provide plain-English explanations of complex statistical bias.
- **⚡ Real-time Mitigation Simulation:** Adjust model parameters in real-time to see how fairness can be improved without sacrificing accuracy.
- **🎨 Ethos Modern Design:** A premium, dark-mode-ready user interface built for modern developers and auditors.
- **📜 Exportable Reports:** Generate and download PDF reports of your fairness audits for stakeholders.

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla), Marked.js
- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **AI Integration:** Google Gemini API (`google-genai` SDK)
- **Deployment:** Vercel (Frontend), Render (Backend)

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/bhavikakanathe/FairAI-bias-analyzer.git
cd FairAI-bias-analyzer
```

### 2. Setup the Backend
1. Navigate to the Backend folder:
   ```bash
   cd Backend
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Gemini API Key:
   ```env
   GEMINI_API_KEY=your_actual_key_here
   ```
4. Start the server:
   ```bash
   uvicorn api:app --reload
   ```

### 3. Launch the Frontend
Simply open `frontend new/stitch_fairai_bias_analyzer/0_dashboard_overview/code.html` in your web browser.

---

## 📂 Project Structure

- `Backend/`: FastAPI server, bias calculation logic, and Gemini integration.
- `frontend new/`: The premium "Ethos Modern" UI prototype.
- `sample_dataset.csv`: A sample dataset to test bias detection (Loan Approvals).

---

## 🏆 Google Solution Challenge 2026
This project was developed for the **Google Solution Challenge** to address the need for ethical AI and reduced inequality in automated decision-making systems.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
