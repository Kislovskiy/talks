from matplotlib import pyplot as plt


def despine(axis: plt.Axes, which_spines: list = ["top", "right"]) -> plt.Axes:
    return axis.spines[which_spines].set_visible(False)


def remove_ticks(axis: plt.Axes) -> plt.Axes:
    axis.tick_params(axis="both", which="both", length=0)
    axis.set_xticks([])
    axis.set_yticks([])
    return axis


def add_arrows_to_axis(axis: plt.Axes) -> plt.Axes:
    xmin, xmax = axis.get_xlim()
    ymin, ymax = axis.get_ylim()
    axis.plot(
        xmin,
        ymax,
        "^k",
        transform=axis.get_yaxis_transform(),
        clip_on=False,
        zorder=10,
        label="y_arrow",
    )
    axis.plot(
        xmax,
        ymin,
        ">k",
        transform=axis.get_xaxis_transform(),
        clip_on=False,
        zorder=10,
        label="x_arrow",
    )
    return axis


def add_labels_to_lines(
    axis: plt.Axes, label: str, x_delta: float = 0.02, y_delta: float = 0
) -> plt.Axes:
    for line in axis.lines:
        if line.get_label().startswith(label):
            latest_x, latest_y = line.get_data()

    axis.text(
        latest_x[-1] + x_delta,
        latest_y[-1] + y_delta,
        label,
        ha="left",
        va="center",
        fontsize=12,
    )

    return axis


def format_yticklabels_with_celsius(ax: plt.Axes) -> plt.Axes:
    yticks = ax.get_yticks()
    yticklabels = [f"{temp:.1f}°C" for temp in yticks]
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    ax.spines[["bottom", "left"]].set_color("dimgrey")

    ax.tick_params(axis="x", colors="dimgrey", labelsize=10)
    ax.tick_params(axis="y", colors="dimgrey", labelsize=10)

    return ax
