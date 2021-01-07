# -*- coding: utf-8 -*-
import xbmc, xbmcgui, urllib, re, xbmcplugin, datetime, random, os, json, urlparse
from resources.lib import client, control

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
artPath = control.artPath()
base_url = "https://tv2.hu"
def main_folders():
    addDir('TV2', base_url, 1, os.path.join(artPath, 'tv2.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('TV2 Klasszikusok', '%s/tv2klasszikusok/' % base_url, 2, os.path.join(artPath, 'tv2class.jpg'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('SuperTV2', '%s/supertv2' % base_url, 3, os.path.join(artPath, 'supertv2.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('FEM3', '%s/fem3' % base_url, 19, os.path.join(artPath, 'fem3.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('Mozi+', '%s/moziplusztv/videok/oldal' % base_url, 11, os.path.join(artPath, 'moziplusz.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Izaura TV', '%s/izauratv' % base_url, 5, os.path.join(artPath, 'izauratv.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '')
    addDir('Prime', '%s/prime/search/' % base_url, 13, os.path.join(artPath, 'prime.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('TV2 Séf', '%s/tv2sef/search/' % base_url, 14, os.path.join(artPath, 'sef.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('TV2 Kids', '%s/tv2kids/search/' % base_url, 15, os.path.join(artPath, 'kids.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Zenebutik', '%s/zenebutik/search/' % base_url, 17, os.path.join(artPath, 'zenebutik.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('TV2 Comedy', '%s/tv2comedy/search/' % base_url, 18, os.path.join(artPath, 'comedy.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Jocky TV', '%s/jockytv/search/' % base_url, 23, os.path.join(artPath, 'jockytv.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    addDir('Moziverzum', '%s/moziverzum/search/' % base_url, 16, os.path.join(artPath, 'moziverzum.png'), os.path.join(artPath, 'tv2csop.jpg'), '', '1')
    return

def musor_listaTV2():  #TV2
    addDir('[COLOR orange]''Teljes filmek''[/COLOR]', url + '/search/teljes+film/oldal', 24, os.path.join(artPath, 'movie.png'), fanart, '', '1')
    addDir('[COLOR orange]''Összes videó''[/COLOR]', url, 7, iconimage, fanart, '', '1')
    r = client.request(url + '/videok/')
    m = re.compile('value="([0-9]+)" > (.+?) </').findall(r)
    for musor_id, musor_cim in m:
        try: name = client.replaceHTMLCodes(musor_cim.decode('utf-8')).strip()
        except: name = musor_cim.strip()
        addDir(name.encode('utf-8'), url, 7, iconimage, fanart, musor_id, '1')

def musor_lista_sTV2(): #SuperTv2
    addDir('[COLOR orange]''Teljes filmek''[/COLOR]', url + '/musoraink/teljes_filmek/oldal', 26, os.path.join(artPath, 'movie.png'), fanart, '', '1')
    addDir('[COLOR orange]''Összes videó''[/COLOR]', url, 9, iconimage, fanart, '', '1')
    r = client.request(url + '/videok/')
    m = re.compile('value="([0-9]+)" > (.+?) </').findall(r)
    for musor_id, musor_cim in m:
        try: name = client.replaceHTMLCodes(musor_cim.decode('utf-8')).strip()
        except: name = musor_cim.musor_cim.strip()
        addDir(name.encode('utf-8'), url, 9, iconimage, fanart, musor_id, '1')

def musor_lista_fem3():
    addDir('[COLOR orange]''Összes videó''[/COLOR]', url, 10, iconimage, fanart, '', '1')
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
        addDir(name.encode('utf-8'), "%s%s" % (base_url, link), 8, iconimage, fanart, '', '1')

def musor_lista_mplus(): #Mozi+
    addDir('[COLOR orange]''Videók''[/COLOR]', url + 'videok/oldal', 11, os.path.join(artPath, 'video.png'), fanart, '', '1')

def musor_lista_izaura():
    addDir('[COLOR orange]''Videók''[/COLOR]', url + '/search/', 28, os.path.join(artPath, 'video.png'), fanart, '', '1')
    r = client.request(url)
    m = client.parseDOM(r, 'div', attrs={'id': 'dropdown_sorozataink'})
    m = client.parseDOM(m, 'a'),client.parseDOM(m, 'a', ret='href')
    m = zip(m[0],m[1])
    for name, link in m:
        try: name = client.replaceHTMLCodes(name)
        except: pass
        addDir(name.encode('utf-8'), "%s%s/oldal" % (base_url, link), 12, iconimage, fanart, '', '1')
   	
########################

def epizod_lista_TV2():
    r = client.request("%s/videok/oldal%s?keyword=%s&datumtol=2000-01-01&datumig=%s&musorid=%s" %(url, page, keyword, current_date, description))
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi[^"]*'})

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '7')
    else:
        if description:
            musorid = client.parseDOM(r, 'select', attrs={'name': 'musorid'})[0]
            option = client.parseDOM(musorid, 'option', attrs={'value': description})[0].strip().encode('utf-8')
        else:
            option = "Összes videó"
        addDir('[COLOR orange]''%s szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % (option, urllib.unquote_plus(keyword)), url, 7, os.path.join(artPath, 'tv2.png'), '', description, page, keyword)

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), '%s%s' % (base_url, link), 20, "%s%s" % (base_url, img), '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 7, '', '', description, str(int(page) + 1), keyword)

def tv2_filmek():
    r = client.request("%s%s" % (url, page)).decode('iso-8859-2').encode('utf-8')
    result = client.parseDOM(r, 'div', attrs={'class': 'oldalbefoglalo'})[0]
    result = client.parseDOM(result, 'div', attrs={'class': 'listaelem_kereses[^"]*'})
    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0].encode('iso-8859-2')
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name, '%s%s' % (base_url, link), 20, "%s%s" % (base_url, img),  '', 'TV2', IsPlayable=True)
        except:
            pass

    if '/search/teljes film/oldal%s' % str(int(page)+1) in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 24, '', '', '', str(int(page) + 1))
    return		
		

def epizod_lista_TV2_class():
    r = client.request(url + '/oldal' + page)
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*'})
    result += client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi\s*margin10b\s*'})
    
    for i in result:
        try:
            name = client.parseDOM(i, 'span')
            name = client.parseDOM(name, 'a')
            img = client.parseDOM(i, 'img', ret='src')[0]
            link = client.parseDOM(i, 'a', ret='href')[0]
            addFile(name[0].encode('utf-8') + ' - ' + name[1].encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), 'TV2 Klasszikusok', '', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 8, '', '', '', str(int(page) + 1))
                      
def epizod_lista_sTV2():
    r = client.request("%s/videok/oldal%s?keyword=%s&datumtol=2000-01-01&datumig=%s&musorid=%s" % (url, page, keyword, current_date, description))
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi[^"]*'})

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '7')
    else:
        if description:
            musorid = client.parseDOM(r, 'select', attrs={'name': 'musorid'})[0]
            option = client.parseDOM(musorid, 'option', attrs={'value': description})[0].strip().encode('utf-8')
        else:
            option = "Összes videó"
        addDir('[COLOR orange]''%s szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % (option, urllib.unquote_plus(keyword)), url, 7, os.path.join(artPath, 'supertv2.png'), '', description, page, keyword)

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'SuperTV2', IsPlayable=True)
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
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img),  '', 'TV2', IsPlayable=True)
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
            addFile(name.encode('utf-8'), "%s%s" %(base_url, link), 20, "%s%s" % (base_url, img),  '', 'TV2', IsPlayable=True)
        except:
            pass
    if 'class="pager"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 27, '', '', '', str(int(page) + 1))
    return		
		
def epizod_lista_fem3():
    r = client.request("%s/videok/oldal%s?keyword=%s&datumtol=2000-01-01&datumig=%s&musorid=%s" % (url, page, keyword, current_date, description))
    result = client.parseDOM(r, 'div', attrs={'class': 'listaelem_kicsi[^"]*'})

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '10')
    else:
        if description:
            musorid = client.parseDOM(r, 'select', attrs={'name': 'musorid'})[0]
            option = client.parseDOM(musorid, 'option', attrs={'value': description})[0].strip().encode('utf-8')
        else:
            option = "Összes videó"
        addDir('[COLOR orange]''%s szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % (option, urllib.unquote_plus(keyword)), url, 7, os.path.join(artPath, 'supertv2.png'), '', description, page, keyword)

    for i in result:
        try:
            name = client.parseDOM(i, 'div')
            img = client.parseDOM(i, 'img', ret='src')[0]
            link = client.parseDOM(i, 'a', ret='href')[0]
            addFile(name[0].encode('utf-8') + ' - ' + name[1].encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'FEM3', IsPlayable=True)
        except:
            pass
    if 'következő oldal' in r or 'következő  &raquo;' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 10, '', '', description, str(int(page) + 1))

def epizod_lista_mplus():
    r = client.request("%s%s?keyword=%s" % (url, page, keyword))

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '11')
    else:
        addDir('[COLOR orange]''Mozi+ szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 11, os.path.join(artPath, 'moziplusz.png'), '', description, page, keyword)
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
            addFile(name.encode('utf-8'), "%s%s" % (base_url, i[0]), 20, img, '', 'Mozi+', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 11, '', '', description, str(int(page) + 1), keyword)

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
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'Izaura TV', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 12, '', '', '', str(int(page) + 1))
    return

