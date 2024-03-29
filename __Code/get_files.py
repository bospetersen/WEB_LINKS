root_path = "https://raw.githubusercontent.com/bospetersen/WEB_LINKS/main"
urls = [
"https://raw.githubusercontent.com/bospetersen/WEB_LINKS/main/AI-Machinelearninng/hardware.md",
"https://raw.githubusercontent.com/bospetersen/WEB_LINKS/main/AI-Machinelearninng/machinelearning.md",
"https://raw.githubusercontent.com/bospetersen/WEB_LINKS/main/Communicating sharing work.md",
]

def make_select_name(root_path, url):
        select_path = url.split(root_path) 
        select_path = select_path[1][1:]
        select_path = select_path[:-3]
        return select_path


select_names = []
url_setup = []
for url in urls:
        name = make_select_name(root_path, url)
        select_names.append(name)
        url_setup.append({'name': name, "url": url})


print(select_names)
print(url_setup)


# urls = [{"name": 'Hardware', "url": url_001}, 
#         {"name": 'Communicating sharing work', "url": url_002}, 
#         {"name": 'Software/Machinelearning', "url": url_003}]
