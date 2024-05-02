/**
 * fetches from URL and displays the value
 * of 'hello' from that fetch in the HTML tag
 */
$(document).ready(function () {
	$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
		$("DIV#hello").text(data.hello);
	});
});