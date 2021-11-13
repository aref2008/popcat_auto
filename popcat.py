try:
	from selenium import webdriver
except Exception as e:
	print('run "pip install -r req.txt"')

try:
	driver = webdriver.Edge("edge.exe")
	driver.get("https://popcat.click/")
	driver.execute_script('var rand_num = Math.random() * (100) + 650;const app=document.querySelector("#app").__vue__;function pop(){var rand_num = Math.random() * (100) + 650;for(var i=0;i<=rand_num;i++)setTimeout(()=>{document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}))},Math.random() * (5) + 5)}document.cookie="country=SY;expires=Sat, 24 FEB 2022 12:00:00 UTC;path=/",document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}));setInterval(()=>{pop()},30000);')
except Exception as e:
	print('chrome webdriver not valid, please download one that fit with your edge version!!')

try:
	driver = webdriver.Chrome("chrome.exe")
	driver.get("https://popcat.click/")
	driver.execute_script('const rand_num = Math.random() * (100) + 650;const app=document.querySelector("#app").__vue__;function pop(){for(var i=0;i<=rand_num;i++)setTimeout(()=>{document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}))},Math.random() * (5) + 5)}document.cookie="country=SY;expires=Sat, 24 FEB 2022 12:00:00 UTC;path=/",document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}));setInterval(()=>{pop()},30000);')
except Exception as e:
	print('chrome webdriver not exist, please download, move it to code folder with name chrome.exe and run code again')


try:
	driver = webdriver.Firefox("firefox.exe")
	driver.get("https://popcat.click/")
	driver.execute_script('const rand_num = Math.random() * (100) + 650;const app=document.querySelector("#app").__vue__;function pop(){for(var i=0;i<=rand_num;i++)setTimeout(()=>{document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}))},Math.random() * (5) + 5)}document.cookie="country=SY;expires=Sat, 24 FEB 2022 12:00:00 UTC;path=/",document.dispatchEvent(new KeyboardEvent("keydown",{key:"s",ctrlKey:!0}));setInterval(()=>{pop()},30000);')
except Exception as e:
	print('firefox webdriver not exist, please download, move it to code folder with name firefox.exe and run code again')
