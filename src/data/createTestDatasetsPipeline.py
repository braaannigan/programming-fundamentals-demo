import xarray as xr

import src.data.loadData as loadData

dataset = "full"
ds = loadData.loadRawData(dataset=dataset)

testDs = xr.concat(
    [
        ds.sel(time=slice("2004-04-07", "2004-04-07")),
        ds.sel(time=slice("2020-03-04", "2020-03-04")),
    ],
    dim="time",
)
dataset = "test"
dataPath, rawDataPath, interimDataPath = loadData.getDataPaths()
filename = loadData.generateFilename(dataset=dataset)

testDs.to_netcdf(rawDataPath / filename)
