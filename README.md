# popcat_auto
Automate boring clicks on https://popcat.click !! (using Edge, you can change webdriver by replace the current in the folder)

click numbers and wait period randomized to bypass any potential automation detection technique! 

<b>Python:</b><br>

<b>Follow these steps :</b><br>
1- Download source code.<br>
2- Install Python 3.9<br>
3- run "pip install -r req.txt"<br>
4- run "python popcat.py"<br>
5- If code not work visit [Edge web driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and download webdriver depend on your Edge version and replace it in folder!<br>





Click here to download [Chrome web driver](https://chromedriver.chromium.org/getting-started)<br>

Click here to download [Firefox web driver](https://github.com/mozilla/geckodriver/releases)<br>



<b>JavaScript:</b><br>
paste this code in your browser console :
<br>
```js
var rand_num = Math.random() * (100) + 650;const app=document.querySelector("#app").__vue__;function pop(){var rand_num = Math.random() * (100) + 650;for(var i=0;i<=rand_num;i++)setTimeout(()=>{document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}))},Math.random() * (5) + 5)}document.cookie="country=SY;expires=Sat, 24 FEB 2022 12:00:00 UTC;path=/",document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}));setInterval(()=>{pop()},30000);
```
<br>

<b>[Youtube video](https://youtu.be/kwuvcYNQYpI)</b><br>


Enjoy :)
