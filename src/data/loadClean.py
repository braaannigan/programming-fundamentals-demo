from pathlib import Path

import xarray as xr


def getDataPaths():
    # Make the Path object for the top-level data directory
    dataPath = Path("data")
    # Make the Path object for the raw data sub-directory
    rawDataPath = dataPath / "raw"
    # Make the Path object for the interim data sub-directory
    interimDataPath = dataPath / "interim"
    # Check that the interim data sub-directory exists before you try to write to it
    if not interimDataPath.exists():
        # If it doesn't exist then make the directory
        interimDataPath.mkdir()
    return dataPath, rawDataPath, interimDataPath


def generateFilename(dataset):
    filename = "moc_transports_mod"
    if dataset == "test":
        filename += "test"
    filename += ".nc"
    return filename


def loadRawData(dataset):
    dataPath, rawDataPath, interimDataPath = getDataPaths()
    filename = generateFilename(dataset=dataset)
    ds = xr.open_dataset(rawDataPath / filename)
    return ds


def cleanRawData(dataset):
    ds = loadRawData(dataset=dataset)
    newNames = {
        "t_therm10": "thermocline",
        "t_aiw10": "AIW",
        "t_ud10": "UD",
        "t_ld10": "LD",
        "t_bw10": "BW",
        "t_gs10": "GS",
        "t_ek10": "Ekman",
        "t_umo10": "UMO",
        "moc_mar_hc10": "MOC",
    }
    ds = ds.rename(name_dict=newNames)
    dataPath, rawDataPath, interimDataPath = getDataPaths()
    filename = generateFilename(dataset=dataset)
    ds.to_netcdf(interimDataPath / filename)
    return ds
