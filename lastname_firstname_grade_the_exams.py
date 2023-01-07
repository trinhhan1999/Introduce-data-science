#TASK1:
fname = input("Enter a class file to grade: ")
fnametxt = fname + ".txt"
try:
    fhand = open(fnametxt)
    print('Successfully opened:', fnametxt)
except:
    print('File cannot be opened:', fnametxt)
    exit()

#TASK2:    
print('**** ANALYZING ****')
invalid = 0
valid = 0
valid_lines = []
id_student = []
for line in fhand:
    line = line.rstrip()
    split_line = line.split(",")
    count = 0
    N = 0
    invalid_line = 0
# tìm các dữ liệu bị sai format theo yêu cầu của đề bài
    for infor in split_line:
        if count == 0:
            if infor[0] != "N" or len(infor) != 9 or infor[1:].isnumeric() == False:
                print('Invalid line of data:', 'N# is invalid:',end ='\n')
                print( line)
                invalid += 1
                invalid_line += 1
        count += 1
            
    if count != 26:
        print('Invalid line of data:', 'does not contain exactly 26 values:',end ='\n')
        print( line)
        invalid += 1
        invalid_line += 1
            
    if invalid_line == 0:
        valid_lines.append(split_line)
        valid += 1
        id_student.append(split_line[0])
            
if invalid == 0:
    print("No errors found!")
    
print('**** REPORT ****')
print('Total valid lines of data:', valid)
print('Total invalid lines of data:', invalid)

#TASK3:
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answerkey = answer_key.split(",")
score_list = []

answer_cancel = []
answer_wrong = []
for id_answer in valid_lines:            
# Tính điểm cho các câu trả lời đúng, sai và bỏ trống            
    score = 0
    for i in range(len(id_answer)-1):
        if id_answer[i+1] == answerkey[i]:
            score += 4
        elif id_answer[i+1] == "":
            score += 0
            answer_cancel.append(i+1) # danh sách các câu hỏi mà các sinh viên bỏ trống
        elif id_answer[i+1] != answerkey[i]:
            score -= 1
            answer_wrong.append(i+1) # danh sách các câu hỏi mà các sinh viên làm sai
    score_list.append(score) 
    
# tìm số học sinh có điểm cao (>80)
sort_score = []
number_student_highscore = 0
for scores in score_list:
    if scores > 80:
        number_student_highscore += 1
    sort_score.append(scores)
sort_score.sort()
print("Total student of high scores:", number_student_highscore)

# Tìm các điểm số max, min, giá trị trung bình và điểm trung vị
sum_score = sum(score_list)
average = (sum_score/len(score_list))
print("Mean (average) score:", format(average,".2f"))
print("Highest score:", max(score_list))
print("Lowest score:", min(score_list))
print("Range of scores:", (max(score_list) - min(score_list)))

# Tìm điểm trung vị của học sinh
if len(score_list)%2 != 0:
    print("Median score:", sort_score[int(len(score_list)//2 + 1)])
else:
    median = (sort_score[int(len(score_list)/2-1)] + sort_score[int(len(score_list)//2)])/2
    print("Median score:", median)
    
# tìm câu hỏi, số lượng sinh viên và tỉ lệ bỏ trống câu hỏi
dict_cancel = {}
for i in answer_cancel:
    if i in dict_cancel:
        dict_cancel[i]+=1
    else:
        dict_cancel[i]=1 
        
itemMaxValue_cancel = max(dict_cancel.items(), key = lambda x: x[1])
listOfKeys_cancel = list()

# Lặp lại tất cả các mục trong từ điển để tìm các khóa có giá trị lớn nhất
for key, value in dict_cancel.items():
    if value == itemMaxValue_cancel[1]:
        listOfKeys_cancel.append(key)        

ratio_cancel = itemMaxValue_cancel[1]/valid
ratio_cancel = round(ratio_cancel, 1)
print('Question that most people skip:', end = " ")
for j in listOfKeys_cancel:
    print(j, "-", itemMaxValue_cancel[1], "-", ratio_cancel, end = ", ")

print()
#tìm câu hỏi, số lượng sinh viên và tỉ lệ trả lời sai   
dict_wrong = {}
for i in answer_wrong:
    if i in dict_wrong:
        dict_wrong[i] += 1
    else:
        dict_wrong[i] = 1 
        
itemMaxValue_wrong = max(dict_wrong.items(), key = lambda x: x[1])
listOfKeys_wrong = list()
# Lặp lại tất cả các mục trong từ điển để tìm các khóa có giá trị lớn nhất
for key, value in dict_wrong.items():
    if value == itemMaxValue_wrong[1]:
        listOfKeys_wrong.append(key)        
ratio_wrong = itemMaxValue_wrong[1]/valid
ratio_wrong = round(ratio_wrong, 2)
print('Question that most people answer incorrectly:', end = " ")
for j in listOfKeys_wrong:
    print(j, "-", itemMaxValue_wrong[1], "-", ratio_wrong, end = ", ")   
    
#TASK4:
# viết vào file txt điểm và mã số của sinh viên
final_score = fname + "_grades.txt"
scores_file = open(final_score, 'w')
for i in range(len(id_student)):
    file = (id_student[i] + "," + str(score_list[i])+'\n')
    scores_file.write(file)
    
scores_file.close()