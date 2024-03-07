import csv
import time
from LinkedList import LinkedList
from SkipList import SkipList

gene_list_file = 'gene_list.csv'
element_to_search = 'MYCN'

with open(gene_list_file, encoding = 'UTF-8') as file:
    csv_file = csv.reader(file)
    gene_list = [x for row in csv_file for x in row]

gene_list = list(set(gene_list))

gene_linked_list = LinkedList()
gene_linked_list.readCSV(gene_list_file)

gene_skip_list = SkipList()
gene_skip_list.readCSV(gene_list_file)

# Testing the search speed of regular Python list
start_time = time.time()
print(gene_list[gene_list.index(element_to_search)])
end_time = time.time()
runtime = end_time - start_time
print(f'Python list Runtime: {runtime:.8f} seconds')

# Testing the search speed of linked list
start_time = time.time()
print(gene_linked_list.find(element_to_search).data)
end_time = time.time()
runtime = end_time - start_time
print(f'Linked list Runtime: {runtime:.8f} seconds')

# Testing the search speed of SkipList
start_time = time.time()
print(gene_skip_list.find(element_to_search).elem)
end_time = time.time()
runtime = end_time - start_time
print(f'SkipList Runtime: {runtime:.8f} seconds')
