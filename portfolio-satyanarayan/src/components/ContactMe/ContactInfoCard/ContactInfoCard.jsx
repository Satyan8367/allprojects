import React from 'react';
import './ContactInfoCard.css'

function ContactInfoCard({iconUrl,text}) {
  return (
    <div className="contact-details-card">
        <div className="icon">
            <img src={iconUrl} alt='contact'/>
        </div>
        <p>{text}</p>
    </div>
  )
}

export default ContactInfoCard
