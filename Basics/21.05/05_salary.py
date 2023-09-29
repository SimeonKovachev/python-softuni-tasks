FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

browser_tabs = int(input())
salary = int(input())

for number_tab in range(browser_tabs):
    website_name = input()

    if website_name == "Facebook":
        salary -= FACEBOOK_FINE
    elif website_name == "Instagram":
        salary -= INSTAGRAM_FINE
    elif website_name == "Reddit":
        salary -= REDDIT_FINE

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
