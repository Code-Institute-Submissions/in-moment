$(() => {
    const navBtn = $("#nav-btn");
    const searchBtn = $("#search-btn");
    const filterBtn = $("#filter-btn");
    const navBar = $("#nav-bar");
    const searchBar = $("#search-bar");
    const filterBar = $("#filter-bar");

    const btns = [navBtn, searchBtn, filterBtn];
    const bars = [navBar, searchBar, filterBar];

    let barOpen = false;
    let btnActive = false;
    let currentBar = null;
    let currentBtn = null;

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