const getStudentIdsSum = (arrayStudents) => {
  const studentIdsSum = arrayStudents.reduce((accumulator, student) => accumulator + student.id, 0);
  return studentIdsSum;
};

export default getStudentIdsSum;
