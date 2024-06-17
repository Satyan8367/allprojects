import React, { useRef } from 'react';
import './project.css';
import projectCard from './projectCard';
import {WORK_EXPERIENCE} from '../../utils/data';
import Slider from 'react-slick';

function Project() {
  const sliderRef=useRef();
  const settings={
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow:2,
    slidesToScroll:1,
    arrows:false,
    responsive: [
      {
        breakpoint: 769,
        settings: {
          slidesToShow:1,
          slidesToScroll:1,
        },
      },
    ],
  };

  const sliderRight=()=>{
    sliderRef.current.slickNext();
  };

  const sliderLeft=()=>{
    sliderRef.current.slickPrev();
  };


  return (
    <section className="experience-container">
      <h5>Work Experience</h5>
      <div className="experience-content">
        <div className="arrow-right" onClick={sliderRight}>
          <span className='right'>{'<'}</span>
        </div>
        <div className="arrow-left" onClick={sliderLeft}>
          <span className='left'>{">"}</span>
        </div>

      <Slider ref={sliderRef} {...settings}>
        {
          WORK_EXPERIENCE.map((item)=>
          (
            <projectCard key={item.title} details={item}/>)
          )
          
        }
        </Slider>

      </div>
    </section>
   
  )
}

export default Project;
