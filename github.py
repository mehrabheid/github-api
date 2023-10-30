import requests
from json import loads
from time import sleep


#create object for our requests
class paramsGIT:
    def __init__(self):
        token='your-github-api-token'
        authHeaders={'Authorization': 'token %s' % token}
        self.requ=requests.Session()
        self.requ.headers=authHeaders


def github_api(search_in_github):
    
    myRequest=paramsGIT().requ
    searchQuery=search_in_github
    pages_back= 37
    
    for page in range(1,pages_back):

        # search your word in all github repositories
        searchAPI=f"https://api.github.com/search/repositories?q={searchQuery}&page={page}"
        
        #send request with valid headers
        github_searchAPI_requ=myRequest.get(searchAPI)
        sleep(4.2)
        if github_searchAPI_requ.status_code!=200:

            #you should update your token
            logs= str(github_searchAPI_requ.status_code)+': your token is expired set a new one'
            print(logs)
            break

        github_searchAPI_json:dict=loads(github_searchAPI_requ.text)
        github_searchAPI_json_items=github_searchAPI_json.get('items')
        if not github_searchAPI_json_items:
            logs= 'json error, call provider'#need to check name in --> github_searchAPI_json.get('items')
            print(logs)
            break

        for item in github_searchAPI_json_items:
            sleep(4.5)

             
            fullName=item.get('full_name')#get fullname
            repo_Link=item.get('html_url')#get repository URL
            title=item.get('description')#get description as title 
            owner_details=item.get('owner')#get owner details
            author=owner_details.get('login')#get author
            dateCreated=item.get('created_at')#get date created
            if not title:
                title=item.get('name')#get name as title if description == null
 
            # get readme.md  
            readmeAPI=f"https://raw.githubusercontent.com/{fullName}/master/README.md"
            readmeAPI_requ=myRequest.get(readmeAPI)   
            readmeAPI_text=readmeAPI_requ.text


            # add your codes here to print,save as file or insert into database



github_api()
