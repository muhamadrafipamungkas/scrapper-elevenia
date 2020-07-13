import sys
from scrapper import ScrapperElevenia

inp = sys.argv
if(len(inp) == 1):
    print("Harap sertakan link produk Elevenia")
else:
    coba = ScrapperElevenia(str(inp[1]))
    coba.getPrice()

