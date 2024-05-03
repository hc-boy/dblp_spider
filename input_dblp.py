start_urls = ["https://dblp.org/db/journals/toplas/index.html","https://dblp.org/db/journals/tosem/index.html","https://dblp.org/db/journals/tse/index.html",
                 "https://dblp.org/db/journals/ase/index.html", "https://dblp.org/db/conf/pldi/index.html", "https://dblp.org/db/conf/popl/index.html",
                 "https://dblp.org/db/conf/sigsoft/index.html", "https://dblp.org/db/conf/oopsla/index.html", "https://dblp.org/db/conf/kbse/index.html", 
                 "https://dblp.org/db/conf/icse/index.html", "https://dblp.org/db/conf/issta/index.html"]  # 要爬的dblp会议/期刊的主页
# start_urls = ["https://dblp.org/db/conf/icse/index.html"]
year = 10  # how many recent year
keyword = r'\b(GUI|vision)\b' #edit the reg-ex to costumize search option
delay = 1.8 #download minimum delay, in second