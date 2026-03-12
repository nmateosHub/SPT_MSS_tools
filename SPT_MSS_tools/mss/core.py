import numpy as np


def compute_moment_scaling(traj, v_list, max_lag=None):

    # traj is expected to be a 2D array with shape (n, 2) where n is the number of time points
    # and the two columns correspond to x and y positions. The units of the positions are assumed
    #  to be in micrometers (µm). Unless the user specifies otherwise, we will compute the scaling 
    # exponents for moments v=0,1,2,3,4,5,6.

    n = len(traj)

    if max_lag is None:
        max_lag = n // 3

    Delta_n_list = np.arange(1, int(np.floor(max_lag)) + 1)
    # list to store the scaling exponents for each moment
    gamma_v_list = []

    for v in v_list: # loop over the different moments

        Mu_v_list = []

        for Delta_n in Delta_n_list: # loop over the different time lags

            displacement = traj[Delta_n:] - traj[:-Delta_n]
            norm_displacement = np.sqrt(displacement[:,0]**2 + displacement[:,1]**2)
            Mu_v = np.sum(norm_displacement**v) / (len(traj) - Delta_n)
            Mu_v_list.append(Mu_v)

        Mu_v_array = np.array(Mu_v_list)

        log_Delta_n = np.log(Delta_n_list)
        log_Mu_v = np.log(Mu_v_array)
        # fit a line to log-log data to get the slope, which is the scaling exponent gamma_v
        gamma_v, _ = np.polyfit(log_Delta_n, log_Mu_v, 1)
        # append the scaling exponent to the list
        gamma_v_list.append(gamma_v)

    return gamma_v_list, Delta_n_list


def compute_sMSS(traj, v_list=None, max_lag=None):

    if v_list is None:
        v_list = [0,1,2,3,4,5,6]

    gamma_v_list, _ = compute_moment_scaling(traj, v_list, max_lag=max_lag)
    
    sMSS, intercept = np.polyfit(v_list, gamma_v_list, 1)

    return sMSS, gamma_v_list