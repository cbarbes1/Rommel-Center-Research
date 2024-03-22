import React from 'react';

const VideoBackground = () => (
    <video autoPlay loop muted playsInline 
           className="fixed z-0 w-full h-full"
           style={{
               objectFit: 'cover', // Ensure the video covers the full viewport
               objectPosition: 'center', // Center the video
               width: '100vw', // Viewport width
               height: '100vh', // Viewport height
               top: 0,
               left: 0,
               filter: 'brightness(70%)'
           }}>
      <source src="/suVid.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
);

export default VideoBackground;