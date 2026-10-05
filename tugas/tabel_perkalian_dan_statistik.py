print("Tabel Perkalian dan Statistik")
n = int(input("n: "))

while n <= 0:
    print("n harus lebih besar dari 0.")
    n = int(input("Masukkan n lagi: "))

total_keseluruhan = 0
counter_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end=" ")

        total_keseluruhan += hasil

        if hasil % 2 == 0:
            counter_genap += 1

        total_baris += hasil

    print(f"| Total baris = {total_baris}")

print("\nStatistik:")
print("Total keseluruhan =", total_keseluruhan)
print("Jumlah bilangan genap =", counter_genap)
