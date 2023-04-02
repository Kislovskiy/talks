from importlib.util import module_from_spec, spec_from_file_location
from inspect import getmembers, isfunction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def main():
    # Create a PDF file to store all the plots
    path_to_assembled_pdf = (
        Path(__file__).parent.parent.joinpath("results").joinpath("assembled.pdf")
    )
    path_to_assembled_pdf.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(path_to_assembled_pdf) as pdf:
        for file in Path(__file__).parent.glob("plot_*.py"):
            spec = spec_from_file_location("src", file)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, func in getmembers(module, isfunction):
                if name.startswith("plot_"):
                    fig = func()
                    if fig:
                        pdf.savefig(fig)
                        plt.close(fig)


if __name__ == "__main__":
    main()
