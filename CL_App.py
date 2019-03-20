import click
import requests

# the apikey from newsapi.org
API_KEY = '133011acc65c42569875c0252ae5310d​'

@click.group()
def main():
        """
        N is a news application which offers a list of 4 news sources. From these four sources,a choice of a preferred source is made and it's from that choice where a list of the top 10 headlines is got,
        The news headline has a title, description and a url in case the user needs to follow up on the news story
        The user should also have have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
    main_url = " https://newsapi.org/v2/sources?apiKey=133011acc65c42569875c0252ae5310d"
    
# fetching data in json format 
open_source = requests.get(main_url).json() 

source = open_source["sources"] 

results = [] 

for k in source: 
    results.append(k["id"])


for w in results[0:4]:
    print(w)	


@main.command()
def topheadlines():
          """ Please enter your choice from the listsources """
newsSource = click.prompt("Please enter your choice from listsources")

main_url = "https://newsapi.org/v2/top-headlines?apiKey=133011acc65c42569875c0252ae5310d="+newsSource

# fetching data in json format 
open_headline = requests.get(main_url).json() 

headline = open_headline["articles"] 



output = [] 

for h in headline: 
    click.echo('\n')
    click.secho(click.style('TITLE: ' + h['title'], fg='red'))
    click.secho(click.wrap_text(h['description']))
    click.secho(click.style('DOMAIN: ' + h['url'], fg='blue'))

for i in output[:11]:
                print(i)


if __name__ == '__main__':
	main() 
