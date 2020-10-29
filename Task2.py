Read_FILE_NAME="book.txt"
Write_Mode="w"
Read_Mode="r"
Output_File='Summary.txt'
Alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open(Output_File,Write_Mode)as output:
    def summarize_letters(string):
        letters=[]
        counts=[]
        for letter in string.upper():
            if letter in Alphabets:
                if letter in letters:
                    index=letters.index(letter)
                    counts[index]+=1
                else:
                        letters.append(letter)
                        counts.append(1)
                        tuples=list(zip(letters,counts))
                        tuples.sort()
                        return tuples
                with open(Read_FILE_NAME,Read_Mode) as book:
                            data=book.read()
                            summary=summarize_letters(data)
                for char,count in summary:
                                output.write(f'{char}{count}\n')
                                all_letters=True
                if len(summary)== len(Alphabets):
                    for item in summary:
                        if item[0] not in Alphabets:
                                all_letters=False
                                break
                else:
                                all_letters=False
                if all_letters:
                                output.write('It has all letters. \n')
                else:
                                 output.write('It doesn"t have all letters. \n')



