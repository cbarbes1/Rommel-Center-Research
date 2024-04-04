// Importing React library to use JSX syntax for defining UI components.
import React from 'react';

// Defining a functional component named VideoBackground.
// This component is responsible for rendering a video background on the webpage.
const VideoBackground = () => (
    // Using the <video> HTML element to embed a video in the webpage.
    // The video is configured to play automatically, loop indefinitely, be muted, and play inline.
    <video autoPlay loop muted playsInline 
           // Applying TailwindCSS utility classes for styling:
           // - fixed: Position the video in a fixed position on the screen.
           // - z-0: Set the z-index to 0 to ensure it's behind other content.
           // - w-full: Make the video full width of its parent container.
           // - h-full: Make the video full height of its parent container.
           className="fixed z-0 w-full h-full"
           // Inline styles for further customization:
           style={{
               objectFit: 'cover', // Ensures the video covers the available space without distortion.
               objectPosition: 'center', // Centers the video within its container.
               width: '100vw', // Sets the width to 100% of the viewport width.
               height: '100vh', // Sets the height to 100% of the viewport height.
               top: 0, // Positions the top edge of the video at the top of the viewport.
               left: 0, // Positions the left edge of the video at the left of the viewport.
               filter: 'brightness(70%)' // Applies a filter to reduce the brightness of the video.
           }}>
      {/* The <source> element specifies the path to the video file and its MIME type. */}
      <source src="/suVid.mp4" type="video/mp4" />
      {/* Fallback text displayed if the browser does not support the <video> element. */}
      Your browser does not support the video tag.
    </video>
);

// Exporting the VideoBackground component to make it available for use in other parts of the application.
export default VideoBackground;