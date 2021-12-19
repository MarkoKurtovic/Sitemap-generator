import sys
import mysql.connector
from mysql.connector import Error


cnx = mysql.connector.connect(host = 'localhost',database = 'landmont',user = 'root',password = '')

FIND_AVAILABLE_PRODUCTS_QUERY = "SELECT l.id, l.locale, l.updated_at, l.title_slug, lt.slug, m.slug, c.slug AS city FROM lands as l JOIN land_types as lt ON lt.id = l.land_type_id JOIN municipalities as m ON l.municipality_id = m.id JOIN cities AS c ON c.id = l.city_id order by l.locale='sr'"
cnx = mysql.connector.connect(host = 'localhost',database = 'landmont',user = 'root',password = '')
print("Connection to database established.")

cursor = cnx.cursor(dictionary=True)
cursor.execute(FIND_AVAILABLE_PRODUCTS_QUERY)
available_products = cursor.fetchall()



FIND_AVAILABLE_BLOGS_QUERY = "select locale, post_date, title_slug, updated_at from blogs order by locale='sr'"
cnx = mysql.connector.connect(host = 'localhost',database = 'landmont',user = 'root',password = '')
print("Connection to database established.")

cursor = cnx.cursor(dictionary=True)
cursor.execute(FIND_AVAILABLE_BLOGS_QUERY)
available_blogs = cursor.fetchall()


with open('sitemap9.xml', "w") as file:
    file.write(
    	  '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n\txmlns:xhtml="http://www.w3.org/1999/xhtml">'
      )
    file.write("\n\t<url>\n\t\t<loc>https://land-montenegro.com/en</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>1</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/en/lands-on-sale</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/en/exclusive-lands</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>1</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/en/blog</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/en/contact</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>monthly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/sr</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>1</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/sr/zemljista-na-prodaju</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>1</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/sr/ekskluzivna-zemljista</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/sr/blog</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>weekly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>\n\t<url>\n\t\t<loc>https://land-montenegro.com/sr/kontakt</loc>\n\t\t<lastmod>2021-10-30</lastmod>\n\t\t<changefreq>monthly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>")
    for product in available_products:
        if product['locale'] == 'en':
          details = '/land-details/'
        else:
          details = '/zemljiste-detalji/'
        product_date = str(product['updated_at'])
        url = 'https://land-montenegro.com/'+product['locale'] + details + product['city']+ '/' + product['slug'] + '/' + product['title_slug'] + '/'+ str(product['id'])
        sitemap_template="\n\t<url>\n\t\t<loc>"+ url +"</loc>\n\t\t<lastmod>"+ product_date[ 0 : product_date.index(" ")] +"</lastmod>\n\t\t<changefreq>monthly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>"
        sitemap_template = sitemap_template.replace('  ', '\n')
        file.write(sitemap_template)
    for blog in available_blogs:
      blog_date = str(blog['post_date'])
      blog_date.split(" ", 1)[0]
      blog_url = 'https://land-montenegro.com/'+blog['locale'] +'/blog/' + blog_date + '/' + blog['title_slug']
      sitemap_template_blog="\n\t<url>\n\t\t<loc>"+ blog_url +"</loc>\n\t\t<lastmod>"+ blog_date+"</lastmod>\n\t\t<changefreq>monthly</changefreq>\n\t\t<priority>0.9</priority>\n\t</url>"
      sitemap_template_blog = sitemap_template_blog.replace('  ', '\n')
      file.write(sitemap_template_blog)

    file.write(
    	"\n</urlset>"
      )