def izaura_videok():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))
    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '28')
    else:
        addDir('[COLOR orange]''Izaura videók szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 28, os.path.join(artPath, 'izaura.png'), '', description, page, keyword)

    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'Izaura TV', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 28, '', '', description, str(int(page) + 1), keyword)
    return

def epizod_lista_prime():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '13')
    else:
        addDir('[COLOR orange]''Prime szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 13, os.path.join(artPath, 'prime.png'), '', description, page, keyword)

    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'Prime', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 13, '', '', description, str(int(page) + 1), keyword)
    return

def epizod_lista_sef():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '14')
    else:
        addDir('[COLOR orange]''TV2 Séf szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 14, os.path.join(artPath, 'sef.png'), '', description, page, keyword)

    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = re.search('>([^<]+)', name).group(1)
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'TV2 Séf', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 14, '', '', description, str(int(page) + 1), keyword)
    return
	
def epizod_lista_kids():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '15')
    else:
        addDir('[COLOR orange]''TV2 Kids szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 15, os.path.join(artPath, 'kids.png'), '', description, page, keyword)

    r = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    r = r[0].replace('\n','')
    result = zip(client.parseDOM(r, 'a', ret='href'),client.parseDOM(r, 'a'))
    
    for i in result:
        try:
            name = client.parseDOM(i[1], 'div', attrs={'class': 'cim'})[0]            
            name = client.replaceHTMLCodes(name)
            img = client.parseDOM(i[1], 'img', ret='src')[0]
            img = urlparse.urljoin(url, img)
            addFile(name.encode('utf-8'), "%s%s" % (base_url, i[0]), 20, img , '', 'Kiwi TV', IsPlayable=True)
        
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 15, '', '', description, str(int(page) + 1), keyword)
    return
	
