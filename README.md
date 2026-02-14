
**Household Energy Forecast**

This project loads daily household energy usage, engineers lag and rolling features, trains a multiple linear regression model, and produces a 7-day forecast CSV.

**Files**
- **Project script:** [main.py](main.py)
- **Input data:** [energy_usage.csv](energy_usage.csv)
- **Forecast output:** [Output.csv](Output.csv)

**Requirements**
- Python 3.8+
- Packages: `pandas`, `numpy`, `scikit-learn`

**Quick setup (Windows PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install pandas numpy scikit-learn
```

**Run**
```powershell
python main.py
```
After running, the forecast for the next 7 days will be saved to `Output.csv`.

**Input CSV format (sample)**
The script expects a CSV with two columns: `Date` and `Energy_Usage` (daily totals). Date format: `YYYY-MM-DD`.

Example `energy_usage.csv`:

```
Date,Energy_Usage
2026-01-01,23.5
2026-01-02,22.1
2026-01-03,24.0
2026-01-04,21.8
2026-01-05,20.7
```

**Notes & suggestions**
- The script creates lag features and rolling averages and splits data with an 80/20 train/test split; MAE is printed to console.
- For experimentation, open a Jupyter Notebook and replicate the `main.py` steps to inspect residuals, feature importance, and to try other models.
- If you want a `requirements.txt`, run:
```powershell
pip freeze > requirements.txt
```

**Contact / Next steps**
- If you'd like, I can: add a sample `energy_usage.csv`, create a `requirements.txt`, or provide a Jupyter notebook demonstrating the modeling steps and metrics.
