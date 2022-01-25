from time import time
import src.data.loadClean as loadClean
import src.analysis.timeseries as timeseries

dataset = "full"
ds = loadClean.loadRawData(dataset=dataset)
timeAverage = timeseries.getTimeAverage(ds=ds, freq="year")
