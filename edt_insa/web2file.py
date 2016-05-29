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
import mechanize
import subprocess as sp

def getPage(url):
    
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)

    if url.find('http') < 0:
        url = 'https://'+url

    reponse = browser.open(url).read()
    cmd = sp.Popen('ls', stdout=sp.PIPE)
    result, error = cmd.communicate();
    
    if result.find('reponsefromweb4pdfscript.html'):
        del_cmd = 'rm reponsefromweb4pdfscript.html'
        sp.call(del_cmd.split())
    
    f = open('reponsefromweb4pdfscript.html','a')
    f.write(reponse)
    print f
    f.close()
    cmd = 'xdg-open reponsefromweb4pdfscript.html'
    sp.call(cmd.split())
    
    
def main():

   url = raw_input('Url?\n')
   getPage(url)
   
    
if __name__ == '__main__':
    main()
