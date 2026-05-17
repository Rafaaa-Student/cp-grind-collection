"""

Competitive Programming Solutions Collection

=============================================

42+ problems from Codeforces & LeetCode

Topics: Implementation, Two Pointers, Sliding Window, Greedy, Strings



Lang: Python 3

Solved with love ☕

"""



import sys



# =========================================

# PROBLEM 1 (231A / TEAM)

# =========================================

input_data = int(sys.stdin.readline().strip())

solved_input = 0

for i in range(input_data):

    panjang_input = list(map(int, sys.stdin.readline().split()))

    if sum(panjang_input) >= 2:

        solved_input += 1

print(solved_input)



# =========================================

# PROBLEM 2 (71A / WAY TOO LONG)

# =========================================

word = sys.stdin.readline().strip()



if len(word) > 10:

    middle = len(word) - 2

    print(word[0] + str(middle) + word[-1])

else:

    print(word)



# =========================================

# PROBLEM 3 (4A / WATERMELON)

# =========================================

w = int(sys.stdin.readline().strip())



if w % 2 == 0 and w > 2:

    print("YES")

else:

    print("NO")



# =========================================

# PROBLEM 4 (158B / TAXI)

# =========================================

n = int(sys.stdin.readline().strip())

groups = list(map(int, sys.stdin.readline().split()))



cnt1 = cnt2 = cnt3 = cnt4 = 0



for s in groups:

    if s == 4:

        cnt4 += 1

    elif s == 3:

        cnt3 += 1

    elif s == 2:

        cnt2 += 1

    elif s == 1:

        cnt1 += 1



taxi = cnt4



taxi += cnt3

cnt1 = max(0, cnt1 - cnt3)



taxi += cnt2 // 2

if cnt2 % 2 == 1:

    taxi += 1

    cnt1 = max(0, cnt1 - 2)



if cnt1 > 0:

    taxi += (cnt1 + 3) // 4



print(taxi)



# =========================================

# PROBLEM 5 (TWO SUM - LeetCode)

# =========================================

nums = list(map(int, sys.stdin.readline().split()))

target = int(sys.stdin.readline().strip())



for i in range(len(nums)):

    for j in range(i + 1, len(nums)):

        if nums[i] + nums[j] == target:

            print([i, j])

            break

print([])



# =========================================

# PROBLEM 6 (PALINDROME NUMBER - LeetCode)

# =========================================

s = sys.stdin.readline().strip()



if s == s[::-1]:

    print("YES")

else:

    print("NO")



# =========================================

# PROBLEM 7 (STRING PROBLEM)

# =========================================

s = list(sys.stdin.readline().split())

z = set(s)

print(z)



# =========================================

# PROBLEM 8 (YOUNG PHYSICIST / 69A)

# =========================================

n = int(sys.stdin.readline().strip())



sumX = sumY = sumZ = 0

for _ in range(n):

    x, y, z = map(int, sys.stdin.readline().split())

    sumX += x

    sumY += y

    sumZ += z



if sumX == 0 and sumY == 0 and sumZ == 0:

    print("YES")

else:

    print("NO")



# =========================================

# PROBLEM 9 (NUMBER BETWEEN TWO OTHERS / 2225A)

# =========================================

t = int(sys.stdin.readline().strip())

x, y = map(int, sys.stdin.readline().split())



if y // x == 2:

    print("NO")

else:

    print("YES")



# =========================================

# PROBLEM 10 (DOMINO PILLING / 50A)

# =========================================

n, m = map(int, sys.stdin.readline().split())

