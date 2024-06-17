import './App.css';
import NavBar from './components/Navbar/NavBar';
import Hero from './components/Hero/Hero';
import Skills from './components/Skills/Skillcard/Skills'
import WorkExperience from './components/Skills/Skillcard/WorkExperience/WorkExperience';
import ContactMe from './components/ContactMe/ContactMe';
import Footer from './components/Footer/Footer';
import Projects from './components/Projects';

function App() {
  return (
   <>
   <NavBar/>
   <div className='container'><Hero/>
   <Skills/>
   <WorkExperience/>
   <Projects/>

   <ContactMe/>
   
   
   </div>
   <Footer/>
   
   
   </>
  );
}

export default App;
