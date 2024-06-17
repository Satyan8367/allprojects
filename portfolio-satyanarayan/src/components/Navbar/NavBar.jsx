import React, { useState } from 'react';
import './NavBar.css';
import 'boxicons';
import MobileNav from './MobileNav';

function NavBar() {
    let menulogo='#fff';
    const [openMenu,setOpenMenu]=useState(false);
    const toggleMenu=()=>{
        setOpenMenu(!openMenu);
    }
  return (
    <>
    <MobileNav isOpen={openMenu} toggleMenu={toggleMenu}/>
    <nav className="nav-wrapper">
        <div className="nav-content">
            {/* <img className="logo" src={logo} alt="logo" /> */}
            <span className='logo'>Coder</span>
            <ul>
                <li> 
                    <a className="menu-item" href="./">Home</a>
                </li>
                <li> 
                    <a className="menu-item" href="#skills">Skills</a>
                </li>
                <li> 
                    <a className="menu-item" href="#workexperience">Work Experience</a>
                </li>
                <li> 
                    <a className="menu-item" href="#contact">Contact</a>
                </li>

                <button className='contact-btn' onClick={()=>{}}>Hire Me</button>
            </ul>

            <button className='menu-btn' onClick={toggleMenu}>
                <span style={{fontSize:'1.8rem'}}>
                {openMenu ? <box-icon name='x' animation='tada' rotate='90' color={menulogo} onMouseEnter={()=>{menulogo='#a993fe'}} onMouseLeave={()=>{menulogo='#fff'}} ></box-icon> : <box-icon name='menu' flip='horizontal' animation='tada' color={menulogo} onMouseEnter={()=>{menulogo='#a993fe'}} onMouseLeave={()=>{menulogo='#fff'}} ></box-icon>}
                </span>
            </button>
        </div>
    </nav>
      
    </>
  )
}

export default NavBar
