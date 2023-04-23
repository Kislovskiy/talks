from plot_common_chart import plot_common_chart


def test_plot_common_chart():
    fig = plot_common_chart()

    assert len(fig.axes) == 1

    assert len(fig.axes[0].lines) == 4

    assert fig.axes[0].lines[0].get_label() == "label 1"
    assert fig.axes[0].lines[1].get_label() == "label 2"
    assert fig.axes[0].lines[2].get_label() == "y_arrow"
    assert fig.axes[0].lines[3].get_label() == "x_arrow"
