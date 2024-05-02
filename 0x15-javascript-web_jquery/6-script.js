/**
 * updates the text of the <header> element to 'New Header!!!'
 *  when the user clicks on the tag
 */
$(document).ready(function () {
	$("DIV#update_header").click(function () {
		$("header").text("New Header!!!");
	});
});