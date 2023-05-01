The full thesis can be found in the thesis/ folder.

II. Data and Methodology
2.1 Dataset

This study used a Twitter dataset containing all of the geotagged tweets from October 26, 2017 to today. Geotagging is a feature that allows users to attach geographical location information to their tweets. The dataset contains one zip file per day, each of which contains all of the information that Twitter has about every geotagged tweet from that day. Since the dataset does not have information for every day in 2017 or 2023, the study excluded those years. As such, the study only used data from January 1, 2018 to December 31, 2022.
2.2 Data Limitations

	The dataset used in this study has a few limitations. The first limitation is that the data only includes geotagged tweets. Geotagged tweets only represent about 2% of total tweets. Using all tweets would more accurately assess the effectiveness of using Twitter to identify trends in the conversation about electric vehicles. Another limitation of the data is that there is missing data from September 6, 2022 to December 31, 2022. This underestimates the growth of the electric vehicle conversation on Twitter in 2022. Another limitation of the data is that it only reflects countries that have country codes on Twitter. This mostly excludes very small countries that would not have meaningful results anyways. However, Twitter is banned in China, which leads the global electric vehicle market, but is not in any of the results. The model has one limitation, which is that it only extracted hashtags in English, so the model favors English-speaking countries.
2.3 Data Processing

	This study used MapReduce to extract the desired information from the Twitter dataset. MapReduce is an efficient procedure for large scale parallel processing used for a wide range of applications. The procedure consists of three main phases: the Partition phase, the Map phase, and the Reduce phase. The partition phase was not required for this study because the Twitter dataset was already divided into one file per day.
The src/map.py file accomplished the map phase. To achieve desirable insights, two pieces of information were needed from each tweet in the dataset. One of these pieces was the hashtags that were used in the tweet, and the other piece was the country code associated with the tweet. The src/map.py file contains a list called “hashtag” that has 54 hashtags. There are a few reasons why these hashtags were chosen. Some of them were chosen because they are commonly used hashtags in social media posts related to electric vehicles, others were chosen to provide insight into a specific area of electric vehicle adoption, and some were chosen for data exploration purposes and because they had the potential to provide interesting results. The hashtags were divided into four categories: Electric Vehicle Adoption Generally, Electric Vehicle Companies, Electric Vehicle Technologies, and Electric Vehicle Policies. Of all of the 54 hashtags, 14 were related to electric vehicles generally, 22 were related to electric vehicle companies, 12 were related to electric vehicle technologies, and 6 were related to electric vehicle policies.


hashtags = [
# General
   '#evs',
   '#electricvehicles',
   '#evcharging',
   '#evadoption',
   '#evrevolution',
   '#greentransportation',
   '#cleantransportation',
   '#electricvehiclecharging',
   '#electricvehicleadoption',
   '#sustainabletransport',
   '#sustainabletransportation',
   '#zeroemissions',
   '#electriccar',
   '#electriccars',
# Companies
   '#tesla',
   '#lucidmotors',
   '#zoox',
   '#aptiv',
   '#nio',
   '#volvoev',
   '#byd',
   '#canoo',
   '#electriccarstartup',
   '#rivian',
   '#nissanleaf',
   '#nissanev',
   '#chevybolt',
   '#chevyev',
   '#fordmustangmache',
   '#fordev',
   '#bmwi3',
   '#kianiroev',
   '#vwid4',
   '#audietron',
   '#hyundaikonaev',
  '#electricvehicleindustry',
# Technologies
   '#electricvehicletechnology',
   '#evtechnology',
   '#evtech',
   '#electricvehicletech',
   '#batterytechnology',
   '#chargingtechnology',
   '#selfdrivingcars',
   '#regenerativebraking',
   '#vehicletogrid',
   '#batterytech',
   '#chargingtech',
   '#autonomousvehicles',
# Policies
   '#evpolicy',
   '#evtaxcredits',
   '#evincentives',
   '#transportationpolicy',
   '#evtaxexemptions',
   '#evtaxdeductions',
   ]


The src/map.py file opened every zip file and searched the contents of every tweet from that day. It extracted the country code from each tweet, but only extracted hashtags that matched one of the hashtags in the “hashtag” list. For every file, src/map.py summed the number of tweets that contained each hashtag for each country code. The resulting data was organized in a dictionary in a new file, which was added to the resulting outputs/ folder.
The reduce.py file accomplished the reduce phase. It looped through every file in the outputs/ folder and combined all of the information into a single dictionary, summing all of the hashtag count values by country, and adding this dictionary to the resulting reduced.country file. 
2.4 Model Construction

