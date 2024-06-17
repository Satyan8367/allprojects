import React, { useRef } from 'react';
import './ContactForm.css';
import emailjs from '@emailjs/browser';

function ContactForm() {
  const form = useRef();


  const sendEmail = (e) => {
    e.preventDefault();
    // console.log(e.target[0].value)
  

    emailjs
      .sendForm('service_p7f5fzc', 'template_kqgqlkh', form.current, {
        publicKey: 'LvZRy4tgNxbwnxuFw',
      })
      .then(
        () => {
          console.log('SUCCESS!');
        },
        (error) => {
          console.log('FAILED...', error.text);
        },
      );

      e.target[0].value='';
      e.target[1].value='';
      e.target[2].value='';
      e.target[3].value='';
      alert("Email is send successfully")
  };
  return (
    <div className="contact-form-container">
        <form action="/" ref={form} onSubmit={sendEmail}>
        <div className="name-container"> 
            <input type="text" name='firstname' placeholder='First Name' />
            <input type="text" name='lastname' placeholder='Last Name' />
        </div>
        <input type="text" name='email' placeholder='Email' />
        <textarea type="text" name="message" id="" cols="" rows="3"></textarea>
        <button type="submit" value="Send">SEND</button>
        </form>
    </div>
   
  )
}

export default ContactForm
