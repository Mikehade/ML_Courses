# student1_score1 = 75
# student1_score2 = 80

# student2_score1 = 79
# student2_score2 = 82

def add_scores(score1, score2): #defining a functon or functio definition
    total = score1 + score2
    print(f"Total in function: {total}")

    return total

def avergae_scores(score1, score2): #defining a functon or functio definition
    unit1 = 2
    unit2 = 3
    avg = ((score1 * unit1) + (score2 * unit2)) / 2
    print(f"Average in function: {avg}")

    return avg



student1_score1 = int(input("What is score 1 for student 1:  "))
student1_score2 = int(input("What is score 2 for student 1:  "))

total_score1 = add_scores(student1_score1, student1_score2) #calling a function
print(f"Total 1: {total_score1}")

average_score1 = avergae_scores(student1_score1, student1_score2)
print(f"Avergae: {average_score1}")


student2_score1 = int(input("What is score 1 for student 2:  "))
student2_score2 = int(input("What is score 2 for student 2:  "))
total_score2 = add_scores(student2_score1, student2_score2)
print(f"Total 2: {total_score2}")


average_score2 = avergae_scores(student2_score1, student2_score2)
print(f"Avergae: {average_score2}")