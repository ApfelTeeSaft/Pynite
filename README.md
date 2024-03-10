# Pynite The first Fortnite backend written in python

# What does it have:

-Basic lobby loading

-More comming soon


# How to set up? 
First Install python from [Here](https://www.python.org/downloads/)
<br>
Second run install.py to install very important stuff :)
<br>
After that run python main.py in the dir to start the backend
<br> 
Then you have to redirect your build to your backend so run this Fiddler script:
<br>
`
import Fiddler;
class Handlers
{
    static function OnBeforeRequest(oSession: Session) {
        if (oSession.hostname.Contains("ol.epicgames.") ||            // Epic's Backend
            oSession.hostname.Contains("s3-us-west-1.amazonaws.com")) // waitingroom retry config
        {
            if (oSession.HTTPMethodIs("CONNECT"))
            {
                oSession["x-replywithtunnel"] = "ServerTunnel";
                return;
            }
            oSession.fullUrl = "http://127.0.0.1:8383/" + oSession.PathAndQuery
        }
    }
}`
<br>
After that Your done!! Enjoy!
#Ps: Made in one day, don't expect it to run flawlessly
