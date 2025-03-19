def make_list_of_files(n):
    files = ['file_0.txt','file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']
    for i in range(n):
        files.append("file_" + str(i) + ".txt")
        return files
    """
    make a lists of n file names with the format "file_0.txt"
    assume n greater than or equal to 1
    hint: use a loop and append
    """

print(make_list_of_files(5)) #['file_0.txt', 'file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']