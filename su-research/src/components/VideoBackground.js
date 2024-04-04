// Importing React to enable JSX syntax and component logic within this file.
import React from 'react';

// Defining a functional component named VideoBackground.
// This component will render a video that plays automatically, loops, and fills the entire background.
const VideoBackground = () => (
    // Using the <video> HTML tag to embed a video in the webpage.
    // The video has several attributes set for desired behavior:
    // - autoPlay: The video will start playing as soon as it is ready without user interaction.
    // - loop: Once the video reaches the end, it will loop back to the beginning and continue playing.
    // - muted: The video will be muted by default to avoid sudden audio playback.
    // - playsInline: Allows the video to play 'inline' on iOS devices, preventing automatic fullscreen.
    <video autoPlay loop muted playsInline 
           // Applying TailwindCSS classes for styling:
           // - fixed: Positioning the video in a fixed position.
           // - z-0: Setting the z-index to 0 to ensure it stays behind all other content.
           // - w-full: Making the video full width of its parent.
           // - h-full: Making the video full height of its parent.
           className="fixed z-0 w-full h-full"
           // Inline styles are used here for specific adjustments not covered by TailwindCSS:
           style={{
               objectFit: 'cover', // Ensures the video covers the full viewport without being stretched.
               objectPosition: 'center', // Centers the video within its element.
               width: '100vw', // Sets the width to 100% of the viewport width.
               height: '100vh', // Sets the height to 100% of the viewport height.
               top: 0, // Positions the top edge of the video at the top of the viewport.
               left: 0, // Positions the left edge of the video at the left of the viewport.
               filter: 'brightness(50%)' // Applies a filter to reduce the brightness of the video by 50%.
           }}>
      {/* The <source> tag is used to specify multiple media resources for the <video> element.
          Here, it specifies the path to the video file and its MIME type. */}
      <source src="/suVid.mp4" type="video/mp4" />
      {/* This text is displayed if the browser doesn't support the <video> tag. */}
      Your browser does not support the video tag.
    </video>
);

// Exporting the VideoBackground component to be used in other parts of the application.
export default VideoBackground;