import React from 'react';
import './Projects.css';
import svasthkart from './svasthkart.jpeg';
import tictactoe from './tictactoe.jpeg';
import todolist from './todolist.jpeg';
import rps from './rps.jpeg';
import emp from "./emp.jpeg";
import ecom from './ecom.jpeg'




function Project({details}) {
  return (
    <div className="project-card">
            <div className="project-img">
              {/* <h1>{details.id}</h1> */}
              <img src={details.img} alt="project" />
                {/* <img src={ecom} alt="project" /> */}
            </div>
            <h4>Title : {details.name}</h4>
            <p>Description : {details.desc}</p>
            <p>Tech : {details.tech}</p>
            <div className="project-demo-code">
            <a href={details.demo} target='_blank'  rel="noopener noreferrer">Demo</a>
            <a href={details.code}>Source code</a>
            </div>
            

        </div>
  )
}

export default Project