print(n * m // 2)



# =========================================

# PROBLEM 11 (BOY OR GIRL / 236A)

# =========================================

username = sys.stdin.readline().strip()

print("IGNORE HIM" if len(set(username)) % 2 == 1 else "CHAT WITH HER")



# =========================================

# PROBLEM 12 (HELPFUL MATHS / 339A)

# =========================================

s = sys.stdin.readline().strip()

numbers = s.split('+')

numbers.sort()

print("+".join(numbers))



# =========================================

# PROBLEM 13 (PETYA AND STRINGS / 112A)

# =========================================

s = sys.stdin.readline().strip().lower()

s2 = sys.stdin.readline().strip().lower()



if s < s2:

    print("-1")

elif s > s2:

    print("1")

else:

    print("0")



# =========================================

# PROBLEM 14 (BIT++ / 282A)

# =========================================

n = int(sys.stdin.readline().strip())

x = 0



for i in range(n):

    y = sys.stdin.readline().strip()

    if "+" in y:

        x += 1

    else:

        x -= 1



print(x)



# =========================================

# PROBLEM 15 (NEXT ROUND / 158A)

# =========================================

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))



count = 0

for i in range(n):

    if a[i] >= a[k - 1] and a[i] > 0:

        count += 1



print(count)



# =========================================

# PROBLEM 16 (THEATRE SQUARE / 1A)

# =========================================

n, m , a = map(int, sys.stdin.readline().split())

persegi = (n + a - 1) // a

panjang = (m + a - 1) // a



hasil = persegi * panjang

print(hasil)



# =========================================

# PROBLEM 17 (CHAT ROOM / 58A)

# =========================================

s = list(sys.stdin.readline().strip())

target = "hello"



it = iter(s)

if all(x in it for x in target):

    print("YES")

else:

    print("NO")



# =========================================

# PROBLEM 18 (TWINS / 160A)

# =========================================

n = int(sys.stdin.readline().strip())

koin = list(map(int, sys.stdin.readline().split()))

total = sum(koin)

me_uang = 0



koin.sort(reverse=True) 



for i in range(n):

    me_uang += koin[i]

    if me_uang > total - me_uang:

        print(i + 1)

        break



# =========================================

# PROBLEM 19 (LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS)

# =========================================

s = sys.stdin.readline().strip()

seen = set()

i = 0

maks = 0



for j in range(len(s)):

    while s[j] in seen:

        seen.remove(s[i])

        i += 1

    seen.add(s[j])

    operasi = j - i + 1

    maks = max(maks, operasi)



print(maks)



# =========================================

# PROBLEM 20 (BOOKS / 279B)

# =========================================

n, t = map(int, sys.stdin.readline().split())

buku = list(map(int, sys.stdin.readline().split()))

i = 0

maksimum = 0

total = 0



for j in range(n):

    total += buku[j]

    while total > t:

        total -= buku[i]

        i += 1

    maksimum = max(maksimum, j - i + 1)



print(maksimum)



# =========================================

# PROBLEM 21 (INCREASING SEQUENCE / 11A)

# =========================================

n, d = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

total_langkah = 0



