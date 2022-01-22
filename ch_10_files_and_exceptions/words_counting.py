"""
count word choising  
"""
def count(word,file_name):
    try:
        with open(file_name) as f:
            content=f.read()
    except FileNotFoundError:
        print("file not found")
    else:
        c=content.lower().count(word.lower())
        print(f"{word} have been used {c} times")
count("gambling","the_gambler.txt")