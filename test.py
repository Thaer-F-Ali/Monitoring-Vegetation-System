from osgeo import gdal
import sys

fn = "G:/temp/boatman1-2-eg4.tif"
ds = gdal.Open(fn)
if not ds:
    print("Unable to open the file")
    sys.exit(1)
  
#Create Copy of Raster
driver = gdal.GetDriverByName("GTiff")
des_fn = "G:/temp/new6_boatman1-2-eg4.tif"
dst_ds = driver.CreateCopy(des_fn, ds, strict=0)


#fetching bands of the raster
Band = [1,2,3,4,5,6]
for i in range(1,6):
    Band[i] = ds.GetRasterBand(i)
   
print("the file was fetched successfully")

xsize1 = Band[1].XSize
ysize1 = Band[1].YSize

import struct
#getting data in the raster
y = 1
while y < xsize1:
    scanline1 = Band[3].ReadRaster(xoff=0, yoff= 0, xsize = xsize1 , ysize= y, buf_xsize= xsize1, buf_ysize =1, buf_type = gdal.GDT_Float32)
    scanline2 = Band[4].ReadRaster(xoff=0, yoff= 0, xsize = xsize1 , ysize= y, buf_xsize= xsize1, buf_ysize =1, buf_type = gdal.GDT_Float32)
    
    tuple_of_floats1 = struct.unpack('f' * Band[3].XSize, scanline1)
    tuple_of_floats2 = struct.unpack('f' * Band[4].XSize, scanline2)
    
    # Printing values into the new raster
    if (tuple_of_floats1[y] - tuple_of_floats2[y]) == 2:
        print("ok")
    else:
        print(tuple_of_floats1)
    y = y + 1
#     input(sum)
print("data of the file have been got")

print("the value of x is ", xsize1, " the value of y is ", ysize1)

ds = None
dst_ds = None
print("Here is the statment where the GitHup is added")
print("the file has written successfully")
