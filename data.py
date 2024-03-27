import os

# Mendapatkan path direktori saat ini
current_directory = os.path.dirname(os.path.realpath(__file__))

# Nama file teks
txt_file = os.path.join(current_directory, 'data.txt')

# Nama folder yang akan dibandingkan
folder_directory = current_directory

# Baca data dari file teks
with open(txt_file, 'r') as file:
    txt_data = file.read().splitlines()

# Dapatkan daftar nama folder dari direktori yang sama
folder_names = os.listdir(folder_directory)

# Bandingkan setiap nama dalam data teks dengan setiap nama folder
matches = []
mismatches = []

for name in txt_data:
    if name in folder_names:
        matches.append(name)
        folder_names.remove(name)  # Menghapus nama yang sudah cocok dari daftar folder
    else:
        mismatches.append(name)

# Identifikasi nama-nama yang cocok atau tidak cocok
print("Nama-nama yang cocok:")
print(matches)

print("\nNama-nama yang tidak cocok:")
print(mismatches)

print("\nNama-nama yang ada di folder tetapi tidak ada di data.txt:")
print(folder_names)
