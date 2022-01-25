def getTimeAverage(ds, freq):
    freq = f"time.{freq}"
    timeAverage = ds.groupby(freq).mean()
    return timeAverage
