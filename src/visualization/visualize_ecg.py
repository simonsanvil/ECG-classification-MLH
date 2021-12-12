from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)


def plot_ecg(uploaded_ecg,FS):
    ecg_1d = uploaded_ecg.reshape(-1)
    N = len(ecg_1d)
    fig,axs = plt.subplots(2,2,figsize=(8,8))
    time = np.arange(N) / FS
    p=FS*5

    for i,ax in enumerate(axs.flat):
        segment = ecg_1d[i*p:(i*p+p)]
        time_segment = time[i*p:(i*p+p)]
        ax.plot(time_segment,segment)
        ax.title.set_text(f'Segment from {i*5} to {5*i+5} seconds')
        ax.set_xlabel('Time in s')
        ax.set_ylabel('ECG in mV')

        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))

        ax.xaxis.set_minor_locator(AutoMinorLocator(4))
        ax.yaxis.set_minor_locator(AutoMinorLocator(4))

        ax.grid(which='major', color='#CCCCCC', linestyle='--')
        ax.grid(which='minor', color='#CCCCCC', linestyle=':')

    fig.tight_layout()
    return fig