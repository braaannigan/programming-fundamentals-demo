import sys
from pathlib import Path

import pandas as pd


def getPaths():
    """
    Generate the paths to the data directories
    """
    dataPath = Path("data")
    rawDataPath = dataPath / "raw"
    interimDataPath = dataPath / "interim"
    processedDataPath = dataPath / "processed"
    if not interimDataPath.exists():
        interimDataPath.mkdir()
    if not processedDataPath.exists():
        processedDataPath.mkdir()
    return rawDataPath, interimDataPath, processedDataPath


def generateFilename(dataset: str) -> str:
    """
    Generate the filename for the full and test dataset
    """
    filename = "atlanticInterpolated"
    if dataset == "test":
        filename += "test"
    filename += ".csv"
    return filename


def parseArgs():
    """
    Parse the user arguments for the full or test dataset
    """
    if len(sys.argv) > 1:
        dataset = sys.argv[1]
    else:
        dataset = ""
    return dataset


def main() -> pd.DataFrame:
    """
    Main function to load the data
    """
    dataset = parseArgs()
    rawDataPath, interimDataPath, processedDataPath = getPaths()
    filename = generateFilename(dataset=dataset)
    filePath = rawDataPath / filename
    df = pd.read_csv(filePath)
    return df


if __name__ == "__main__":
    main()
