import React, { Component } from 'react';
import './index.css';
import Icons from './Icons.js'

class EpisodeResult extends Component {
    render() {
        const value = this.props.value;
        return (
            <li className='episode'>
                <div className='info'>
                    <h6>Episode</h6>
                    <p>{value.episode_name}</p>
                </div>
                <div className='links'>
                    {/* TODO: add Icon function once links are added to database & API
                     <Icons value={value} /> */}
                </div>
            </li>
        )
    }
}

export default EpisodeResult