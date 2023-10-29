const getListStudentIds = (ids) => {
  if (!Array.isArray(ids)) {
    return [];
  }
  const arrayIds = ids.map((item) => item.id);

  return arrayIds;
};

export default getListStudentIds;
