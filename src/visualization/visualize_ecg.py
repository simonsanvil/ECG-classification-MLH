from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from subplotted import subplotted

def plot_ecg(uploaded_ecg,FS):
    '''
    Visualize the ECG signal. 
    
    Parameters
    ----------
    uploaded_ecg : numpy.ndarray
        The ECG signal as a numpy array.
    FS : int
        The sampling frequency of the ECG signal.
    
    Returns
    -------
        The figure object created by matplotlib of the ECG signal. 
    '''
    ecg_1d = uploaded_ecg.reshape(-1)
    N = len(ecg_1d)
    # fig,axs = plt.subplots(2,2,figsize=(4,4))
    time = np.arange(N) / FS
    p=FS*5

    for S,ax,i in subplotted(int(np.ceil(len(time)/p)),ncols=2,figsize=(8,10)):
        segment = ecg_1d[i*p:(i*p+p)]
        time_segment = time[i*p:(i*p+p)]
        ax.plot(time_segment,segment)
        ax.set_title(f'Segment from {i*5} to {5*i+5} seconds',fontsize=7)
        ax.set_xlabel('Time in s',fontsize=5)
        ax.set_ylabel('ECG in mV',fontsize=5)
        ax.set_ylim([segment.min()-.5,segment.max()+.5])
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))

        ax.xaxis.set_minor_locator(AutoMinorLocator(4))
        ax.yaxis.set_minor_locator(AutoMinorLocator(4))

        ax.grid(which='major', color='#CCCCCC', linestyle='--')
        ax.grid(which='minor', color='#CCCCCC', linestyle=':')
        ax.xaxis.set_tick_params(labelsize=6)
        ax.yaxis.set_tick_params(labelsize=6)

    S.fig.tight_layout()
    return S.fig