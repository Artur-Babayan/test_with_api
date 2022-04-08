from flask import Flask, json



persons = [
			{"Dob": "01.01.2000", "name": "Arthur", "Last-name": "Babayan", "Gender": "Male"},
			{"Dob": "01.01.2001", "name": "Aram", "Last-name": "Xachatryan", "Gender": "Male"}, 
			{"Dob": "01.01.2002", "name": "Areg", "Last-name": "Badalyan", "Gender": "Male"}, 
			{"Dob": "01.01.2003", "name": "Arman", "Last-name": "Durunts", "Gender": "Male"}, 
			{"Dob": "01.01.2004", "name": "Ashot", "Last-name": "Babayan", "Gender": "Male"}, 
			{"Dob": "01.01.2005", "name": "Araqs", "Last-name": "Ohanyan", "Gender": "Female"}, 
			{"Dob": "01.01.2006", "name": "Arshaluys", "Last-name": "Gyagunts", "Gender": "Female"}, 
			{"Dob": "01.01.2007", "name": "Ashxen", "Last-name": "Durunts", "Gender": "Female"}, 
			{"Dob": "01.01.2008", "name": "Babken", "Last-name": "Xachatryan", "Gender": "Male"}, 
			{"Dob": "01.01.2009", "name": "Karen", "Last-name": "Durunts", "Gender": "Male"}, 
			{"Dob": "01.01.2010", "name": "Sarmen", "Last-name": "Manukyan", "Gender": "Male"}, 
			{"Dob": "01.01.2011", "name": "Suren", "Last-name": "Durunts", "Gender": "Male"}, 
			{"Dob": "01.01.2000", "name": "Sergey", "Last-name": "Manukyan", "Gender": "Male"}, 
			{"Dob": "01.01.2003", "name": "Vasya", "Last-name": "Manukyan", "Gender": "Male"}, 
			{"Dob": "01.01.2000", "name": "Davo", "Last-name": "Durunts", "Gender": "Male"}, 
			{"Dob": "01.01.2004", "name": "Tiko", "Last-name": "Manukyan", "Gender": "Male"}, 
			{"Dob": "01.01.2015", "name": "Narek", "Last-name": "Xachatryan", "Gender": "Male"}, 
			{"Dob": "01.01.1997", "name": "Vigen", "Last-name": "Manukyan", "Gender": "Male"}, 
			{"Dob": "01.01.1990", "name": "Edo", "Last-name": "Manukyan", "Gender": "Male"}, 
			{"Dob": "01.01.1994", "name": "manuk", "Last-name": "Xachatryan", "Gender": "Male"}]

api = Flask(__name__)

@api.route('/person', methods=['GET'])
def get_persons_info():
  return json.dumps(persons)

if __name__ == '__main__':
    api.run() 