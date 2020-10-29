



def create_outline():
    
    course_topics = set(["Introduction to Python", "Tools of the Trade", 
    "How to make decisions", "How to repeat code", "How to structure data",
    "Functions", "Modules"])
    course_topics = list(course_topics)
    course_topics.sort()

    print ("Course Topics:")
    for topics in course_topics:
        print("*",topics)
    
    def problems(s):
        return s+" : Problem 1, Problem 2, Problem 3"
    print("Problems: ")
    mapping = map(problems, course_topics)
    for map_list in mapping:
        print("*", map_list)
    
    status = ['[STARTED]', '[GRADED]', '[COMPLETED]']
    student_list = [('Nyari', 'Functions', 'Problem 1', status[0]), ('Nicholas', 'Modules', 'Problem 2', status[1]), ('Stranger', 'How to repeat code', 'Problem 3', status[2])]
    student_list.sort(reverse = True, key=lambda x:x[3])
    print("Student Progress:")
    count = 1
    for my_tuple in student_list:
        print(f"{count}. {my_tuple[0]} - {my_tuple[1]} - {my_tuple[2]} {my_tuple[3]}")
        count += 1
    
    
if __name__ == "__main__":
    create_outline()
