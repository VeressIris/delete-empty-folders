import os

directory = input("From what directory would you like to remove all empty folders? ")

deleted_folder_count = 0

def search(search_dir):
    if not os.listdir(search_dir):
        os.rmdir(search_dir)

        global deleted_folder_count
        deleted_folder_count += 1
        
        return
    else:
        for f in os.listdir(search_dir):
            new_search_dir = search_dir + "/" + f
            if os.path.isdir(new_search_dir):
                search(new_search_dir)

# first search
search(directory)

total_deleted_folder_count = deleted_folder_count

# keep searching the directory until all emtpy folders are deleted
while not deleted_folder_count == 0:
    deleted_folder_count = 0
    search(directory)
    total_deleted_folder_count += deleted_folder_count

if total_deleted_folder_count == 0:
    print("There were no empty folders in this directory.")
else:
    print("Deleted " + str(total_deleted_folder_count) + " folders!")
