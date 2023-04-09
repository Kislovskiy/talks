from matplotlib import pyplot as plt


def despine(axis: plt.Axes):
    return axis.spines[["top", "right"]].set_visible(False)
