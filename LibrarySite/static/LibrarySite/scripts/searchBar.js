/**
 * Created by scott on 2016-01-28.
 */

window.onload = function()
{
	//Get submit button
	var submitbutton = document.getElementById("sb");
	//Add listener to submit button
	if(submitbutton.addEventListener)
    {
		submitbutton.addEventListener("click", function()
        {
			if (submitbutton.value == 'Search for a Book'){
				submitbutton.value = '';
			}
		}); // end addlistener
	}

}/**
 * Created by scott on 2016-03-16.
 */
