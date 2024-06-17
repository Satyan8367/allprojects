import React from 'react';
import './Projects.css';
import {PROJECTDATA} from "../utils/data";
import Project from './Project';


function Projects() {
  return (<>
  <div className="project-container">
    <div className="project-head">
        <h2>My Projects</h2>
    </div>
    <div className="project-body">
        {
            PROJECTDATA.map((item)=>(
                <Project key={item.id} details={item}/>
            ))
        }

        
    </div>

  </div>

  </>
    
  )
}

export default Projects