for i in range(1, n):

    if data[i] <= data[i - 1]:

        sisa = data[i - 1] - data[i]

        langkah = (sisa // d) + 1

        data[i] += langkah * d

        total_langkah += langkah



print(total_langkah)



# =========================================

# PROBLEM 22 (FAVORITE SEQUENCE / 1462A)

# =========================================

t = int(sys.stdin.readline().strip())

n = int(sys.stdin.readline().strip())

data = list(map(int, sys.stdin.readline().split()))



kiri = 0

kanan = n - 1

skor = []



for _ in range(t):

    while kiri <= kanan:

        skor.append(data[kiri])

        if kiri != kanan:

            skor.append(data[kanan])

        kiri += 1

        kanan -= 1



print(*skor)



# =========================================

# PROBLEM 23 (SEREJA AND DIMA / 381A)

# =========================================

n = int(sys.stdin.readline().strip())

data = list(map(int, sys.stdin.readline().split()))



kiri = 0

kanan = n - 1

skor_sereja = 0

skor_dima = 0

turn_sereja = True



while kiri <= kanan:

    if data[kiri] > data[kanan]:

        get = data[kiri]

        kiri += 1

    else:

        get = data[kanan] 

        kanan -= 1



    if turn_sereja:

        skor_sereja += get

    else:

        skor_dima += get



    turn_sereja = not turn_sereja



print(skor_sereja, skor_dima)



# =========================================

# PROBLEM 24 (RATA RATA PENJUALAN 6 BARANG)

# =========================================

data = []

for i in range(6):

    n = int(sys.stdin.readline().strip())

    data.append(n)

hasil = sum(data) / len(data)

print(hasil)



# =========================================

# PROBLEM 25 (CHEWBACCA AND NUMBER / 518A)

# =========================================

x = sys.stdin.readline().strip()

s = list(x)



for i in range(len(s)):

    digit = int(s[i])

    kebalikan = 9 - digit

    if i == 0 and digit == 9:

        continue

    if kebalikan < digit:

        s[i] = str(kebalikan)



print(''.join(s))



# =========================================

# PROBLEM 26 (STONES ON THE TABLE / 266A)

# =========================================

n = int(sys.stdin.readline().strip())

s = sys.stdin.readline().strip()

hasil = 0



for i in range(1, n):

    if s[i] == s[i - 1]:

        hasil += 1



print(hasil)



# =========================================

# PROBLEM 27 (ELEPHANT / 617A)

# =========================================

x = int(sys.stdin.readline().strip())

gajah = 0



langkah = (x + 3 - 1) // 3



gajah += langkah

print(gajah)



# =========================================

# PROBLEM 28 (SOLDIER AND BANANAS / 546A)

# =========================================

k, n, w = map(int, sys.stdin.readline().split())

total = k * (w * (w + 1) // 2)

print(max(0, total - n))



# =========================================

# PROBLEM 29 (BEAUTIFUL MATRIX / 263A)

# =========================================

hasil = 0

for i in range(5):

    baris = sys.stdin.readline().split()

    if '1' in baris:

        j = baris.index('1')

        hasil = abs(i - 2) + abs(j - 2)



print(hasil)



# =========================================

# PROBLEM 30 (PRESENTS / 136A)

# =========================================

n = int(sys.stdin.readline().strip())

p = list(map(int, sys.stdin.readline().split()))

total = [0] * n



for i in range(n):

    pemberi = i + 1

    penerima = p[i]     

    total[penerima - 1] = pemberi



print(*total)



# =========================================

# PROBLEM 31 (FOOTBALL / 96A)

# =========================================

n = sys.stdin.readline().strip()

count = 1



if 1 < len(n) < 100:

    for i in range(len(n) - 1):

        if n[i] == n[i + 1]:

            count += 1

        else:

            count = 1

        if count == 7:

            print("YES")

            exit()

    print("NO")



# =========================================

# PROBLEM 32 (STRING TASK / 118A)

# =========================================

s = sys.stdin.readline().strip()

vowels = 'aeiouy'

hasil = ""

for char in s:

    if char.lower() not in vowels:

        hasil += '.'

        hasil += char.lower()



print(hasil)



# =========================================

# PROBLEM 33 (LUCKY NUMBER / 122A)

# =========================================

n = int(sys.stdin.readline().strip())

lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]



is_lucky_divisible = any(n % lucky == 0 for lucky in lucky_numbers)



if is_lucky_divisible:

    print("YES")

else:

    print("NO")

                    # CARA KE 2 #

lucky_numbers = []

def generate_lucky(current_num):

    if current_num > 1000: 

        return

    if current_num > 0:

        lucky_numbers.append(current_num)



    generate_lucky(current_num * 10 + 4)

    generate_lucky(current_num * 10 + 7)



generate_lucky(0)



sys.stdout.write(str(lucky_numbers))



# =========================================

# PROBLEM 34 (TRAM / 116A)

# =========================================

n = int(sys.stdin.readline().strip())



pengunjung_maksimal = 0

pengunjung_now = 0



for _ in range(n):

    a, b = map(int, sys.stdin.readline().strip().split())

    pengunjung_now += (b - a)

    pengunjung_maksimal = max(pengunjung_maksimal, pengunjung_now)



sys.stdout.write(str(pengunjung_maksimal))



# =========================================

# PROBLEM 35 (DRAGONS / 230A)

# =========================================

s, n = map(int, sys.stdin.readline().split())

daftar = []



for i in range(n):

    x, y = map(int, sys.stdin.readline().split())

    daftar.append((x, y))



daftar.sort()



for x, y in daftar:

    if s >= x:

        s += y

    else:

        print("NO")

        break

else:

    print("YES")



# =========================================

# PROBLEM 36 (MINIMUM SIZE SUB ARRAY SUM / 209)

# =========================================

daftar = list(map(int, sys.stdin.readline().split()))

n = len(daftar)



i = 0

total = 0

panjang = float('inf')

panjang_sekarang = 0



for j in range(n):

    total += daftar[j]

    while total >= 7:

        panjang_sekarang = j - i + 1

        panjang = min(panjang, panjang_sekarang)



        total -= daftar[i]

        i += 1



print(panjang if panjang != float('inf') else 0)



# =========================================

# PROBLEM 37 (ROMANS TO INTEGER - LeetCode)

# =========================================

nilai = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

teks = sys.stdin.readline().strip().upper()



teks = teks.replace("IV", "IIII").replace("IX", "VIIII")

teks = teks.replace("XL", "XXXX").replace("XC", "LXXXX")

teks = teks.replace("CD", "IIII").replace("CM", "DCCCC")



total = sum(nilai[huruf] for huruf in teks)



print(total)



# =========================================

# PROBLEM 38 (BERSU BALL / 489B)

# =========================================

n = int(sys.stdin.readline().strip())

lk = list(map(int, sys.stdin.readline().split()))



m = int(sys.stdin.readline().strip())

pr = list(map(int, sys.stdin.readline().split()))



lk.sort()

pr.sort()



i = 0

j = 0

total = 0



while i < n and j < m:

    selisih = abs(lk[i] - pr[j])

    if selisih <= 1:

        i += 1

        j += 1

        total += 1

    else:

        if lk[i] <= pr[j]:

            i += 1

        else:

            j += 1

print(total)



# =========================================

# PROBLEM 39 (CELLULAR NETWORK / 702C)

# =========================================

def solve():

    n , m = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))

    b = list(map(int, sys.stdin.readline().split()))



    j = 0

    r_maksimal = 0



    for i in range(n):

        while j + 1 < m and abs(b[j + 1] - a[i]) <= abs(b[j] - a[i]):

            j += 1

        r_maksimal = max(r_maksimal, abs(b[j] - a[i]))



    print(r_maksimal)



