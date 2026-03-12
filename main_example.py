from pathlib import Path
import pandas as pd

from SPT_MSS_tools.mss.analysis import analyze_track_MSS


# Create data folder if it doesn't exist
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# CSV file inside data folder
spots_csv = data_folder / "FNSDF_Series001fixed1_Spots in tracks statistics.csv"

# Load data
pd_spots = pd.read_csv(spots_csv)

trajectory_xy = pd_spots[['TRACK_ID', 'POSITION_X', 'POSITION_Y', 'FRAME']]

# Run MSS analysis
sMSS = analyze_track_MSS(
    trajectory_xy,
    track_id=9,
    plot=True
)

print(f"sMSS: {sMSS}")