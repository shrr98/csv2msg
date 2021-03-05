import csv

def generate_message(data):
    sentence = "Assalamualaikum wr wb.\n\n\
Diberitahukan kepada Bapak/Ibu Wali murid bahwa tagihan administrasi untuk kelas XI atas nama *{}* sebesar *Rp {}*,-. Dengan rincian sebagai berikut.\n".format(
        data["NAMA"], data["TOTAL"]
    )

    # 1 DANA PARTISIPASI
    sentence += "1. Dana Partisipasi : Rp {},-".format(data["DANA PARTISIPASI"])
    if int(data["DANA PARTISIPASI"]) == 0:
        sentence += " ({})".format(data["KETD"])
    sentence += "\n"


    # 2. TABUNGAN
    sentence += "2. Tabungan : Rp {},- ".format(data["TABUNGAN"])
    if data["KETT"].isnumeric():
        sentence += "({} bulan : {})".format(data["KETT"], data["BULANT"])
    else:
        sentence += "({})".format(data["KETT"], data["BULANT"])
    sentence += "\n"

    # 3. SPP
    sentence += "3. SPP : Rp {},- ".format(data["SPMP/SPP"])
    if data["SPMP/SPP"]=="0":
        sentence += "({})".format(data["KETS"])
    else :
        sentence += "({} bulan : {})". format(data["KETS"], data["BULANS"])
    sentence += "\n"

    # 4. LKS Semester 1
    sentence += "4. LKS Semester 1 : Rp {},-\n".format(data["LKS1"])
    # 5. LKS Semester 2
    sentence += "5. LKS Semester 2 : Rp {},-\n".format(data["LKS2"])

    # 6. DANA KESISWAAN
    sentence += "6. Dana Kesiswaan : Rp {},- ".format(data["DANA KESISWAAN"])
    if data["KETK"] != "":
        sentence += "({})".format(data["KETK"])
    sentence+="\n"

    sentence += "\nPembayaran dapat dilakukan dengan transfer ke rekening BXX 00-000-000-00 atas nama GURUGURUGURU atau langsung ke petugas di sekolah.\n\
Terima kasih atas perhatian bapak/ibu.\n\nWassalamualaikum wr wb."
    return sentence

filename="tagihan.csv"
fileout = "pesan.txt"
with open(filename) as f:
    csv_file = csv.DictReader(f)
    with open(fileout, "w") as fo:
        for data in csv_file:
            msg = generate_message(data)
            fo.write(msg)
            fo.write("\n\n-------------------\n\n")
        