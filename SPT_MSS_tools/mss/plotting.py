import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory(traj, track_id=None):

    plt.figure()

    plt.plot(traj[:,0], traj[:,1], marker='o', color='black')

    plt.xlabel('Position X [μm]')
    plt.ylabel('Position Y [μm]')

    if track_id is not None:
        plt.title(f'Trajectory of Track {track_id}')
    plt.show()

def plot_gamma_vs_v(v_list, gamma_v_list, sMSS):

    intercept = np.polyfit(v_list, gamma_v_list, 1)[1]

    plt.figure()

    plt.plot(v_list, gamma_v_list, marker='o')

    plt.plot(
        v_list,
        intercept + sMSS*np.array(v_list),
        color='red',
        label=f'sMSS={sMSS:.2f}'
    )

    plt.xlabel('v')
    plt.ylabel('gamma_v')
    plt.title('gamma_v vs v')
    plt.legend()
    plt.show()