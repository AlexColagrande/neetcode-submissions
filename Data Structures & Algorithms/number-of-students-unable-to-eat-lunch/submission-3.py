class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = None
        n = 0
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                n = 0
            else:
                if stud == students[0]:
                    n += 1
                else:
                    stud = students[0]
                    n = 1
                if n == len(students):
                    return n
                students = students[1:] + [students[0]]
        return len(students)


        