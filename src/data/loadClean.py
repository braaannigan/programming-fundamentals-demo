from typing import Tuple
from pathlib import Path

import pandas as pd
import xarray as xr


def getPaths() -> Tuple(Path, Path, Path):
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
    filename = "atlanticInterpolated"
    if dataset == "test":
        filename += "test"
    filename += ".csv"
    return filename


def loadDataFromCSV(duplicateN: int = 1) -> pd.DataFrame:
    rawDataPath, interimDataPath, processedDataPath = getPaths()
    df = pd.read_csv(rawDataPath / "atlanticInterpolated.csv")
    z = df.z.values
    dropColumns = []
    for col in df.columns:
        if df.loc[30, col] > df.loc[0, col] - 0.1:
            dropColumns.append(col)
    df = df.drop(columns=dropColumns)
    df = pd.concat([df for _ in range(duplicateN)], axis=1)
    temps = df.iloc[:, 1:].values
    surfaceTemps = temps[:2, :].mean(axis=0)
    return df, temps, z, surfaceTemps
