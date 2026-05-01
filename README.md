# campus-pulse-dashboard
# Campus Pulse Dashboard

Campus Pulse is a student satisfaction dashboard that analyzes and visualizes feedback data related to campus facilities such as Library, Cafeteria, and Sports.

---

## Features

- Interactive dashboard for data visualization  
- Facility-wise filtering (Library, Cafeteria, Sports)  
- Display of key metrics (Average, Best, Worst facility)  
- FastAPI backend integration  
- Data preprocessing using Pandas  
- Basic login system for secure access  

---

## Tech Stack

- Backend: FastAPI, Python  
- Frontend: HTML, CSS, JavaScript  
- Visualization: Chart.js  
- Data Analysis: Pandas, Matplotlib, Seaborn  

---

## Project Structure
campus-pulse/
│
├── backend/ # FastAPI backend
├── frontend/ # Dashboard UI and login page
├── analysis/ # Data analysis (Jupyter Notebook)
├── data/ # Dataset
├── requirements.txt

---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/SHAILESH197/campus-pulse-dashboard.git

cd campus-pulse-dashboard

---

### 3. Install dependencies
python -m venv venv
venv\Scripts\activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Run backend server
uvicorn backend.main:app --reload

---

### 5. Run frontend

Open the file `frontend/login.html` in your browser.

---

## Login Credentials
Username: admin
Password: Shailesh@2005

---

## Output

- Dashboard with charts and metrics  
- Facility-wise satisfaction analysis  
- Interactive filtering system  

---

## Future Enhancements

- Real-time data integration  
- Advanced authentication (JWT)  
- Machine learning-based prediction  
- Cloud deployment  

---

## Author

Shailesh Dwivedi

---

## Project Status

Completed  
Ready for deployment
