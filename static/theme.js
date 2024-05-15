function setTheme(theme) {
    document.cookie = `theme=${theme}; path=/; expires=Fri, 31 Dec 9999 23:59:59 GMT`;
    applyTheme(theme);
    applyThemeToImage();
}
  
function toggleTheme(event) {
    const currentTheme = getTheme();
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
}