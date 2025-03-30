""" Plot yearly CT emissions. """

__author__ = "technologeve"

# Standard library imports
import argparse

# External imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    """ Main function. """

    # Pass in the file as command line input
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename", type=str, 
        help="Filepath to 'co2ml95models.csv' dataset from the paper"
        " 'Counting Carbon: A Survey of Factors Influencing the Emissions of Machine Learning'")
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.filename)

    # Filter data to 2021
    df = df[df["Year published"] == 2021]
    # Format C02 into log scale
    df["Log CO₂eq emitted [kg]"] = np.log(df["CO₂eq emitted [kg]"])

    # Create the plot
    sns.boxplot(df, x="Task", y="Log CO₂eq emitted [kg]",
                palette=["#055D25", "#5c053c", "#9bbea7", "#97709e", "#055D25"])
    plt.title("Estimated cost of training ML model, by task", fontsize=15)
    plt.xlabel("Task", fontsize=20)
    plt.ylabel("Log CO₂eq emitted [log kg]", fontsize=15)

    plt.plot([0,4], [np.log(54000000)]*2, color="blue",
            label="Estimated UK\nyearly emissions\nfor CT scans (log kg)")

    plt.xticks([0,1,2,3,4], fontsize=15, labels=[
        "Named\nEntity\nRecognition",
        "Image\nClassification", 
        "Machine\nTransation",
        "Object\nDetection", 
        "Question\nAnswering"
    ])
    plt.yticks(fontsize=14)
    plt.legend(fontsize=14)
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
