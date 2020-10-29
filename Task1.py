import os
Read_FILE_NAME="scores.txt"
Write_Mode="w"
Read_Mode="r"
Count_Student=0
Total_Score=0
score_list=[]
Write_File_Name='log.txt'
try:
  score=open(Read_FILE_NAME,Read_Mode)
  output=open(Write_File_Name,Write_Mode)
  with score,output:
    for line in score:
      name,score=line.split()
      try:
        score_list.append(int(score))
        Total_Score+=int(score)
      except ValueError as error:
          output.write(f'Bad score for {str(name)}, ignored.\n')
          print(f'Bad score for {str(name)}, ignored.\n')
      else:
            Count_Student+=1
            output.write(f'The class average is {int(Total_Score/Count_Student)} for {Count_Student} students')
            print(f'The class average is {int(Total_Score/Count_Student)} for {Count_Student} students')
except OSError as error:
  output.write(f'{Read_FILE_NAME} is not a valid file, error message:{error}\n')
  print(f'{Read_FILE_NAME} is not a valid file, error message:{error}\n')
except IOError as error:
  output.write(f'IOError, error message:{error}\n')