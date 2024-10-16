news = 'On a field in England, three robots have been given a mission: to find and zap weeds with electricity before planting seeds in the cleared soil.The robots — named Tom, Dick and Harry — were developed by Small Robot Company to rid land of unwanted weeds with minimal use of chemicals and heavy machinery.The startup has been working on its autonomous weed killers since 2017, and this April launched Tom, its first commercial robot which is now operational on three UK farms. The other robots are still in the prototype stage, undergoing testing.Small Robot says robot Tom can scan 20 hectares (49 acres) a day, collecting data which is then used by Dick, a “crop-care” robot, to zap weeds. Then it’s robot Harry’s turn to plant seeds in the weed-free soil.Using the full system, once it is up and running, farmers could reduce costs by 40% and chemical usage by up to 95%, the company says.According to the UN Food and Agriculture Organization six million metric tons of pesticides were traded globally in 2018, valued at $38 billion.“Our system allows farmers to wean their depleted, damaged soils off a diet of chemicals,” says Ben Scott-Robinson, Small Robot’s co-founder and CEO.'

split_news = news.split(' ')
# print(split_news)
res = {}
for word in split_news:
    if word in res:
        res[word] += 1
    else:
        res[word] = 1
print(res) # print every word frequency
print("robots 共出現 " + str(res['robots']) + " 次\nweeds 共出現 " + str(res['weeds']) + " 次") # print robots & weeds frequency