import './styles/index.css';
import { useState } from 'react';
import avatar1 from './assets/01.jpg';
import avatar2 from './assets/02.jpg';
import avatar3 from './assets/03.jpg';
import avatar4 from './assets/04.jpg';
import avatar5 from './assets/05.jpg';
import Employee from './components/Employee';
// import { v4 as uuidv4 } from 'uuid';


export default function App() {
  const showEmployee = true;
  const [employees, setEmployees] = useState([
    { id: 1, name: 'Tivere', role: 'Jnr. Engineer', avatar: 'https://github.com/tivereidoro/assets/assets/105525310/df9377a9-8ee2-4e94-876f-93d3ddb1175e' },
    { id: 2, name: 'Osaretin', role: 'Intern', avatar: avatar1 },
    { id: 3, name: 'Caleb', role: 'Tester', avatar: avatar2 },
    { id: 4, name: 'Pneuma', role: 'Developer', avatar: avatar4 },
    { id: 5, name: 'Jake', role: 'Frontend Dev.', avatar: avatar3 },
    { id: 6, name: 'Nelly', role: 'P.M', avatar: avatar1 },
    { id: 7, name: 'Lyric', role: 'Intern', avatar: avatar2 },
    { id: 8, name: 'Jesse', role: 'Intern', avatar: avatar5 },
  ]);

  // Function for editing and updating
  // an employee's details.
  function updateEmployee(id, newName, newRole) {
    const updatedEmployees = employees.map((employee) => {
      if (id == employee.id) {

        // Update and return the new employee
        // if the id matches
        return { ...employee, name: newName, role: newRole }
      }

      return employee;
    });
    setEmployees(updatedEmployees);
  }

  return (
    <div className='App'>
      {showEmployee ?

        <div className='flex flex-wrap justify-center'>
          {employees.map(
            (employee) => {
              return (
                <Employee
                  name={employee.name}
                  role={employee.role}
                  avatar={employee.avatar}
                  key={employee.id}
                  id={employee.id}
                  update={updateEmployee}
                />
              )
            }
          )}
        </div>

        :

        <p>You need admin priviledges to see this page</p>
      }

    </div>
  )
}
