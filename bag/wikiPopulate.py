import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language.settings')
import django
django.setup()

from wiki.models import Category, Page
import random
def populate():
    # Python
    category = addCategory('Python')
    addPage(category, '官方 Python 教材', 'http://docs.python.org/3/')
    addPage(category, '如何像電腦科學家一樣思考', 'http://www.greenteapress.com/thinkpython/')
    addPage(category, '10 分鐘內學好 Python', 'http://www.korokithakis.net/tutorials/python/')
    addPage(category, '簡單學習 Python', 'http://www.tutorialspoint.com/python/')
    # PHP
    category = addCategory('PHP')
    addPage(category, '官方 PHP 教材', 'http://http://php.net/docs.php')
    addPage(category, 'W3C-PHP 教材', 'http://www.w3schools.com/php/')
    addPage(category, '簡單學習 PHP', 'http://www.tutorialspoint.com/php/')
    # Java
    category = addCategory('Java')
    addPage(category, '官方 Java 教材', 'http://docs.oracle.com/javase/tutorial/java/')
    addPage(category, 'Java 精要', 'http://www.oracle.com/technetwork/java/index-138747.html')
    addPage(category, '簡單學習 Java', 'http://www.tutorialspoint.com/java/')
    # C
    category = addCategory('C')
    addPage(category, 'C 語言教材', 'http://www.programiz.com/c-programming')
    addPage(category, 'C 語言精要', 'http://www.cprogramming.com/tutorial/c-tutorial.html')
    addPage(category, '簡單學習 C', 'http://www.tutorialspoint.com/cprogramming/')
    addPage(category, '在 Youtube 學習 C', 'https://www.youtube.com/watch?v=2NWeucMKrLI')
    # JavaScript
    category = addCategory('JavaScript')
    addPage(category, '簡單學習 JavaScript', 'http://www.tutorialspoint.com/javascript/')
    addPage(category, 'JavaScript 資訊', 'http://javascript.info/')
    # jQuery
    category = addCategory('jQuery')
    addPage(category, '簡單學習 jQuery', 'http://www.tutorialspoint.com/jquery/')
    addPage(category, 'jQuery 學習中心', 'https://learn.jquery.com/')
    # Matlab
    category = addCategory('Matlab')
    addPage(category, '簡單學習 Matlab', 'http://www.tutorialspoint.com/matlab/')
    addPage(category, '學習 Matlab', 'http://www.mathworks.com/support/learn-with-matlabtutorials.html?requestedDomain=www.mathworks.com')
    
    # Print everything
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(category.name, '--', page.title)
             
             
def addCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = random.randint(0, 20)
    category.likes = random.randint(0, 20)
    category.save()
    return category
def addPage(category, title, url):
    page = Page.objects.get_or_create(category=category, title=title, url=url)[0]
    page.views = random.randint(0, 20)
    page.save()

if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 