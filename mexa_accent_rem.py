import os
count1, count2 = 0, 0

def rem_accent(text):
    global count1
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n', 'ü': 'u'}
    for acento, no_accent in accents.items():
        text = text.replace(acento, no_accent)
        count1 += 1
    return text

def process_file(filee):
    global count2
    try:                            # modifica el encoding del file!
        with open(filee, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content_wo_accents = rem_accent(content)
                                        #encoding 
        with open(filee, 'w', encoding='utf-8') as f:
            f.write(content_wo_accents)
        count2 += 1    
    except Exception as e:
        print(f"Error processing file:  {filee}: {e}")

def process_folder(folder):
    try:
        for filee in os.listdir(folder):
            if filee.endswith('.txt'):
                whole_file_route = os.path.join(folder, filee)
                process_file(whole_file_route)
    except Exception as e:
        print(f"Error processing ffolder {folder}: {e}")

# Cambia 'ruta_de_tu_carpeta', yo puse un "raw_string" para que leyera las barras, pero usa lo que quieras
process_folder(r'C:route\to\folder')

os.system('cls')
print("Nothing left!    Files done!")
print(f"# of accents modified: {count1}\n")
print(f"# of files modified: {count2}")
