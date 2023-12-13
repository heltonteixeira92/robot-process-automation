"""this script changes/organizes files into folders"""

import os
from tkinter.filedialog import askdirectory

source_folder = askdirectory(title="Pasta Origem")
destination_folder = askdirectory(title="Pasta Destino")

file_rules = {
    # file: folder
    'jan': 'Janeiro',
    'fev': 'Fevereiro',
    'mar': 'Março',
}

file_list = os.listdir(source_folder)

for file_name in file_list:
    for key in file_rules.keys():
        if key in file_name:
            new_folder = file_rules[key]

            original_full_name = os.path.join(destination_folder, file_name)
            final_full_name = os.path.join(destination_folder, new_folder, file_name)

            new_folder_path = os.path.join(destination_folder, new_folder)
            if not os.path.exists(final_full_name):
                os.mkdir(new_folder_path)

            os.rename(original_full_name, final_full_name)