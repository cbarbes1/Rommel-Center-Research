module.exports = {
  // The `content` property tells Tailwind where your application's content files are located.
  // This allows Tailwind to scan your files for class names to generate the necessary styles.
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // This pattern matches any file in the src directory with the extensions .js, .jsx, .ts, or .tsx
  ],
  // The `theme` property allows you to customize Tailwind's default styling to match your design.
  theme: {
    // The `extend` property allows you to add custom styles or override existing ones.
    extend: {
      // Customizing `boxShadow` to add our own shadows with specific blur and spread radius.
      boxShadow: {
        // `custom` is a custom shadow with a darker color for a more pronounced effect.
        // The values control the x-offset, y-offset, blur radius, spread radius, and color.
        custom: '0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -2px rgba(0, 0, 0, 0.5)',
        // `custom-medium` is a slightly lighter shadow for medium emphasis elements.
        'custom-medium': '0 5px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -4px rgba(0, 0, 0, 0.3)',
      },
      // Customizing `colors` to add our own color palette.
      colors: {
        // `suGray` is a custom gray color used for text or backgrounds.
        suGray: '#888a8d',
        // `suGold` is a custom color object with a default and a darker variant.
        suGold: {
          DEFAULT: '#FFC420', // The default shade of suGold.
          dark: '#B38600', // A darker variant of suGold for contrast or emphasis.
        },
        // `suMaroon` is another custom color object with a default and a darker variant.
        suMaroon: {
          DEFAULT: '#8A0000', // The default shade of suMaroon.
          dark: '#670000', // A darker variant of suMaroon for contrast or emphasis.
        },
      },
    },
  },
  // The `plugins` array allows you to add additional functionality or custom components to Tailwind.
  plugins: [], // Currently, no plugins are added.
}