# =========================================

# PROBLEM 40 (VASYA AND STRINGS / 676C)

# =========================================

n, k = map(int, sys.stdin.readline().split())

data = list(sys.stdin.readline().strip())



i = 0

jumlah_b = 0

maks_A = 0



for j in range(n):

    if data[j] == 'b':

        jumlah_b += 1



    while jumlah_b > k:

        if data[i] == 'b':

            jumlah_b -= 1

        i += 1



    maks_A = max(maks_A, j - i + 1)



i = 0

jumlah_a = 0

maks_B = 0



for j in range(n):

    if data[j] == 'a':

        jumlah_a += 1



    while jumlah_a > k:

        if data[i] == 'a':

            jumlah_a -= 1

        i += 1



    maks_B = max(maks_B, j - i + 1)



print(max(maks_A, maks_B))



# =========================================

# PROBLEM 41 (BALANCED TEAM / 1133C)

# =========================================

n = int(sys.stdin.readline().strip())

daftar = list(map(int, sys.stdin.readline().split()))

daftar.sort()



i = 0

maximum = 0

now = 0



for j in range(n):

    while daftar[j] - daftar[i] > 5:

        i += 1

    now = j - i + 1

    maximum = max(maximum, now)



sys.stdout.write(str(maximum))



# =========================================

# PROBLEM 42 (TERNARY STRING / 1354B)

# =========================================

t = int(sys.stdin.readline().strip())



for _ in range(t):

    s = sys.stdin.readline().strip()

    n = len(s)



    i = 0

    min_len = float('inf') 

    counts = {}



    for j in range(n):

        if s[j] in counts:

            counts[s[j]] += 1

        else:

            counts[s[j]] = 1



        while len(counts) == 3:

            min_len = min(min_len, j - i + 1)



            counts[s[i]] -= 1

            if counts[s[i]] == 0:

                del counts[s[i]]

            i += 1



    print(min_len if min_len != float('inf') else 0)

