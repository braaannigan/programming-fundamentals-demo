from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

# Use this import * approach - it means you can use the same function names when running interactively
from src.data.loadClean import *


def test_getPaths():
    rawDataPath, interimDataPath, processedDataPath = getPaths()
    assert interimDataPath.exists()
    assert processedDataPath.exists()


@pytest.mark.parametrize(
    "dataset,target",
    [("test", "atlanticInterpolatedtest.csv"), ("", "atlanticInterpolated.csv")],
)
def test_generateFilename(dataset, target):
    output = generateFilename(dataset=dataset)
    assert output == target


@pytest.mark.parametrize(
    "testArgs,targetDataset",
    [
        (
            [
                "loadClean.py",
            ],
            "",
        ),
        (
            ["loadClean.py", "dataset"],
            "dataset",
        ),
    ],
)
def test_parseArgs(testArgs, targetDataset):
    # Overwrite the sys.argv so we can check parseArgs returns the correct values
    with patch.object(sys, "argv", testArgs):
        outputDataset = parseArgs()
        assert outputDataset == targetDataset


# Use parametrize here to test both the test dataset and the full dataset
@pytest.mark.parametrize(
    "testArgs,targetDatasetColumns",
    [
        (
            [
                "loadClean.py",
            ],
            3926,
        ),
        (
            ["loadClean.py", "test"],
            3,
        ),
    ],
)
def test_main(testArgs, targetDatasetColumns):
    # Overwrite the sys.argv so we can check parseArgs returns the correct values
    with patch.object(sys, "argv", testArgs):
        df = main()
        assert isinstance(df, pd.DataFrame)
        assert "z" in df.columns
        assert df.shape[0] == 199
        assert df.shape[1] == targetDatasetColumns
