import csv
import time
from SkipList import SkipList

with open('gene_list.csv', encoding = 'UTF-8') as file:
    csv_file = csv.reader(file)
    gene_list = [x for row in csv_file for x in row]

gene_list = list(set(gene_list))

gene_skip_list = SkipList()
gene_skip_list.readCSV('gene_list.csv')

element_to_delete = 'MYCN'

# Testing the deletion speed of regular Python list
start_time = time.time()
gene_list.remove(element_to_delete)
end_time = time.time()
runtime = end_time - start_time
print(f'Python list Runtime: {runtime:.8f} seconds')

# Testing the deletion speed of SkipList
start_time = time.time()
gene_skip_list.remove(element_to_delete)
end_time = time.time()
runtime = end_time - start_time
print(f'SkipList Runtime: {runtime:.8f} seconds')
