# -*- coding: utf-8 -*-
import xbmc, xbmcgui, urllib, re, xbmcplugin, datetime, random, os, json, urlparse
from resources.lib import client, control

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
artPath = control.artPath()

def main_folders():
    addDir('TV2', 'http://tv2.hu', 1, os.path.join(artPath, 'tv2.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('TV2 Klasszikusok', 'http://tv2.hu/tv2klasszikusok/', 2, os.path.join(artPath, 'tv2class.jpg'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('SuperTV2', 'https://tv2.hu/supertv2', 3, os.path.join(artPath, 'supertv2.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('FEM3', 'http://fem3.hu', 19, os.path.join(artPath, 'fem3.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('Mozi+', 'https://tv2.hu/moziplusztv/', 4, os.path.join(artPath, 'moziplusz.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('Izaura TV', 'http://izauratv.hu', 5, os.path.join(artPath, 'izauratv.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('Prime', 'http://tv2csoport.hu/prime/videok/oldal', 13, os.path.join(artPath, 'prime.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Lichi TV', 'https://tv2.hu/lichitv/videok/oldal', 14, os.path.join(artPath, 'lichitv.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Kiwi TV', 'https://tv2.hu/kiwitv/videok/oldal', 15, os.path.join(artPath, 'kiwitv.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Zenebutik', 'https://tv2.hu/zenebutik/videok/oldal', 17, os.path.join(artPath, 'zenebutik.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Humor+', 'http://humorplusz.hu/videok/oldal', 18, os.path.join(artPath, 'humorplusz.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Jocky TV', 'http://jockytv.hu', 22, os.path.join(artPath, 'jockytv.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Moziverzum', 'https://tv2.hu/moziverzum/filmek/oldal', 16, os.path.join(artPath, 'moziverzum.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Tények', 'https://tenyek.hu', 21, os.path.join(artPath, 'tenyek.jpg'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    return

def musor_listaTV2():  #TV2
    addDir('[COLOR orange]''Teljes filmek''[/COLOR]', url + '/musoraink/teljes_filmek/oldal', 24, os.path.join(artPath, 'movie.png'), fanart, '', '1')
    addDir('[COLOR orange]''Videók''[/COLOR]', url + '/videok/oldal', 25, os.path.join(artPath, 'video.png'), fanart, '', '1')
    r = client.request(url + '/videok/')
    m = re.compile('value="([0-9]+)" > (.+?) </').findall(r)
    for musor_id, musor_cim in m:
        try: name = client.replaceHTMLCodes(musor_cim.decode('utf-8'))
        except: name = musor_cim
        addDir(name.encode('utf-8'), url, 7, iconimage, fanart, musor_id, '1')

def musor_lista_sTV2(): #SuperTv2
    addDir('[COLOR orange]''Teljes filmek''[/COLOR]', url + '/musoraink/teljes_filmek/oldal', 26, os.path.join(artPath, 'movie.png'), fanart, '', '1')
    addDir('[COLOR orange]''Videók''[/COLOR]', url + '/videok/oldal', 27, os.path.join(artPath, 'video.png'), fanart, '', '1')
    r = client.request(url + '/videok/')
    m = re.compile('value="([0-9]+)" > (.+?) </').findall(r)
    for musor_id, musor_cim in m:
        try: name = client.replaceHTMLCodes(musor_cim.decode('utf-8'))
        except: name = musor_cim
        addDir(name.encode('utf-8'), url, 9, iconimage, fanart, musor_id, '1')

def musor_lista_fem3():
    r = client.request(url + '/videok/')
    m = re.compile('value="([0-9]+)" > (.+?) </').findall(r)
    for musor_id, musor_cim in m:
        try: name = client.replaceHTMLCodes(musor_cim.decode('utf-8'))
        except: name = musor_cim
        if 'fem3' in url: mode = 10
        addDir(name.encode('utf-8'), url, mode, iconimage, fanart, musor_id, '1')
		
def musor_lista_TV2_class(): #TV2 Klasszikusok
    r = client.request(url)
    m = client.parseDOM(r, 'div', attrs={'id': 'musorokdropdown'})
    m = client.parseDOM(m, 'a'),client.parseDOM(m, 'a', ret='href')
    m = zip(m[0],m[1])
    for name, link in m:
        try: name = client.replaceHTMLCodes(name)
        except: pass
        addDir(name.encode('utf-8'), link, 8, iconimage, fanart, '', '1')

def musor_lista_mplus(): #Mozi+
    addDir('[COLOR orange]''Teljes filmek''[/COLOR]', url + 'teljes_filmek/oldal', 11, os.path.join(artPath, 'movie.png'), fanart, '', '1')
    addDir('[COLOR orange]''Videók''[/COLOR]', url + 'videok/oldal', 11, os.path.join(artPath, 'video.png'), fanart, '', '1')

def musor_lista_izaura():
    addDir('[COLOR orange]''Videók''[/COLOR]', url + '/videok/oldal', 28, os.path.join(artPath, 'video.png'), fanart, '', '1')
    r = client.request(url)
    m = client.parseDOM(r, 'div', attrs={'id': 'dropdown_sorozataink'})
    m = client.parseDOM(m, 'a'),client.parseDOM(m, 'a', ret='href')
    m = zip(m[0],m[1])
    for name, link in m:
        try: name = client.replaceHTMLCodes(name)
        except: pass
        addDir(name.encode('utf-8'),url + link + '/oldal', 12, iconimage, fanart, '', '1')
   
def musor_lista_jockytv():
    addDir('[COLOR orange]''Teljes filmek''[/COLOR]', url + '/cimke/teljes filmek/oldal', 23, os.path.join(artPath, 'movie.png'), fanart, '', '1')
    addDir('[COLOR orange]''Videók''[/COLOR]', url + '/search/sorozat/oldal', 23, os.path.join(artPath, 'video.png'), fanart, '', '1')	
		
########################

def epizod_lista_TV2():
    r = client.request(url + '/videok/oldal' + page + '?keyword=&datumtol=2000-01-01&datumig=' + current_date + '&musorid=' + description)
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*balra\s*'})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*balra\s*margin10b\s*'})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), 'http://tv2.hu' + link, 20, 'http://tv2.hu' + img, '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 7, '', '', description, str(int(page) + 1))

