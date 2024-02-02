if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks.get(query_name)
    if marks:
        average = sum(marks) / len(marks)
        print(f"{average:.2f}")  # Format to display two decimal places
    else:
        print("Belirtilen öğrenci için herhangi bir not bulunamadı...")