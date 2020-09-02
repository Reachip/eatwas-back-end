import xlrd
import os

ciqual_wb = xlrd.open_workbook(filename=os.environ.get("CIQUAL_PATH"))
green_peace_wb = xlrd.open_workbook(filename=os.environ.get("GREENPEACE_PATH"))

