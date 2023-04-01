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
    with PdfPages(path_to_assembled_pdf) as pdf:
        # Loop over each Python file in the directory that starts with "plot_"
        for file in Path(__file__).parent.glob("plot_*.py"):
            # Import the module containing the plotting functions
            spec = spec_from_file_location("src", file)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, func in getmembers(module, isfunction):
                # Skip any functions that don't start with "plot_"
                print(name)
                if not name.startswith("plot_") or name.startswith("plot_nothing"):
                    continue

                fig = func()
                pdf.savefig(fig)
                plt.close(fig)


if __name__ == "__main__":
    main()
