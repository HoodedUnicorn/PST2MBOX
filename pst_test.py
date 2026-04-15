import pypff

pst = pypff.file()
pst.open("i.bakker@wxs.nl.pst")

root = pst.get_root_folder()

print("Root:", root.name)
print("Folders:", root.number_of_sub_folders)
print("Messages:", root.number_of_sub_messages)