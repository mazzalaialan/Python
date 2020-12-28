import csv

reader = csv.reader(['Hola|, Mundo', 'Python'], escapechar='|')

file_content = list(reader)

print(file_content)