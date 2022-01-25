import xarray as xr

import src.data.loadClean as loadClean

datasets = ["test", "full"]
for dataset in datasets:
    ds = loadClean.loadRawData(dataset=dataset)
