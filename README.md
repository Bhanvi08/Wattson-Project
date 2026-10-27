# Wattson | AI Energy Analytics & Fault Diagnostics ⚡🤖
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Backend](https://img.shields.io/badge/Backend-Flask-lightgrey.svg?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange.svg?style=flat-square&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web)

## 📝 Project Overview
**Wattson** is an intelligent energy management platform designed to bridge the gap between electrical hardware data and software analytics. 

Most energy consumers lack the tools to understand their consumption patterns or identify household electrical risks. I built Wattson to act as a virtual technical assistant that handles data tracking and safety diagnostics. The system uses a Python backend to process meter data and provides a real-time dashboard for power consumption and cost estimation, alongside an AI-driven fault diagnostic engine that provides human-like explanations for complex electrical issues.

---

## 🛠️ System Architecture & Core Tech Stack
*   **Backend:** Python and Flask framework.
*   **Frontend:** HTML, CSS, and JavaScript.
*   **Analytics:** Chart.js library for dynamic data visualization.
*   **Environment:** Isolated Python environment utilizing UV.

**System Modules:**
*   **Energy Analytics:** Real-time tracking of kWh units with integrated tariff slab logic for billing.
*   **AI Diagnostics:** A rule-based analytical engine that processes reported symptoms like MCB trips or high bills.
*   **Technical Assistant:** An NLP assistant using keyword mapping for electrical safety and troubleshooting.
*   **User Data Management:** Personalized profile system with persistent data across the application session.

---

## ⚙️ Engineering Logic Employed
The system is built on core **Electrical Engineering** principles to ensure technical accuracy:
*   **Efficiency Modeling:** Analysis based on BEE Star Ratings and thermal equilibrium.
*   **Fault Diagnostics:** Troubleshooting flows for Short Circuits, Earth Leakage, and Weak Neutral faults.
*   **Consumption Math:** Implementation of the standard energy formula `(Power in Watts × Time in Hours) / 1000`.
*   **Power Quality:** Actionable advice on power factor optimization and load shifting for peak hours.

---

## 🚀 Future Roadmap
*   **Hardware Integration:** Connecting the Flask engine to ESP32 and IoT current sensors for live data streaming.
*   **LLM Integration:** Upgrading from heuristic logic to a full LLM API for complex technical queries.
*   **Mobile Deployment:** Developing a cross-platform mobile instance for real-time energy alerts.

Author: Bhanvi Singh Chauhan
