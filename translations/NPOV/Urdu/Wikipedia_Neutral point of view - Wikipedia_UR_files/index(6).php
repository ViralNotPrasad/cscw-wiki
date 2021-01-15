$(document).ready(function()
{
var HTML_CHAR_MAP = {
'<': '&lt;',
'>': '&gt;',
'&': '&amp;',
'"': '&quot;',
"'": '&#39;'
};
 
function escapeHtml (s) {
return s.replace(/[<>&"']/g, function (ch) {
return HTML_CHAR_MAP[ch];
});
}
	if(mw.config.get('wgUserNewMsgRevisionId') != null)
	{
		var orangeBarDiv = document.createElement("div");
		orangeBarDiv.innerHTML = 'آپ کے لیے کسی صارف کے جانب سے <a href="/wiki/User_talk:' + encodeURIComponent(wgUserName) + '" title="User talk:'+escapeHtml(wgUserName)+'">نیا پیغام ہے</a> (<a href="/w/index.php?title=User_talk:'+encodeURIComponent(wgUserName)+'&diff=cur&old='+wgUserNewMsgRevisionId+'">1 آخری تبدیلی</a>).';
		orangeBarDiv.className = "usermessage";
 
		if($("#contentSub").length == 0) //No #contentSub in CologneBlue, so handle it specially (possibly adding multiple orange bars but oh well)
		{
			$(".tagline").after(orangeBarDiv);
		}
		else //all other skins
		{
			$("#contentSub").after(orangeBarDiv);
		}
 
		//default styling, in case the CSS stylesheet fails to load (keeping the className the same allows for user customization)
		$(orangeBarDiv).css({"background-color": "#ffce7b","border": "1px solid #ffa500","color": "black","font-weight": "bold","margin": "2em 0 1em","padding": ".5em 1em","vertical-align": "middle"})
	}
});