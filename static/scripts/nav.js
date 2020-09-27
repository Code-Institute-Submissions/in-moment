// Script that toggles dropdown menu items such as navigation and search window on mobile view.
$(() => {
    // Elements
    const navBtn = $("#nav-btn");
    const searchBtn = $("#search-btn");
    const navBar = $("#nav-bar");
    const searchBar = $("#search-bar");
    // Creating arrays of elements for ease of iteration.
    const btns = [navBtn, searchBtn];
    const bars = [navBar, searchBar];
    // Variables to track down which tab is open.
    let barOpen = false;
    let btnActive = false;
    let currentBar = null;
    let currentBtn = null;
    /* 
        Adding on click event to each button on action bar to trigger animation
        on assosiated tab.
        Making sure that only one tab is open at the time and hides previous one. 
    */
    for (let i = 0; i < btns.length; i++) {
        btns[i].click(() => {
            if (!barOpen) {
                bars[i].addClass("open-bar");
                btns[i].addClass("active-btn");
                barOpen = true;
                btnActive = true;
                currentBar = bars[i];
                currentBtn = btns[i];
            } else if (barOpen && currentBar !== bars[i]) {
                currentBar.removeClass("open-bar");
                currentBtn.removeClass("active-btn");
                bars[i].addClass("open-bar");
                btns[i].addClass("active-btn");
                currentBar = bars[i];
                currentBtn = btns[i];
            } else {
                bars[i].removeClass("open-bar");
                btns[i].removeClass("active-btn");
                barOpen = false;
                btnActive = false;
                currentBar = null;
                currentBtn = null;
            }
        });
    }
});