def epizod_lista_zenebutik():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))

    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '17')
    else:
        addDir('[COLOR orange]''Zenebutik szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 17, os.path.join(artPath, 'zenebutik.png'), '', description, page, keyword)

    result = client.parseDOM(r, 'div', attrs={'class': 'pagewrapper'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            name = client.parseDOM(i, 'a', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(name)
            link = client.parseDOM(i, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'Zenebutik', IsPlayable=True)
        except:
            pass
    if '/assets/next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 17, '', '', description, str(int(page) + 1), keyword)
    return
	
def epizod_lista_comedy():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))
    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '18')
    else:
        addDir('[COLOR orange]''TV2 Comedy szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 18, os.path.join(artPath, 'comedy.png'), '', description, page, keyword)
    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.replaceHTMLCodes(client.parseDOM(cim, 'a')[0])
            link = client.parseDOM(cim, 'a', ret='href')[0]
            img = client.parseDOM(i, 'img', ret='src')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'Comedy', IsPlayable=True)
        except:
            pass
    if '/pager_next' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 18, '', '', description, str(int(page) + 1), keyword)
    return
	
def epizod_lista_jockytv():	
    r = client.request("%s%s/oldal%s" % (url, keyword, page))
    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '23')
    else:
        addDir('[COLOR orange]''JockyTV szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 23, os.path.join(artPath, 'jocky.png'), '', description, page, keyword)

    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img), '', 'Jocky TV', IsPlayable=True)
        except:
            pass
    if 'class="next"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 23, '', '', description, str(int(page) + 1), keyword)
    return

