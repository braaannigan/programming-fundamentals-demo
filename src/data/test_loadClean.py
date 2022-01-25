from src.data.loadClean import *


def test_generateFilename():
    dataset = "test"
    output = generateFilename(dataset=dataset)
    target = "moc_transports_modtest.nc"
    assert output == target