All of the Python files used in this study were added to the src/ folder. The countriesYearly.py file was used to produce the results. This file used Python’s matplotlib library to produce plots, which displayed how different countries used a certain hashtag over time. The countriesYearly.py file used all of the files in the outputs/ folder, the reduced.country file, and the visualize.py file to build the model. The visualize.py file sorted the total usage levels for a given hashtag in the reduced.country file. It then sorted for the five countries who tweeted that hashtag the most in the five-year timeframe. Then, the visualize.py file plotted the top five countries and their usage levels of the hashtag on a bar plot. These plots were added to the plots/barpots/ folder. The countriesYearly.py file used the visualize.py file to add the top five countries for a given hashtag to a list. The model only used the top five countries to produce results. The countriesYearly.py file was based on the countriesDaily.py file, which was also used to create the countriesWeekly.py and countriesMonthly.py files. After the countriesYearly.py file reduced the model’s scope to the top five countries for the hashtag, it looped through all of the files in the outputs/ folder and added their contents to a single dictionary. The keys of the new dictionary were the filenames from the outputs/ folder, which were dates, and the values were the dictionaries of information from each file. Then, the code extracted the dates from the filename keys and replaced them with date keys. The next step in getting the model prepared to plot was filtering the dictionary for the desired hashtag. This reduced the model to only include information for a single hashtag. The code then looped through the model keys and added the last date of each year to an array for the plot’s x-axis values. It then created the empty figure for the plot. To get the plot’s y-axis values, the code looped through the dictionary and for each country, it summed the values for each year and added them to an array for the y-axis values. It then plotted the x-axis values and y-axis values for each year over time. This produced the plots in the plots/lineplots/yearly/ folder, which were used for the results. Similar code was used to produce the other three folders in the plots/lineplots/ folder. The code only differs in the timeframe for which the data is aggregated. The countriesYearly.py file was used to produce the final results because it best identified electric vehicle adoption trends over time.
III. Results
3.1 Model Results

There were eight hashtags used for the results. Four of the plots were in the Electric Vehicle Adoption Generally category, two of them were in the Electric Vehicle Companies category, and two of them were in the Electric Vehicle Technologies category. None of the hashtags analyzed in the final results were from the Electric Vehicle Policies category because there were such low usage levels for those hashtags that it was difficult to confidently identify interesting trends. Australia (AU), Bangladesh (BD), Canada (CA), Germany (DE), Great Britain (GB),  India (IN), Ireland (IE), Japan (JP), Netherlands (NL), Spain (ES), and the United States (US) were the 11 countries that made it into the results.
This study found that the global conversations around electric vehicles and electric vehicle charging are trending upward and that the conversations around autonomous vehicles and self-driving cars are trending downward. Additionally, it found that the United States, Great Britain, India, and Canada are leading the conversation about electric vehicles on Twitter. When comparing hashtag levels across countries, it is important to consider that the model was limited to hashtags in English, so it favored English-speaking countries like the United States, Great Britain, and Canada.

Figure 3.1: #zeroemissionsYearly

