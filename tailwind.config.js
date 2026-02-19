/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*/templates/**/*.html',
    './**/forms.py',
    '!./node_modules',
    '!./.venv',
    "./static/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}