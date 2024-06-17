import React from 'react';
import './Hero.css';
import profile from '../satya-profile.png';
import reactlogo from '../react-logo-48.png'
import pythonlogo from '../python-logo-48.png'
import jslogo from '../javascript-logo-48.png'
import csslogo from '../css3-logo-48.png'


function Hero() {
  return (
    <>
    <section className='hero-container'>
        <div className="hero-content">
            <h2>FullStack Developer</h2>
            <p>Possinate Fullstack developer | Transforming Ideas Samless and visually Stunning web Solutions</p>
            <a id='resume' href="satyanarayan-resume.pdf" download>
            <button type="button">Download Resume</button></a>
        </div>
        <div className="hero-img">
            <div>
                <div className="tech-icon">
                {/* <box-icon className="icon-log" name='react' type='logo' rotate='90' animation='spin' color='#6852ba' ></box-icon> */}
                <img className='icon-log' src={reactlogo} alt="react" />
                </div>
                <img src={profile} alt="" />
            </div>
            <div className="tech-icons">
            <div className="tech-icon">
            <img className='icon-log' src={pythonlogo} alt="react" />
            </div>
            <div className="tech-icon">
            <img className='icon-log' src={jslogo} alt="react" />
            </div>
            <div className="tech-icon">
            <img className='icon-log' src={csslogo} alt="react" />
            </div>
            </div>
            

        </div>

    </section>
    </>
   
  )
}

export default Hero;
