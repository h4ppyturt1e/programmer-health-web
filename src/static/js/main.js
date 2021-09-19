var navbar = document.getElementById("navbar");

window.onscroll = function (ev) {

	// If you scroll atleast an 8th of the page height, the shadow appears on the navigation bar.
	if (window.scrollY >= 5) {
		navbar.style = `box-shadow: 0px 4px 13px 0px rgba(0, 0, 0, 0.26); -webkit-box-shadow: 0px 4px 13px 0px rgba(0, 0, 0, 0.26);
        -moz-box-shadow: 0px 4px 13px 0px rgba(0, 0, 0, 0.26);`;
	} else {
		navbar.style = `box-shadow: unset;`;
	}
}