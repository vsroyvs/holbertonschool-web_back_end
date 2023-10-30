const getStudentsByLocation = (arrayStudents, city) => {
  const filterStudentByLocation = arrayStudents.filter(
    (arrayStudents) => arrayStudents.location === city,
  );

  return filterStudentByLocation;
};

export default getStudentsByLocation;