def epizod_lista_moziverzum():
    r = client.request("%s%s/oldal%s" % (url, keyword, page))
    if len(keyword) == 0:
        addDir('[COLOR orange]''Szűkítés''[/COLOR]', url, 29, '', '', description, '16')
    else:
        addDir('[COLOR orange]''Moziverzum szűrés: [COLOR lime]%s[/COLOR]''[/COLOR]' % urllib.unquote_plus(keyword), url, 16, os.path.join(artPath, 'moziverzum.png'), '', description, page, keyword)

    result = client.parseDOM(r, 'div', attrs={'class': 'leftblock'})
    result = client.parseDOM(result, 'div', attrs={'class': 'cikk_listaelem'})

    for i in result:
        try:
            img = client.parseDOM(i, 'img', ret='src')[0]
            cim = client.parseDOM(i, 'div', attrs={'class': 'cim'})[0]
            name = client.parseDOM(cim, 'a')[0]
            link = client.parseDOM(cim, 'a', ret='href')[0]
            addFile(name.encode('utf-8'), "%s%s" % (base_url, link), 20, "%s%s" % (base_url, img),  '', 'Moziverzum', IsPlayable=True)
        except:
            pass
    if 'class="next"' in r:
        addDir('[COLOR green]''Következő oldal''[/COLOR]', url, 16, '', '', description, str(int(page) + 1), keyword)
    return
	
def getVideo():
    from resources.lib import m3u8_parser
    r = client.request(url)
    try:
        json_url = re.search('jsonUrl\s*=\s*[\'"]([^\'"]+)', r).group(1)
        json_url = re.sub('^//', 'https://', json_url)
        r = client.request(json_url)

        json_data = json.loads(r)
        m3u_url = json_data['bitrates']['hls']
        m3u_url = json_url = re.sub('^//', 'https://', m3u_url)
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

def addDir(name, url, mode, iconimage, fanart, description, page, keyword=""):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&page="+urllib.quote_plus(page)+'&keyword='+urllib.quote_plus(keyword)
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

def getText(title, hidden=False):
    search_text = ''
    keyb = xbmc.Keyboard('', title, hidden)
    keyb.doModal()

    if (keyb.isConfirmed()):
        search_text = keyb.getText()

    return search_text

def doSearch():
    search_text = getText(u'Add meg a keresend\xF5 kifejez\xE9st')
    if search_text != '':
        global keyword
        global page
        functionIdx = page
        keyword = urllib.quote_plus(search_text)
        page = '1'
        global mode2Sub
        mode2Sub[int(functionIdx)]()
	
params = get_params()
url = None
name = None
mode = None
iconimage = None
fanart = None
description = ""
page = None
maxbitrate=0
simpleDownloader=False
keyword = ""

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
try:
    keyword = urllib.unquote_plus(params["keyword"])
except:
    pass
	


mode2Sub = {None: main_folders, 
               1: musor_listaTV2, 
               2: musor_lista_TV2_class, 
               3: musor_lista_sTV2, 
               4: musor_lista_mplus, 
               5: musor_lista_izaura, 
               7: epizod_lista_TV2, 
               8: epizod_lista_TV2_class, 
               9: epizod_lista_sTV2, 
              10: epizod_lista_fem3, 
              11: epizod_lista_mplus, 
              12: epizod_lista_izaura, 
              13: epizod_lista_prime, 
              14: epizod_lista_sef, 
              15: epizod_lista_kids, 
              16: epizod_lista_moziverzum, 
              17: epizod_lista_zenebutik, 
              18: epizod_lista_comedy, 
              19: musor_lista_fem3, 
              20: getVideo, 
              23: epizod_lista_jockytv, 
              24: tv2_filmek, 
              26: supertv2_filmek, 
              27: supertv2_videok, 
              28: izaura_videok, 
              29: doSearch}

mode2Sub[mode]()
xbmcplugin.endOfDirectory(int(sys.argv[1]))