def tv2_filmek():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem_nagy'})
   
    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/musoraink/teljes_filmek/oldal' + link, 20, 'https://tv2.hu/' + img,  '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'következő' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 24, '', '', '', str(int(page) + 1))
    return		
		
def tv2_videok():	
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'id': 'leftblock'})
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi balra  '})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi balra  margin10b  '})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/videok/oldal' + link, 20, 'https://tv2.hu/' + img,  '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'class="pager"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 25, '', '', '', str(int(page) + 1))
    return		
	
def epizod_lista_TV2_class():
    r = client.request('http://tv2.hu' + url + '/oldal' + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*'})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*margin10b\s*'})
    
    for i in result:
        try:
            name = client.parseDOM(i, 'span')
            name = client.parseDOM(name, 'a')
            img = client.parseDOM(i, 'img', ret='src')[0]
            link = client.parseDOM(i, 'a', ret='href')[0]
            addFile(name[0].encode('utf-8') + ' - ' + name[1].encode('utf-8'), 'http://tv2.hu' + link, 20, 'http://tv2.hu' + img, 'TV2 Klasszikusok', '', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 8, '', '', '', str(int(page) + 1))
                      
def epizod_lista_sTV2():
    r = client.request(url + '/videok/oldal' + page + '?keyword=&datumtol=2000-01-01&datumig=' + current_date + '&musorid=' + description)
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*'})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*margin10b\s*'})
 
    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), url + link, 20, 'https://tv2.hu' + img, '', 'SuperTV2', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 9, '', '', description, str(int(page) + 1))

def supertv2_filmek():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'id': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem_nagy'})
   
    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/supertv2/musoraink/teljes_filmek' + link, 20, 'https://tv2.hu/' + img,  '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'következő' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 26, '', '', '', str(int(page) + 1))
    return

def supertv2_videok():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'id': 'listablokk_wrapper'})
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*'})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*margin10b\s*'})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/supertv2' + link, 20, 'https://tv2.hu/' + img,  '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'class="pager"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 27, '', '', '', str(int(page) + 1))
    return		
		
def epizod_lista_fem3():
    r = client.request(url + '/videok/oldal' + page + '?keyword=&datumtol=2000-01-01&datumig=' + current_date + '&musorid=' + description)
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*'})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*margin10b\s*'})

    for i in result:
        try:
            name = client.parseDOM(i, 'div')
            img = client.parseDOM(i, 'img', ret='src')[0]
            link = client.parseDOM(i, 'a', ret='href')[0]
            addFile(name[0].encode('utf-8') + ' - ' + name[1].encode('utf-8'), url + link, 20, 'https://tv2.hu' + img, '', 'FEM3', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 10, '', '', description, str(int(page) + 1))

