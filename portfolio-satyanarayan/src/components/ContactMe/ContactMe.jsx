import React from 'react';
import './ContactMe.css'
import ContactInfoCard from './ContactInfoCard/ContactInfoCard';
import ContactForm from './ContactForm/ContactForm';
import mail from './gmail-logo-36.png';
import github from './github-logo-36.png';

function ContactMe() {
  return (
    <div className="contact-container" id='contact'>
        <h5>Contact Me</h5>
        <div className="contact-content">
            <div style={{flex:1}}>
                <ContactInfoCard
                iconUrl={mail}
                text='satyanarayanbairwa033@gmail.com'/>
                <ContactInfoCard
                iconUrl={github}
                text='https://github.com/Satyan8367'/>
            </div>
            <div style={{flex:1}}>
                <ContactForm/>
            
            </div>
        </div>

    </div>
    
  )
}

export default ContactMe
