import speedtest
speed=speedtest.Speedtest()
download=speed.download()
upload=speed.upload()
print(f"Download speed {download}")
print(f"Upload speed {upload}")

