""" title = "Alice in Wonderland" 
l=title.split() """
def count(file_name):
    try:
        with open(file_name) as f:
            content=f.read()
    except FileNotFoundError:
        print("file not found")
    else:
        print(f"{file_name} have {len(content)} words ")
