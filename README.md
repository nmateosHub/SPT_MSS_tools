# SPT MSS Tools

A small Python toolkit to compute the **Moment Scaling Spectrum (MSS)** and its slope (**sMSS**) from **single-particle tracking (SPT)** trajectories.

The implementation follows the MSS framework used to characterize diffusion behavior by analyzing the scaling of trajectory displacement moments. The tool is designed to work directly with **TrackMate export tables** (CSV files containing track coordinates).

---

## Features

* Compute **moment scaling spectrum (MSS)**
* Compute **sMSS (slope of the MSS)**
* Works directly with **TrackMate CSV outputs**
* Optional trajectory and MSS visualization
* Automatic correction for **negative sMSS values** caused by abnormal trajectory segments

If a negative sMSS is detected, the algorithm **removes the last frame of the trajectory and recomputes the MSS once**.

---

## Project Structure

```
SPT_MSS_tools_project/
│
├── main.py
├── data/
│   └── spots_in_tracks_statistics.csv
│
└── SPT_MSS_tools/
    └── mss/
        ├── core.py        # MSS mathematical implementation
        ├── analysis.py    # Track analysis functions
        └── plotting.py    # Visualization functions
```

---

## Requirements

* Python ≥ 3.8
* numpy
* pandas
* matplotlib

(the code has been written in Python 3.12.7)

Install dependencies with:

```bash
pip install numpy pandas matplotlib
```

---

## Input Data

The tool expects a **TrackMate "Spots in tracks statistics" CSV export** containing at least the following columns:

```
TRACK_ID
POSITION_X
POSITION_Y
FRAME
```

Place the CSV file inside the `data/` folder.

Example:

```
data/
└── Example_Spots in tracks statistics.csv
```

---

## Usage

Run the main script:

```bash
python main.py
```

Example `main.py`:

```python
from pathlib import Path
import pandas as pd

from SPT_MSS_tools.mss.analysis import analyze_track_MSS

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

spots_csv = data_folder / "FNSDF_Series001fixed1_Spots in tracks statistics.csv"

pd_spots = pd.read_csv(spots_csv)

trajectory_xy = pd_spots[['TRACK_ID','POSITION_X','POSITION_Y','FRAME']]

sMSS = analyze_track_MSS(
    trajectory_xy,
    track_id=45,
    plot=True
)

print(f"sMSS: {sMSS}")
```

Running the script will:

1. Load the TrackMate trajectory table
2. Extract a selected track
3. Compute the **Moment Scaling Spectrum**
4. Estimate the **sMSS slope**
5. Display trajectory and MSS plots (if enabled)

---

## Output

The script prints the sMSS value:

```
sMSS: 0.82
```

And optionally generates plots:

* **Trajectory plot**
* **γᵥ vs v (Moment scaling spectrum)**

---

## Interpretation of sMSS

Typical interpretations:

| sMSS | Diffusion type   |
| ---- | ---------------- |
| 0 | stationary |
| 0 < sMSS < 0.5| confined diffusion     |
| ~0.5   | normal diffusion |
| 0.5 < sMSS < 1   | super diffusion   |
| 1 | ballistic |

These thresholds may vary depending on the experimental system and acquisition conditions.

This code still can give negative values for sMSS. This happens when the trajectories are non self-similar.

---

## Notes

* The MSS calculation uses lags up to **one third of the trajectory length**, which is a common practice in trajectory analysis.
* Negative sMSS values can occur when **a trajectory contains abnormal jumps**. The code attempts a **single correction by trimming the last frame**.

---

## License

MIT License

---

## Author

Developed for **single-particle tracking analysis** and diffusion characterization.
