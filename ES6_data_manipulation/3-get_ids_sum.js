const getStudentIdsSum = (arrayStudents) => {
  const studentIdsSum = arrayStudent.reduce(
    (accumulator, student) => {
      accumulator + student.id
    }, 0);
  return studentIdsSum
};

export default getStudentIdsSum;
