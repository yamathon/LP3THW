def web_scrape(how_many_sites, index_intensity):
    levels = int(input("Enter levels of internet to scan (1-6):: "))
    print("\nReady, hit ENTER to continue, CTRL-C to abort.")
    input()
    print(f"Scanning {how_many_sites}!!!")
    print(f"Scraping intensity: {index_intensity}.")
    
    objects_found = (levels * how_many_sites * 300000) / (index_intensity * 10)
    print(f"Objects found: {objects_found}!!")

hello, greetings = 29403294320, 2222
terrible, great = 1.1, 398993 + 3899


web_scrape(90, 10)
web_scrape(234+234, 8*3)
web_scrape(hello, greetings)
web_scrape(hello + 3, greetings + 23)
web_scrape(hello / greetings, hello / greetings)
web_scrape(greetings * hello ** 0, hello / (greetings**2))
web_scrape(terrible - hello, hello - 2 * hello)
web_scrape(2, 889)
userinput = int(input("Enter value1 for web_scrape:: "))
userinput2 = int(input("enter value2 for web_scrape:: "))
web_scrape(userinput, userinput2)
web_scrape(userinput * hello * greetings, 3344 / 23)