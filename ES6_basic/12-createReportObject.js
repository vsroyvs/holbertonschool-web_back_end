import createEmployeesObject from './11-createEmployeesObject';

export default function createReportObject(employeesList) {
  const object = {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList){
      return Object.keys(employeesList).length;
    }, 
  }
  return object;
}