def epizod_lista_mplus():
    r = client.request(url + page)
    r = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    r = r[0].replace('\n','')
    result = zip(client.parseDOM(r, 'a', ret='href'),client.parseDOM(r, 'a'))
    
    for i in result:
        try:
            name = client.parseDOM(i[1], 'div', attrs={'class': 'cim'})[0]
            if 'teljes_filmek' in url: name = name.rsplit('-', 1)[0].strip()
            name = client.replaceHTMLCodes(name)
            img = client.parseDOM(i[1], 'img', ret='src')[0]
            img = urlparse.urljoin(url, img)
            addFile(name.encode('utf-8'), 'https://tv2.hu/moziplusztv/' + i[0], 20, img, '', 'Mozi+', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 11, '', '', '', str(int(page) + 1))

def epizod_lista_izaura():
    r = client.request(url + page)
    r = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    r = r[0].replace('\n','')
    result = client.parseDOM(r, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'http://izauratv.hu' + link, 20, 'https://tv2.hu' + img, '', 'Izaura TV', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 12, '', '', '', str(int(page) + 1))
    return

def izaura_videok():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/izauratv/videok/oldal' + link, 20, 'https://tv2.hu' + img, '', 'Izaura TV', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 28, '', '', '', str(int(page) + 1))
    return

def epizod_lista_prime():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'http://tv2csoport.hu' + link, 20, 'http://tv2csoport.hu' + img, '', 'Prime', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 13, '', '', '', str(int(page) + 1))
    return

def epizod_lista_chili():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = re.search('>([^<]+)', name).group(1)
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/lichitv/' + link, 20, 'https://tv2.hu' + img, '', 'Lichi TV', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 14, '', '', '', str(int(page) + 1))
    return
	
def epizod_lista_kiwitv():
    r = client.request(url + page)
    r = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    r = r[0].replace('\n','')
    result = zip(client.parseDOM(r, 'a', ret='href'),client.parseDOM(r, 'a'))
    
    for i in result:
        try:
            name = client.parseDOM(i[1], 'div', attrs={'class': 'cim'})[0]            
            name = client.replaceHTMLCodes(name)
            img = client.parseDOM(i[1], 'img', ret='src')[0]
            img = urlparse.urljoin(url, img)
            addFile(name.encode('utf-8'), 'https://tv2.hu/kiwitv/videok/oldal' + i[0], 20, img , '', 'Kiwi TV', IsPlayable=True)
        
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 15, '', '', '', str(int(page) + 1))
    return
	
def epizod_lista_zenebutik():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'pagewrapper'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/zenebutik/videok/oldal' + link, 20, 'https://tv2.hu' + img, '', 'Zenebutik', IsPlayable=True)
        except:
            pass
    if '/assets/next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 17, '', '', '', str(int(page) + 1))
    return
	
def epizod_lista_humorplusz():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem_nagy'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), 'http://humorplusz.hu' + link, 20, 'https://tv2.hu' + img, '', 'Humor+', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 18, '', '', '', str(int(page) + 1))
    return
	
def epizod_lista_jockytv():	
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), 'http://jockytv.hu' + link, 20, 'https://tv2.hu' + img, '', 'Jocky TV', IsPlayable=True)
        except:
            pass
    if 'class="next"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 23, '', '', '', str(int(page) + 1))
    return

def epizod_lista_moziverzum():
    r = client.request(url + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), 'https://tv2.hu/moziverzum/filmek/oldal' + link, 20, 'https://tv2.hu/' + img,  '', 'Moziverzum', IsPlayable=True)
        except:
            pass
    if 'class="next"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 16, '', '', '', str(int(page) + 1))
    return
	
