from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data_cleaned.csv", index_col=0)
with PdfPages('plots.pdf') as pdf:
    for label in df.columns:
        if label not in  ["Locality", "Build Year"]:
            plt.figure()
            if label == "Price" or "SURFACE" in label.upper():
                df[label].plot.hist(bins=200)
            else:
                df[label].value_counts(dropna=False).plot(kind = 'barh')
            plt.title(f"Values of {label}")
            pdf.savefig()
            plt.close()
    for label in df.columns:
        if label == "Price" or "SURFACE" in label.upper():
            plt.figure()
            df[label].plot.box()
            plt.title(f"Boxplot of {label}")
            pdf.savefig()
            plt.close()
