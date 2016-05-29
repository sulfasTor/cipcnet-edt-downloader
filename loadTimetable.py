 # Copyright (C) 2016 sulfasTor                         
                                                                          
 #  This program is free software; you can redistribute it and/or modify    
 #  it under the terms of the GNU General Public License as published by    
 #  the Free Software Foundation; either version 3, or (at your option)     
 #  any later version.                                                      
                                                                          
 #  This program is distributed in the hope that it will be useful,         
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of          
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           
 #  GNU General Public License for more details.                            
                                                                          
 #  You should have received a copy of the GNU General Public License       
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.   

import os
import getpass
import mechanize

def getEDT(username, password, groupe, semaine):

    
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)
    url = 'https://login.insa-lyon.fr/cas/login?service=http%3A%2F%2Fcipcnet.insa-lyon.fr%2Flogin_form%3Fform.submitted%3D1%26cas_came_from%3D&submit=Log+in'
    browser.open(url)
    browser.select_form(nr = 0)     
    browser.form['username'] = username
    browser.form['password'] = password
    response = browser.submit()
    pdf = browser.retrieve('https://cipcnet.insa-lyon.fr/scol/php/edt_pdf?id_groupe='+groupe+'&id_semaine_pc='+semaine)[0]
    os.system( '/usr/bin/gnome-open ' + pdf)
        
    
   # for line in browser.open('https://cipcnet.insa-lyon.fr/scol/php/edt_pdf?id_groupe='):
       

   #      if re.search('<table class="edt">', line):
   #          founded = True
            
   #      if re.search("</table>", line):
   #          break

   #      if founded:
   #          reponse+=line;
def main():

    groupe = raw_input('groupe?\n')
    semaine = raw_input('semaine?\n')
    usr = raw_input('Username?\n')
    psw = getpass.getpass('Password?\n')
    getEDT(usr, psw, groupe, semaine)
    
    
if __name__ == '__main__':
    main()
