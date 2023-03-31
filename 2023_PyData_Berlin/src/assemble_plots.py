from importlib.util import module_from_spec, spec_from_file_location
from inspect import getmembers, isfunction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def main():
    # Get a list of all the Python files in the directory
    plot_files = Path(__file__).parent.glob("plot_*.py")
    results_dir = Path(__file__).resolve().parent.parent / "results"
    with PdfPages(f"{results_dir}/assembled.pdf") as pdf:
        # Loop over each Python file in the directory
        for file in plot_files:
            # Import the module containing the plotting functions
            spec = spec_from_file_location("module.name", file)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, func in getmembers(module, isfunction):
                # Skip any functions that don't start with "plot_"
                print(name)
                if not name.startswith("plot_") or name == "plot_nothing":
                    continue

                fig = func()
                # Add the plot to the PDF document as a separate page
                pdf.savefig(fig)
                plt.close(fig)


if __name__ == "__main__":
    main()
