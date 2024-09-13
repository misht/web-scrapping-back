# Web Scrapping Back

WeCollaborate is a web application
designed to encourage collaboration between users in the academic and research
environment, facilitating the interaction and exchange of knowledge between both
experienced and novice researchers, thus promoting the creation of scientific
collaboration networks. 

Run the application:
- Install virtualenv: pip install virtualenv
- Create a virtual environment with Python 3.10: virtualenv -p python3 venv_name 
- Activate the virtual environment: source venv_name/bin/activate
- Install requirements: pip install -r requirements.txt
- Execute the command: python3 -m flask --debug run

Run the application with Docker:
- Install Docker Desktop for your operating system (Example windows): https://docs.docker.com/desktop/install/windows-install/ 
- Once, it has been successfully installed (You should be inside web-scrapping-back directory):
  - Execute the command: docker build --tag web-scrapping-back . 
  - Then, execute: docker run -p 5000:5000 web-scrapping-back