![#zeroemissionsYearly](https://github.com/samchotzen/senior-thesis/blob/main/plots/lineplots/yearly/%23zeroemissionsYearly.png)

The #zeroemissionsYearly plot represented the only hashtag in the results that relates to electric vehicles as well as emissions more broadly. It illustrates that the United States was talking about zero emissions the most in 2018, but saw a steep decline in tweets containing the hashtag in 2020. This presents a slightly downward trend in the conversation about zero emissions on Twitter. In 2020, the COVID-19 pandemic disrupted the global economy and distracted the world from other issues like climate change. However, every country faced similar circumstances during 2020, and not all of the countries saw a downward trend. Spain was affected by COVID-19 and still experienced an increase in the zero emissions conversation in 2020.

Figure 3.2: #electriccarYearly

The #electriccarYearly plot is one of two plots where the United States does not have the highest total usage. Great Britain's usage of the hashtag skyrocketed in 2022. Conversely, The other four countries were talking about electric cars at a declining rate.

Figure 3.3: #electricvehiclesYearly

The #electricvehiclesYearly plot is the most evenly distributed of all of the results. Four of the countries trended upwards and all increased their usage in 2019, but then decreased their usage in 2020. Ireland deviated from this trend and experienced its peak usage in 2020, where it almost surpassed India. In four of the five years, Ireland saw the lowest usage level. The United States and India are the only two countries that increased the conversation about electric vehicles in 2022. It is also interesting to see that despite Great Britain’s surge in #electriccar usage in 2022, it saw a decline in its usage of #electricvehicles.


Figure 3.4: #evchargingYearly

The #evchargingYearly plot illustrated generally positive trends, with the exception of the United States experiencing a lower usage level in 2022 than 2021. As mentioned previously, about a quarter of the 2022 data is not included in the results, so declines in 2022 cannot provide meaningful results. Contrarily, increases in 2022 offer more powerful results. Electric vehicle charging is trending upwards on Twitter. This is unsurprising because a lack of charging infrastructure is one of the biggest barriers to electric vehicle penetration. Over time, charging infrastructure has not kept up with the technological advancements in the electric vehicle space or the increase in consumer demand.

Figure 3.5: #teslaYearly

The #teslaYearly plot had the highest usage levels of all the hashtags. The United States had much higher values than other countries, which makes sense considering Tesla is based in the United States. Tesla had already received so much attention before 2018, which might explain why there is not a clear trend in the data.





Figure 3.6: #nissanleafYearly

The #nissanleafYearly plot is the second of two plots where the United States does not have the highest total usage. It is also the only plot where Japan appears in the results. Japan has the most usage, which makes sense because Nissan is a Japanese company. This plot illustrates that while the other four countries all saw negative trends, usage in Japan increased over time.

Figure 3.7: #autonomousvehiclesYearly

The #autonomousvehiclesYearly and #selfdrivingcarsYearly hashtags were the two hashtags that were most closely related to technology, and the two hashtags have closely related meanings. Autonomous vehicles is a broader term that encompasses self-driving cars as well as other self-driving vehicles. This plot illustrated that while the United States was far more interested in autonomous vehicles than other countries in 2018, its interest waned over time. This study found that in 2022, the United States was only fractionally more interested in autonomous vehicle technology than Germany, Great Britain, India, and Canada, but it is also clear that all of these countries have experienced a declining interest in this conversation over time.

Figure 3.8: #selfdrivingcarsYearly

The #selfdrivingcarsYearly plot illustrated the same downward trend as the #autonomousvehiclesYearly plot shown above. The only differences were that in the #selfdrivingcarsYearly plot, Germany had higher usage than Great Britain and India had higher usage than Canada.
3.2 Insights and Outlook

Electric vehicle adoption is an important step in reducing global greenhouse gas emissions. Achieving high electric vehicle penetration rates requires expanding the conversation about electric vehicles. Figure 3.1 shows that the conversation about zero emissions is not expanding. However, the window for reaching net-zero emissions in the road transport sector by 2050 is closing quickly, and countries still have a lot of work to do to stay on track for achieving this goal. This shows that the conversation on Twitter is failing to adequately address the importance and urgency of the problem today. As seen in Figure 3.4, countries are talking more about electric vehicle charging now more than before. Improving charging station infrastructure is a necessary step in the future of electric vehicle adoption. Home charging will lead this development over the next decade, along with more public charging stations and more electric truck and electric bus charging stations. Between today and 2040, investment in charging infrastructure will need to exceed $1 trillion to achieve net-zero emissions globally.
It is interesting that the usage level of #electriccar saw downward trends in most countries, while #electricvehicle is being tweeted about more. According to Bloomberg New Energy Finance, while electric cars need to take over the car market, the more important conversation is around heavier vehicles becoming electric, like trucks, buses, and other public transportation systems. This change seems to be reflected in the trends on Twitter.
In the next few decades, one of the longer-term goals in the electric vehicle space will be autonomous vehicles, which will reshape automotive and freight markets around the world. Surprisingly, the results of this study show a decline in the global conversation about autonomous vehicles. This means that the conversation on Twitter is not addressing the importance of this space.


IV. Conclusion

 This study attempts to discover trends in the global conversation of the electric vehicle space. To do so, this study examines twitter data to explore how different countries are fitting into the conversation.
This study used MapReduce to process the data in the Twitter dataset, and then utilized Python’s matplotlib library to produce plots. These plots illustrated trends in how countries were talking about different areas of the electric vehicle industry between 2018-2022. This study concludes that the global conversations on Twitter around electric vehicles generally and electric vehicle charging are experiencing upward trends, while the conversations around autonomous vehicles and self-driving cars are declining.
	The results reflect where in the electric vehicle space different countries are focusing for the future. Electric vehicle charging is an important factor for promoting electric vehicle adoption, so it is promising to see that countries are talking about it. Additionally, autonomous vehicles are a longer-term goal in the electric vehicle industry, so it is unsurprising that it has not been the most popular conversation in the past few years, as there are more urgent and easily attainable goals.
	Further research can be done to continue analyzing the global conversation about electric vehicles. Using data from other social media platforms could help expand the results and more accurately identify trends in how countries are engaging with the electric vehicle conversation.
