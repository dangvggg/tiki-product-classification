import io
import openpyxl
import re
import pandas as pd
def split_string(string):
  line = string.replace("__label__","")
  label = ''
  i=0
  while line[i] != ' ':
      label = label + line[i]
      i = i+1      
  product = line.replace(label + " ","")
  label = label.replace("_", " ")
  return label, product

def convert_txt_to_excel(input_file, output_file):
  with io.open(input_file, "r", encoding="utf-8") as f:
    data = f.readlines()
  workbook = openpyxl.Workbook()
  sheet = workbook.active
  sheet.append(["product"])
  for line in data:
    sheet.append([line])
  workbook.save(output_file)


input_file = "product_test_unlabeled.txt"
output_file = "product_test_unlabeled.xlsx"


convert_txt_to_excel(input_file, output_file)