def tenyek_adasok():
    query = urlparse.urljoin(url, '/osszes_videok/oldal' + page + '&datumig=' + current_date)
    r = client.request(query)
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_ta'})
    for item in result:
        try:
            date = client.parseDOM(item, 'div', attrs={'class': 'datum'})[0].encode('utf-8')
            
            title = client.parseDOM(item, 'a')[-1]
            title = re.search('>(.*)', title).group(1)
            title = title.encode('utf-8')
            
            img = client.parseDOM(item, 'img', ret='src')[0].encode('utf-8')
            if img.startswith('//'): img = 'http:' + img
            
            link = client.parseDOM(item, 'a', ret='href')[0].encode('utf-8')
            link = urlparse.urljoin(url, link)

            try: plot = client.parseDOM(item, 'div', attrs={'class': 'lead'})[0].encode('utf-8')
            except: plot = ''

            addFile('%s - %s' % (date, title), link, 20, img, os.path.join(artPath, 'tenyek_b.jpg'), plot, IsPlayable=True)
        except:
            pass

    if 'class="next"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 21, '', '', '', str(int(page) + 1))
    return

def getVideo():
    from resources.lib import m3u8_parser
    r = client.request(url)
    try:
        json_url = re.search('jsonUrl\s*=\s*[\'"]([^\'"]+)', r).group(1)
        json_url = re.sub('^//', 'http://', json_url)
        r = client.request(json_url)

        json_data = json.loads(r)
        m3u_url = json_data['bitrates']['hls']
        m3u_url = json_url = re.sub('^//', 'http://', m3u_url)
        r = client.request(m3u_url)
        
        root = os.path.dirname(m3u_url)
        sources = m3u8_parser.parse(r)
        try: sources.sort(key=lambda x: int(x['resolution'].split('x')[0]), reverse=True)
        except: pass

        auto_pick = control.setting('autopick') == '1'

        if len(sources) == 1 or auto_pick == True:
            source = sources[0]['uri']
        else:
            result = xbmcgui.Dialog().select(u'Min\u0151s\u00E9g', [str(source['resolution']) if 'resolution' in source else 'Unknown' for source in sources])
            if result == -1:
                source = sources[0]['uri']
            else:
                source = sources[result]['uri']
        stream_url = root + '/' + source

        item = control.item(path=stream_url)
        item.setArt({'icon': iconimage, 'thumb': iconimage})
        item.setInfo(type='Video', infoLabels = {'Title': name})
        control.resolve(int(sys.argv[1]), True, item)
    except:
        return

def addDir(name, url, mode, iconimage, fanart, description, page):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&page="+urllib.quote_plus(page)
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

def addFile(name, url, mode, iconimage, fanart, description, IsPlayable=False):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    if not IsPlayable == False: liz.setProperty("IsPlayable", "true")
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    control.content(int(sys.argv[1]), 'movies')

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param

	
params = get_params()
url = None
name = None
mode = None
iconimage = None
fanart = None
description = None
page = None
maxbitrate=0
simpleDownloader=False


try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage = urllib.unquote_plus(params["iconimage"])
except:
    pass
try:        
    mode = int(params["mode"])
except:
    pass
try:        
    fanart = urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    page = urllib.unquote_plus(params["page"])
except:
    pass
try:        
    description = urllib.unquote_plus(params["description"])
except:
    pass

	
if mode==None:
    main_folders()
elif mode==1:
    musor_listaTV2()
elif mode==2:
    musor_lista_TV2_class()
elif mode==3:
    musor_lista_sTV2()
elif mode==4:
    musor_lista_mplus()
elif mode==5:
    musor_lista_izaura()
elif mode==6:
    musor_lista_prime()
elif mode==7:
    epizod_lista_TV2()
elif mode==8:
    epizod_lista_TV2_class()
elif mode==9:
    epizod_lista_sTV2()
elif mode==10:
    epizod_lista_fem3()
elif mode==11:
    epizod_lista_mplus()
elif mode==12:
    epizod_lista_izaura()
elif mode==13:
    epizod_lista_prime()
elif mode==14:
    epizod_lista_chili()	
elif mode==15:
    epizod_lista_kiwitv()	
elif mode==16:
    epizod_lista_moziverzum()
elif mode==17:
    epizod_lista_zenebutik()
elif mode==18:
    epizod_lista_humorplusz()
elif mode==19:
    musor_lista_fem3()	
elif mode==20:
    getVideo()
elif mode==21:
    tenyek_adasok()	
elif mode==22:
    musor_lista_jockytv()
elif mode==23:
    epizod_lista_jockytv()	
elif mode==24:
	tv2_filmek()
elif mode==25:
    tv2_videok()
elif mode==26:
    supertv2_filmek()
elif mode==27:
    supertv2_videok()
elif mode==28:
    izaura_videok()
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))