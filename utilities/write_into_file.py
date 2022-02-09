def write_into_file(all_records, names):
    f = open("all_transactions.txt", "w")
    for name in names:
        f.write(name + "\t")
    for record in all_records:
        f.write("\n")
        for y in record:
            f.write(str(y) + "\t")
    f.close()