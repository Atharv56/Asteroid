import { Parallax } from 'react-parallax';
import './image.css'
import Ast1 from '../images/asteroid1.jpg'
const Image2 = () => (
    <Parallax className='image' bgImage= {Ast1} strength={800}>
        <div className= "content">
            <span className='img-text'>Mini Planets</span>
        </div>
    </Parallax>
);

export default Image2;