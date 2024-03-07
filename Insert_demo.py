import csv
import time
from SkipList import SkipList

with open('gene_list.csv', encoding = 'UTF-8') as file:
    csv_file = csv.reader(file)
    gene_list = [x for row in csv_file for x in row]

gene_list = list(set(gene_list))

gene_skip_list = SkipList()
gene_skip_list.readCSV('gene_list.csv')

element_to_insert = 'TEST'

# Testing the insert speed of regular Python list
start_time = time.time()
gene_list.insert(2, element_to_insert)
end_time = time.time()
runtime = end_time - start_time
print(f'Python list Runtime: {runtime:.8f} seconds')

# Testing the insert speed of SkipList
start_time = time.time()
gene_skip_list.insert(element_to_insert)
end_time = time.time()
runtime = end_time - start_time
print(f'SkipList Runtime: {runtime:.8f} seconds')
