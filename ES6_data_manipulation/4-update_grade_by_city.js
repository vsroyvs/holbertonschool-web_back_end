const updateStudentGradeByCity = (arrayStudents, city, newGrades) => {
  if (!Array.isArray(arrayStudents) || !Array.isArray(newGrades)) {
    return [];
  }

  const studentByCity = arrayStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grades = newGrades.filter((grade) => student.id === grade.studentId);
      let grade = 'N/A';

      if (grades[0]) {
        grade = grades[0].grade;
      }

      return { ...student, grade };
    });

  return studentByCity;
};

export default updateStudentGradeByCity;
