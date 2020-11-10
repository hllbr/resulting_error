import scrapy


class GamersSpider(scrapy.Spider):
    name = "gamers"
    page_count = 0 
    gamer_count = 1
    file = open("gamers.txt","a",encoding="UTF-8")
    start_urls =[
        "https://www.leagueofgraphs.com/tr/rankings/summoners/page-1"
    ]
        

    def parse(self, response):
        gamers_name =response.css("div.txt span.name::text").extract()
        gamers_puan = response.css("div.leaguePoints i::text").extract()
        gamers_zafer = response.css("div.wins i::text").extract()
        i = 0 
        while( i<len(gamers_puan)):
            """yield{
                "name" : gamers_name[i],
                "paun" : gamers_puan[i],
                "zafer": gamers_zafer[i]
            }"""
            self.file.write("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*\n")
            self.file.write(str(self.gamer_count)+ "\n")
            self.file.write("GAMER NAME : "+gamers_name[i] +"\n")
            self.file.write("GAMER PUAN : "+gamers_puan[i] +"\n")
            self.file.write("GAMER ZAFER : "+gamers_zafer[i] +"\n")
            self.file.write("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*\n")
            self.gamer_count +=1 
            i += 1
      
            
      