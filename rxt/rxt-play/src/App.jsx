import './styles/index.css';
import Header from './components/Header';
import EmployeesPage from './pages/EmployeesPage';


export default function App() {

  return (
    <>
      <Header>
        <EmployeesPage />
      </Header>
    </>
  )
}
