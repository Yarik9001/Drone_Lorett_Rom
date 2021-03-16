from time import sleep
from os import system
import sdr

system("ntpdate")
reciver = sdr.OSMO_SDR("airspy")

if reciver.load_config("METOP-C"):
    reciver.start("liteSDR-METOP-C.iq")
    sleep(100)
    reciver.stop()
